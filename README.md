# TikTok-Launcher

A simple Android app designed to be the default handler for links to the TikTok.com domain.  Upon receiving a URL intent from another app it will send a broadcast intent of "tiktok.LAUNCH" with the URL in the intent's data field.  This intent can be received by anything you want to further process the data.  The original use case was to use Tasker to receive the intent, which triggers a workflow to launch the URL via TikTok in a work/managed profile.  This allowed for isolation of TikTok from the primary system while still allowing for TikTok URLs to open in the native app.

## Setup
1. Install APK to device.
2. Go into app settings for `TikTok Launcher` app and set it as the default handler for TikTok URLs.
3. Install `Termux`, `Tasker`, and `Termux-Tasker` plugin.
4. In Termux, install `python3` and install `zeroconf` module via pip.
5. In Termux, install `adb` via `pkg` command.
6. Copy `adb_port.sh` and `launch_tiktok.py` to the home directory in Termux.
7. Import 3 Tasker profile files (`*.prf.xml`) into Tasker.
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
1. When the work profile is enabled or disabled, a global variable called `%MANAGED_PROFILE_AVAILABLE` is updated via the profiles `Work Profile Enabled` and `Work Profile Disabled` (two profiles are necessary as there is a different intent sent for enabled vs disabled, and Tasker only supports 1 intent received event per-profile).  This is used by the TikTok launching task to determine whether or not the work profile should be started and waited for.  If the profile is already enabled the enabling step will be skipped, decreasing time to launch TikTok.
2. When a TikTok URL is clicked, the TikTok Launcher app will open (as it is the default handler for `*.tiktok.com` URLs).  Upon opening, this app will take the URL it receives and send it as the data in a new broadcast intent sent to `tiktok.LAUNCH`.
3. A profile created within Tasker (`TikTok Intent Received`) is set to listen for broadcasts to `tiktok.LAUNCH`.  Upon receiving this intent, the `TikTok` task is started, which runs the following steps:
   * Check whether or not Wifi is connected
     1. If is is not, send an intent of `android.intent.action.VIEW` to a specific package (should be set to your default browser) with the TikTok URL as the data.  This will open your default browser to the TikTok URL.  Then exit.  This is a fallback step for when Wifi is not connected, as the necessary ADB commands for launching work profile apps will not work without Wifi.
   * If Wifi is connected:
      1. Enable `ADB Wireless`.
      2. If the URL sent in the intent matches `*.tiktok.com*`, proceed.  If not, exit.
      3. If the work profile is enabled (according to the `%MANAGED_PROFILE_AVAILABLE` global variable), proceed.  If not, then turn on the work profile via a built-in Tasker action and then proceed.
      4. Run a command in Termux of `/data/data/com.termux/files/home/adb_port.sh %data`, with the `%data` argument being the TikTok URL received by the intent.
      5. `adb_port.sh` starts, checking for the presence of a file `adb_port.txt` containing the port number of the ADB Wireless port to connect to.  If this file doesn't exist a dummy file is created with the value `12345`.  The value of that file is then stored in the `$PORT` variable.
      6. `adb connect localhost:$PORT` is run to attempt to determine if the device's ADB server is accessible.
      7. If ADB is accessible, the `am` command is run via ADB for the specified work profile ID (default is 10) with the TikTok URL as the argument.  This launches the default handler for TikTok URLs within the work profile, which should be the real TikTok app.  Then ADB disconnects and the script exits.
      8. If ADB is not accessible, the command `/data/data/com.termux/files/home/launch_tiktok.py $1` is run (with the `$1` argument being the TikTok URL).
      9. The `launch_tiktok.py` command launches, using the `zeroconf` Python module to determine the port number of the `"_adb-tls-connect._tcp.local.` service (the ADB wireless port).  Then `adb connect` is run to connect to localhost on the discovered port.  After that, the port number is written to `adb_port.txt` for future use.
      10. Finally, `am start` is run via ADB (like described in step 7), which launches the default handler for the TikTok URL in the work profile (which should be the official TikTok app).
     
