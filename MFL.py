"""
MFL — Anonymous Message Sender (using Textbelt free quota – REAL but VERY limited)

Reality in March 2026:
• Textbelt free tier:        1 message / day  per IP   (resets ~24h)
• Delivery:                  USA / Canada → quite good
                             Many other countries → partial / fails often
• Sender ID:                 usually shows as email gateway or "TXTBE" / random
                             Almost never allows custom sender name like "MFL"
• No registration needed for the free key = 'textbelt'
• If you want more messages → paid key (~$1–2 for 100–200 msgs)

This script uses the REAL public endpoint: https://textbelt.com/text
"""

import requests
import time
import sys
import os
import random

def magnificent_hi():
    lines = [
        "███╗   ███╗███████╗██╗      ",
        "████╗ ████║██╔════╝██║      ",
        "██╔████╔██║█████╗  ██║      ",
        "██║╚██╔╝██║██╔══╝  ██║      ",
        "██║ ╚═╝ ██║███████╗███████╗ ",
        "╚═╝     ╚═╝╚══════╝╚══════╝ ",
        "",
        "MFL  –  A N O N Y M O U S   M E S S A G E",
        "     (Textbelt free – 1 msg/day – real delivery attempt)"
    ]

    colors = ['\033[95m', '\033[94m', '\033[96m', '\033[92m', '\033[93m', '\033[91m']
    for line in lines:
        print(random.choice(colors) + line.center(60) + '\033[0m')
        time.sleep(0.06)

    print("\n" + "═" * 70 + "\n")


def send_via_textbelt(phone: str, message: str) -> bool:
    url = "https://textbelt.com/text"
    payload = {
        "phone": phone,           # must be E.164 format, e.g. +12025550123
        "message": message,
        "key": "textbelt"         # this is the FREE key – limited to ~1/day/IP
    }

    try:
        r = requests.post(url, data=payload, timeout=15)
        resp = r.json()

        if resp.get("success"):
            print("\n" + " " * 15 + "【 MESSAGE QUEUED – delivery attempted 】")
            print(f"Text ID: {resp.get('textId', 'unknown')}")
            print("Check status later at: https://textbelt.com/status/<textId>")
            return True
        else:
            print("\nFailed → " + resp.get("message", "Unknown error"))
            if "quota" in str(resp).lower():
                print("→ You already used your 1 free message today from this IP.")
            elif "invalid" in str(resp).lower():
                print("→ Phone number format looks invalid.")
            return False

    except Exception as e:
        print(f"\nNetwork / service error: {e}")
        return False


def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    magnificent_hi()

    print("  !! REAL MESSAGE ATTEMPT – but VERY limited !!")
    print("  • Using Textbelt free tier → max 1 msg per ~24 hours per IP")
    print("  • Works best to USA / Canada — international delivery spotty")
    print("  • Sender usually NOT 'MFL' — gateways rarely allow custom sender\n")

    while True:
        cc = input("Country code with + (example: +1 +44 +91 +61) → ").strip()
        if not cc.startswith("+") or not cc[1:].isdigit():
            print("Must start with + followed by digits\n")
            continue
        if len(cc) < 2 or len(cc) > 5:
            print("Country codes are usually 1–4 digits\n")
            continue
        break

    while True:
        num = input("Phone number WITHOUT country code → ").strip()
        if not num.isdigit():
            print("Only digits please\n")
            continue
        if len(num) < 6 or len(num) > 14:
            print("Most numbers are 7–14 digits long\n")
            continue

        full = cc + num
        print(f"→ Full number: {full}")
        if input("Correct? (y/n) → ").lower() != 'y':
            continue
        break

    msg = input("\nMessage (160 chars recommended):\n→ ").strip()
    if not msg:
        print("No empty messages.\n")
        sys.exit(1)

    print("\n" + "═" * 70)
    print(f"  From    : (gateway / random – NOT custom 'MFL')")
    print(f"  To      : {full}")
    print(f"  Message : {msg}")
    print("═" * 70 + "\n")

    print("Contacting Textbelt ... ", end="", flush=True)
    for _ in range(6):
        time.sleep(0.35)
        print(".", end="", flush=True)
    print()

    success = send_via_textbelt(full, msg)

    if success:
        print("\nDone. You have likely used your daily free quota.")
        print("Next message probably possible in 24 hours (depends on IP).")
    else:
        print("\nMessage was NOT sent successfully.")

    print("\nWant to try again anyway? (maybe different IP / VPN)")
    if input("(y/n) → ").lower() == 'y':
        print("\n" + "─"*70 + "\n")
        main()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nInterrupted. Bye.")
    except Exception as e:
        print(f"\nUnexpected error → {e}")
