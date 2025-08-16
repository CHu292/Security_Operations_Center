package com.example.myapplication

import retrofit2.Call
import retrofit2.http.GET
import retrofit2.http.Query

interface ApiInterface {
    @GET("current.json")
    fun getWeatherFocast(
        @Query("key") key: String,
        @Query("q") city: String,
        @Query("aqi") aqi: String
    ): Call<WeatherResponse>
}