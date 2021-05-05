package com.conference.ai.view.adapter

import com.conference.ai.model.Conference

interface ScheduleListener {
    fun onConferenceClicked(conference: Conference, position: Int)
}