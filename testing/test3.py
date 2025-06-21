import requests


response = requests.get("https://trigger.macrodroid.com/75b4c80d-729e-4b11-9f5c-22646225ef32/disable")

if response.status_code == 200:
    print("🟢 Successfully blocked")
else:
    print("🔴 Failed to block")

print(type(response.text))