package com.example.myapplication

import android.content.Context
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.TextView
import androidx.recyclerview.widget.DiffUtil
import androidx.recyclerview.widget.ListAdapter
import androidx.recyclerview.widget.RecyclerView

class MessageAdapter(): ListAdapter<Message, MessageAdapter.ViewHolder>(object : DiffUtil.ItemCallback<Message>() {
    override fun areItemsTheSame(oldItem: Message, newItem: Message): Boolean {
        return oldItem.id == newItem.id
    }

    override fun areContentsTheSame(oldItem: Message, newItem: Message): Boolean {
        return oldItem == newItem
    }
}) {

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): ViewHolder {
        val inflater = LayoutInflater.from(parent.context)
        return ViewHolder(inflater.inflate(R.layout.item_message, parent, false))
    }

    override fun onBindViewHolder(holder: ViewHolder, position: Int) {
        holder.bind(getItem(position))
    }

    class ViewHolder(item: View): RecyclerView.ViewHolder(item){
        lateinit var tvMessage: TextView
        lateinit var tvDate: TextView
        init {
            tvMessage = item.findViewById<TextView>(R.id.tvMessage)
            tvDate = item.findViewById<TextView>(R.id.tvDate)
        }
        fun bind(message: Message){
            tvMessage.text = message.message
            tvDate.text = message.date
        }
    }
}