package com.conference.ai.view.adapter

import com.conference.ai.model.Speaker

interface SpeakerListener {
    fun onSpeakerClicked(speaker: Speaker, position: Int)
}