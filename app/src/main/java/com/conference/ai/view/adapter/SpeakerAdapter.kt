package com.conference.ai.view.adapter

import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.ImageView
import android.widget.TextView
import androidx.recyclerview.widget.RecyclerView
import com.bumptech.glide.Glide
import com.bumptech.glide.request.RequestOptions
import com.conference.ai.R
import com.conference.ai.model.Conference
import com.conference.ai.model.Speaker
import java.text.SimpleDateFormat
import java.util.*
import kotlin.collections.ArrayList

class SpeakerAdapter(val speakerListener: SpeakerListener) : RecyclerView.Adapter<SpeakerAdapter.ViewHolder>() {

    var listSpeakers = ArrayList<Speaker>()

    class ViewHolder(itemView: View) : RecyclerView.ViewHolder(itemView) {
        val tvItemSpeakerName = itemView.findViewById<TextView>(R.id.tvItemSpeakerName)
        val tvItemSpeakerJobtitle = itemView.findViewById<TextView>(R.id.tvItemSpeakerJobtitle)
        val ivItemSpeakerImage = itemView.findViewById<ImageView>(R.id.ivItemSpeakerImage)
    }

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int) = SpeakerAdapter.ViewHolder(LayoutInflater.from(parent.context).inflate(
            R.layout.item_speaker, parent, false))

    override fun onBindViewHolder(holder: ViewHolder, position: Int) {
        val speaker = listSpeakers[position] as Speaker
        holder.tvItemSpeakerName.text = speaker.name
        holder.tvItemSpeakerJobtitle.text = speaker.jobtitle
        Glide.with(holder.itemView.context)
                .load(speaker.image)
                .apply(RequestOptions.circleCropTransform())
                .into(holder.ivItemSpeakerImage)


        holder.itemView.setOnClickListener{
            speakerListener.onSpeakerClicked(speaker, position)
        }
    }

    fun updateData(data: List<Speaker>) {
        listSpeakers.clear()
        listSpeakers.addAll(data)
        notifyDataSetChanged()
    }

    override fun getItemCount() = listSpeakers.size

}

