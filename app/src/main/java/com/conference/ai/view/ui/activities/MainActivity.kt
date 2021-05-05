package com.conference.ai.view.ui.activities

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import androidx.navigation.Navigation
import androidx.navigation.ui.NavigationUI
import com.conference.ai.R
import com.conference.ai.model.Conference
import com.conference.ai.model.Speaker
import com.google.firebase.firestore.FirebaseFirestore
import kotlinx.android.synthetic.main.activity_main.*
import org.json.JSONArray
import org.json.JSONObject
import java.util.*

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        setActionBar(findViewById(R.id.tbMainToolbar))
        configNav()
    }

    fun configNav() {
        NavigationUI.setupWithNavController(bnvMenu, Navigation.findNavController(this,R.id.fragmentContent))
    }
}

