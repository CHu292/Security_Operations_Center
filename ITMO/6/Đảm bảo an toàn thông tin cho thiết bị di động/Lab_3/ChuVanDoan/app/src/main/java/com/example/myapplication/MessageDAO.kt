package com.example.myapplication

import androidx.room.Dao
import androidx.room.Insert
import androidx.room.Query

@Dao
interface MessageDAO {
    @Query("SELECT * FROM message")
    fun getAllMessage(): List<Message>

    @Insert
    fun insertMessage(vararg message: Message)
}