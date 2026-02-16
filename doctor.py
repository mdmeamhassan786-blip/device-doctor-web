# doctor.py
# Offline + Online hybrid Device Doctor

PROBLEMS_DB = {
    "bootloop": "Try to flash the device using official firmware. Make sure battery is at least 50%.",
    "won't turn on": "Charge the battery for 30 mins and then press power button for 10 secs.",
    "screen frozen": "Perform a soft reset. Hold power button for 10-15 seconds.",
    "battery draining fast": "Check background apps and reduce screen brightness.",
    "overheating": "Turn off device, remove case, keep in ventilated area.",
    "slow charging": "Use original charger and cable, avoid using while charging.",
    "wifi not connecting": "Forget network and reconnect. Restart router and device.",
    "bluetooth not working": "Turn off and on Bluetooth. Restart device.",
    "app crashing": "Update app, clear cache, or reinstall.",
    "touchscreen unresponsive": "Restart device. If persists, calibrate or check hardware.",
    "firmware verification failed": "Check if the firmware matches your device model. Use correct NB0/GDS files.",
    "slow internet": "Restart your router. Check cables. If WiFi, try changing channel.",
    "no internet": "Check ISP, reconnect cables, restart modem/router.",
    "wifi keeps dropping": "Change WiFi channel, update firmware, keep router ventilated.",
    "cannot login router": "Reset router to default settings, use correct credentials.",
    "router overheating": "Keep router ventilated, reduce continuous usage.",
    "blue screen": "Restart Windows, update drivers, check hardware connections.",
    "slow pc": "Check background programs, disk space, run antivirus.",
    "cannot boot": "Check power supply, remove external devices, run recovery.",
    "printer not printing": "Check printer connection, paper, ink, and restart printer.",
    "software installation failed": "Check compatibility, free disk space, and admin rights.",
    "laptop overheating": "Clean vents, use cooling pad, reduce heavy tasks.",
    "battery not charging": "Check charger, power socket, battery health.",
    "screen flickering": "Update graphics driver, check display cable.",
    "keyboard not working": "Check keyboard driver, try external keyboard.",
    "touchpad not working": "Enable touchpad from settings, update driver.",
    "camera not turning on": "Charge battery, check memory card, reset camera.",
    "device not pairing": "Restart both devices, remove old connections.",
    "signal lost": "Check antenna, obstacles, interference, reposition device.",
    "device overheating": "Turn off device, remove case, let it cool down.",
    "app not installing": "Clear storage, download latest version, restart device.",
    "cannot update firmware": "Check model compatibility and battery level.",
    "network authentication failed": "Re-enter credentials, check network settings.",
    "storage full": "Delete unnecessary files or expand storage.",
    "camera not saving photos": "Check SD card, storage settings, reset device.",
    "wifi password incorrect": "Verify password, reconnect network.",
    "vpn not connecting": "Check VPN server, credentials, network connection.",
    "screen cracked": "Replace screen at authorized service center.",
    "microphone not working": "Check privacy settings, test with another app.",
    "speaker not working": "Check volume, headphone jack, restart device.",
    "device restarting randomly": "Update firmware, check for malware, battery health.",
    "usb not detected": "Try another cable, port, or reinstall drivers.",
    "device lagging": "Clear cache, restart, uninstall heavy apps.",
    "software crashing": "Update software, reinstall, check dependencies."
}

ONLINE_HINTS = {
    "bootloop": "You can try online guide at example.com/bootloop-fix",
    "slow internet": "Try online speed test or check your ISP website for outage info",
    "screen frozen": "Search online for model-specific soft reset steps",
    "wifi not connecting": "Search online router troubleshooting for your model"
}

def diagnose(user_input):
    user_input = user_input.lower()
    for key in PROBLEMS_DB:
        if key in user_input:
            return f"⚡ Offline Solution:\n{PROBLEMS_DB[key]}"
    for key in ONLINE_HINTS:
        if key in user_input:
            return f"🌐 Online Suggestion:\n{ONLINE_HINTS[key]}"
    return "❌ No solution found. Try rephrasing the problem."
