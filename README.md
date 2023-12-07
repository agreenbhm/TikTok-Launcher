# TikTok-Launcher

A simple Android app designed to be the default handler for links to the TikTok.com domain.  Upon receiving a URL intent from another app it will send a broadcast intent of "tiktok.LAUNCH" with the URL in the intent's data field.  This intent can be received by anything you want to further process the data.  The original use case was to use Tasker to receive the intent, which triggers a workflow to launch the URL via TikTok in a work/managed profile.  This allowed for isolation of TikTok from the primary system while still allowing for TikTok URLs to open in the native app.

## Setup
1. Install APK to device.
2. Go into app settings for `TikTok Launcher` app and set it as the default handler for TikTok URLs.
3. Install `Termux`, `Tasker`, and `Termux-Tasker` plugin.
4. In Termux, install `python3` and install `zeroconf` module via pip.
5. In Termux, install `adb` via `pkg` command.
6. Copy `adb_port.sh` and `launch_tiktok.py` to the home directory in Termux.
7. Import 4 Tasker profile files (`*.prf.xml`) into Tasker.  You don't need to import `TikTok.tsk.xml`.
8. Verify/change specified browser package within Tasker task to point to browser of choice (Samsung Internet is the one currently selected).
9. (If managed/work profile doesn't already exist) Install `Island` (https://play.google.com/store/apps/details?id=com.oasisfeng.island&hl=en&gl=US&pli=1).
    * If profile already exists determine profile ID number and update `launch_tiktok.py`, on the line that mentions `--user 10`.  Change 10 to whatever the profile ID number is.
10. Enable ADB wireless via Developer Tools.
11. Pair Termux ADB with ADB wireless using the pairing code option.
12. Disable timeout authorization for ADB in Developer Tools, otherwise this will stop working after a week and you'll need to re-pair ADB.
13. Install official `TikTok` app within Island.


Additional permissions are likely to be requested by Tasker when running the profile, so test it out a few times to make sure that all permissions are granted.  You'll need to use ADB to grant certain permissions.  You'll also need to grant Takser permission to access Termux, which is in the Android permissions settings page for Tasker.

## Usage
When everything is set up properly, you should be able to click a TikTok link anywhere within your primary Android profile and have it open in your Island/managed/work profile.

## How it works
TBD
