import time
from dhooks import Webhook, Embed

banner = r"""
 _____ _           _        _ _ _     _   _____         _      _____
|   __|_|_____ ___| |___   | | | |___| |_|  |  |___ ___| |_   |   __|___ ___ _____ _____ ___ ___
|__   | |     | . | | -_|  | | | | -_| . |     | . | . | '_|  |__   | . | .'|     |     | -_|  _|
|_____|_|_|_|_|  _|_|___|  |_____|___|___|__|__|___|___|_,_|  |_____|  _|__,|_|_|_|_|_|_|___|_|
              |_|                                                   |_|                         
                               Made by: simo5,9
"""

COLOR_MAP = {
    "red":    0xFF0000,
    "yellow": 0xFFFF00,
    "blue":   0x3498DB,
    "green":  0x2ECC71,
    "white":  0xFFFFFF,
    "black":  0x000000,
}

def send_simple_spam(url, message, delay, count):
    hook = Webhook(url)
    sent = 0
    try:
        while count == 0 or sent < count:
            hook.send(message)
            sent += 1
            print(f"[+] Sent Message #{sent}")
            time.sleep(delay)
    except KeyboardInterrupt:
        print("\n[!] Spam stopped by user.")
    except Exception as e:
        print(f"[!] Error: {e}")

def send_embed_spam(url, title, description, footer, color_name, image_url, delay, count):
    hook = Webhook(url)
    sent = 0
    color = COLOR_MAP.get(color_name.lower(), 0x2F3136)  # Default to Discord dark background

    try:
        while count == 0 or sent < count:
            embed = Embed(
                title=title,
                description=description,
                color=color
            )
            embed.set_footer(text=footer)
            if image_url:
                embed.set_image(image_url)
            hook.send(embed=embed)
            sent += 1
            print(f"[+] Sent Embed #{sent}")
            time.sleep(delay)
    except KeyboardInterrupt:
        print("\n[!] Spam stopped by user.")
    except Exception as e:
        print(f"[!] Error: {e}")

if __name__ == "__main__":
    print(banner)

    webhook_url = input("Enter Discord Webhook URL: ")
    mode = input("Choose message type - [1] Simple Message, [2] Advanced Message(Embed Reply): ").strip()

    delay = float(input("Delay between messages (seconds): "))
    count = int(input("Number of messages to send (0 for infinite): "))

    if mode == "1":
        message = input("Enter message to send: ")
        send_simple_spam(webhook_url, message, delay, count)

    elif mode == "2":
        title = input("Embed Title: ")
        description = input("Embed Description: ")
        footer = input("Embed Footer Text: ")

        print("Available colors: red, yellow, blue, green, white, black")
        color = input("Choose embed color: ").strip().lower()

        image_url = input("Embed Image/GIF URL (leave blank for none): ")
        send_embed_spam(webhook_url, title, description, footer, color, image_url, delay, count)

    else:
        print("[!] Invalid option. Exiting.")
