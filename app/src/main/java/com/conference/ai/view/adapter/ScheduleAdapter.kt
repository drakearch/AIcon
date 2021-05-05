package com.conference.ai.view.adapter

import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.TextView
import androidx.recyclerview.widget.RecyclerView
import com.conference.ai.R
import com.conference.ai.model.Conference
import java.text.SimpleDateFormat
import java.util.*
import kotlin.collections.ArrayList

class ScheduleAdapter(val scheduleListener: ScheduleListener) : RecyclerView.Adapter<ScheduleAdapter.ViewHolder>() {

    var listConferences = ArrayList<Conference>()

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int) = ViewHolder(LayoutInflater.from(parent.context).inflate(
        R.layout.item_schedule, parent, false))

    override fun onBindViewHolder(holder: ScheduleAdapter.ViewHolder, position: Int) {
        val conference = listConferences[position] as Conference
        holder.tvItemScheduleTitle.text = conference.title
        holder.tvItemScheduleSpeaker.text = conference.speaker
        holder.tvItemScheduleTopic.text = conference.topic

        val simpleDateFormat = SimpleDateFormat("HH:mm")
        val simpleDateFormatAMPM = SimpleDateFormat("a")
        val cal = Calendar.getInstance()
        cal.time = conference.datetime
        holder.tvItemScheduleHour.text = simpleDateFormat.format(conference.datetime)
        holder.tvItemScheduleAMPM.text = simpleDateFormatAMPM.format(conference.datetime).toUpperCase()



        holder.itemView.setOnClickListener{
            scheduleListener.onConferenceClicked(conference, position)
        }

    }

    override fun getItemCount() = listConferences.size

    fun updateData(data: List<Conference>) {
        listConferences.clear()
        listConferences.addAll(data)
        notifyDataSetChanged()
    }

    class ViewHolder(itemView: View) : RecyclerView.ViewHolder(itemView) {
        val tvItemScheduleTitle = itemView.findViewById<TextView>(R.id.tvItemScheduleTitle)
        val tvItemScheduleSpeaker = itemView.findViewById<TextView>(R.id.tvItemScheduleSpeaker)
        val tvItemScheduleTopic = itemView.findViewById<TextView>(R.id.tvItemScheduleTopic)
        val tvItemScheduleHour = itemView.findViewById<TextView>(R.id.tvItemScheduleHour)
        val tvItemScheduleAMPM = itemView.findViewById<TextView>(R.id.tvItemScheduleAMPM)
    }

}