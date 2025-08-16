package com.example.myapplication

import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.TextView
import androidx.recyclerview.widget.DiffUtil
import androidx.recyclerview.widget.ListAdapter
import androidx.recyclerview.widget.RecyclerView
import androidx.recyclerview.widget.RecyclerView.ViewHolder

class BlogAdapter(): ListAdapter<ItemBlog, ViewHolder>(object : DiffUtil.ItemCallback<ItemBlog>() {
    override fun areItemsTheSame(oldItem: ItemBlog, newItem: ItemBlog): Boolean {
        if (oldItem.type == ItemBlog.TYPE_NORMAL){
            return (oldItem as? ItemBlog.BlogItem)?.message?.id == (newItem as? ItemBlog.BlogItem)?.message?.id
        }
        return false
    }

    override fun areContentsTheSame(oldItem: ItemBlog, newItem: ItemBlog): Boolean {
        return false
    }
}) {

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): ViewHolder {
        val inflater = LayoutInflater.from(parent.context)
        return BlogViewHolder(inflater.inflate(R.layout.item_message, parent, false))
    }

    override fun onBindViewHolder(holder: ViewHolder, position: Int) {
        if (holder is BlogViewHolder) {
            (getItem(position) as? ItemBlog.BlogItem)?.message?.let {
                holder.bind(message = it)
            }
        }
    }

    class BlogViewHolder(item: View): RecyclerView.ViewHolder(item){
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

sealed class ItemBlog(val type: Int){
    class BlogItem(val message: Message): ItemBlog(TYPE_NORMAL)
    class RankingItem(val messages: List<Message>): ItemBlog(TYPE_RANKING)
    class FooterItem() : ItemBlog(TYPE_FOOTER)
    companion object {
        const val TYPE_NORMAL = 0
        const val TYPE_RANKING = 1
        const val TYPE_FOOTER = 2
    }
}