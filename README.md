# TikTok-Launcher

A simple Android app designed to be the default handler for links to the TikTok.com domain.  Upon receiving a URL intent from another app it will send a broadcast intent of "tiktok.LAUNCH" with the URL in the intent's data field.  This intent can be received by anything you want to further process the data.  The original use case was to use Tasker to receive the intent, which triggers a workflow to launch the URL via TikTok in a work/managed profile.  This allowed for isolation of TikTok from the primary system while still allowing for TikTok URLs to open in the native app.
