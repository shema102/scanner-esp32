# This file is executed on every boot (including wake-boot from deepsleep)
# import esp
# esp.osdebug(None)

# import json
# import webrepl
# import network

# # Reading settings from file
# with open("config.json") as f:
#     config = json.load(f)
# ssid = config["ssid"]
# password = config["password"]

# # Connecting to wifi
# wlan = network.WLAN(network.STA_IF)
# wlan.active(True)
# wlan.connect(ssid, password)

# webrepl.start()
