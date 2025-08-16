package com.example.myapplication

import android.os.Bundle
import android.util.Log
import android.widget.TextView
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import androidx.recyclerview.widget.LinearLayoutManager
import androidx.recyclerview.widget.RecyclerView
import androidx.room.Room
import com.google.android.material.button.MaterialButton
import com.google.android.material.textfield.TextInputEditText
import kotlinx.coroutines.GlobalScope
import kotlinx.coroutines.launch
import retrofit2.*
import retrofit2.converter.gson.GsonConverterFactory
import java.text.SimpleDateFormat
import java.util.*

class MainActivity : AppCompatActivity() {
    private lateinit var tvWeather: TextView
    private lateinit var tvHumidity: TextView
    private lateinit var tvTemperature: TextView
    private lateinit var btnUpdateInfo: MaterialButton
    private lateinit var btnSubmit: MaterialButton
    private lateinit var etMessage: TextInputEditText
    private lateinit var rvMessage: RecyclerView

    private val retrofit: Retrofit by lazy {
        Retrofit.Builder()
            .baseUrl(BASE_URL)
            .addConverterFactory(GsonConverterFactory.create())
            .build()
    }

    private val apiService: ApiInterface by lazy {
        retrofit.create(ApiInterface::class.java)
    }

    private val messageDAO: MessageDAO by lazy {
        Room.databaseBuilder(
            applicationContext,
            AppDatabase::class.java,
            "Message"
        ).build().messageDAO()
    }

    private var listMessage: List<Message> = listOf()
    private val mAdapter: MessageAdapter by lazy {
        MessageAdapter()
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        tvWeather = findViewById(R.id.tvWeather)
        tvHumidity = findViewById(R.id.tvHumidity)
        tvTemperature = findViewById(R.id.tvTemperature)
        btnUpdateInfo = findViewById(R.id.btnUpdateInfo)
        btnSubmit = findViewById(R.id.btnSubmit)
        etMessage = findViewById(R.id.etMessage)
        rvMessage = findViewById(R.id.rvMessage)

        rvMessage.apply {
            mAdapter.submitList(listMessage)
            adapter = mAdapter
            layoutManager = LinearLayoutManager(this@MainActivity)
        }

        loadDataFromLocal()

        btnUpdateInfo.setOnClickListener {
            loadDataFromServer()
        }

        btnSubmit.setOnClickListener {
            val message = etMessage.text?.toString().orEmpty()
            saveMessageToLocal(message)
        }
    }

    private fun loadDataFromServer() {
        val call = apiService.getWeatherFocast(
            key = KEY,
            city = CITY,
            aqi = "no"
        )
        call.enqueue(object : Callback<WeatherResponse> {
            override fun onResponse(
                call: Call<WeatherResponse>,
                response: Response<WeatherResponse>
            ) {
                if (response.isSuccessful) {
                    val weatherResponse = response.body()
                    tvWeather.text = weatherResponse?.current?.condition?.text
                    tvHumidity.text = "Humidity: ${weatherResponse?.current?.humidity}%"
                    tvTemperature.text = "Temperature: ${weatherResponse?.current?.tempC}°C"
                }
            }

            override fun onFailure(call: Call<WeatherResponse>, t: Throwable) {
                Log.e("Error", t.message ?: "Unknown error")
                Toast.makeText(this@MainActivity, "Error: ${t.message}", Toast.LENGTH_SHORT).show()
            }
        })
    }

    private fun loadDataFromLocal() {
        GlobalScope.launch {
            listMessage = messageDAO.getAllMessage()
            runOnUiThread {
                mAdapter.submitList(listMessage)
            }
        }
    }

    private fun saveMessageToLocal(content: String) {
        if (content.isBlank()) return
        val message = Message(null, content, getCurrentDate())
        GlobalScope.launch {
            messageDAO.insertMessage(message)
            loadDataFromLocal()
            runOnUiThread {
                etMessage.setText("")
            }
        }
    }

    private fun getCurrentDate(): String {
        val c: Date = Calendar.getInstance().time
        val df = SimpleDateFormat("dd-MMM-yyyy", Locale.getDefault())
        return df.format(c)
    }

    companion object {
        private const val BASE_URL = "http://api.weatherapi.com/v1/"
        private const val KEY = "02c41f75d5674893935155932241204"
        private const val CITY = "Saint Petersburg City"
    }
}
