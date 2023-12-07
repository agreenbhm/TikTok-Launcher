package com.agreenbhm.tiktoklauncher

import android.content.Intent
import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Surface
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.tooling.preview.Preview
import com.agreenbhm.tiktoklauncher.ui.theme.TikTokLauncherTheme

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        Intent().also { intent ->
            intent.setAction("tiktok.LAUNCH")
            intent.putExtra("data", this.intent.data)
            sendBroadcast(intent)
        }
        finish()
    }
}