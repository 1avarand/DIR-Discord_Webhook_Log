# send_discord_message.py
import requests

webhook_url = "https://discord.com/api/webhooks/1372810457705877555/_ifX8dcwnVdPBJmL4eTpl9xVgrpWcWTiErKLPBRQMh6PYV8M0kD5Xc3IgIfpQWN8VrhC"
message = {"content": "discord.gg/holy"}

response = requests.post(webhook_url, json=message)

if response.status_code == 204:
    print("Message sent successfully.")
else:
    print(f"Failed to send message. Status code: {response.status_code}")
