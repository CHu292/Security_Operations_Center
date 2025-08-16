package com.example.myapplication

import androidx.room.ColumnInfo
import androidx.room.Entity
import androidx.room.PrimaryKey

@Entity
data class Message(
    @PrimaryKey val id: Int?,
    @ColumnInfo(name = "message") val message: String,
    @ColumnInfo(name = "date") val date: String
) {
}