"""
MFL - Anonymous Message Sender (demo / educational version)
This script DOES NOT actually send real anonymous SMS messages.

Real anonymous international SMS sending (without registration / payment):
- Has been almost completely blocked/killed in 2024–2026 by carriers and regulators
- Remaining services are either very expensive, very unreliable, or scams
- Almost all "free anonymous SMS" websites from 2021–2023 are dead or don't deliver internationally anymore
"""

import time
import random
import sys
import os

def magnificent_hi():
    lines = [
        "███╗   ███╗███████╗██╗      ",
        "████╗ ████║██╔════╝██║      ",
        "██╔████╔██║█████╗  ██║      ",
        "██║╚██╔╝██║██╔══╝  ██║      ",
        "██║ ╚═╝ ██║███████╗███████╗ ",
        "╚═╝     ╚═╝╚══════╝╚══════╝ ",
        "",
        "A N O N Y M O U S   M E S S A G E   T O O L",
        "           (demo – no real messages sent)           "
    ]

    colors = ['\033[95m', '\033[94m', '\033[96m', '\033[92m', '\033[93m', '\033[91m']

    for line in lines:
        color = random.choice(colors)
        print(color + line.center(60) + '\033[0m')
        time.sleep(0.07)

    print("\n" + "═" * 60 + "\n")


def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    magnificent_hi()

    print("  !! IMPORTANT NOTICE !!")
    print("  This is a DEMO / educational script only")
    print("  It does NOT send real SMS messages in 2025/2026\n")

    while True:
        country_code = input("Enter country code (with + sign, example: +44, +91, +1) → ").strip()

        if not country_code.startswith('+'):
            print("→ Country code must start with + sign\n")
            continue
        if len(country_code) < 2 or len(country_code) > 5:
            print("→ Looks suspicious (most country codes are 2–4 digits)\n")
            continue

        try:
            int(country_code[1:])
        except:
            print("→ Invalid number after +\n")
            continue

        break

    while True:
        number = input(f"Enter phone number (without {country_code}) → ").strip()

        full_number = country_code + number

        if not number.isdigit():
            print("→ Phone number should contain only digits\n")
            continue

        if len(number) < 6 or len(number) > 14:
            print("→ Suspicious length — most numbers are 7–14 digits\n")
            continue

        print(f"  → Target number: {full_number}")
        correct = input("Is this correct? (y/n) → ").lower()
        if correct == 'y':
            break

    message = input("\nMessage to send (max 160 characters recommended):\n→ ").strip()

    if len(message) > 160:
        print(f"Warning: message is {len(message)} characters — many gateways will truncate it\n")

    print("\n" + "═" * 60)
    print(f"  From     : MFL")
    print(f"  To       : {full_number}")
    print(f"  Message  : {message}")
    print("═" * 60 + "\n")

    print("Sending message... ", end="", flush=True)

    for _ in range(8):
        time.sleep(0.4)
        print(".", end="", flush=True)

    print("\n\n" + " " * 18 + "【 MESSAGE SENT (in simulation) 】")
    print(" " * 12 + "(no real message was actually delivered)\n")

    again = input("Send another message? (y/n) → ").lower()
    if again == 'y':
        print("\n" + "-"*70 + "\n")
        main()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nGoodbye.\n")
    except Exception as e:
        print(f"\nUnexpected error: {e}\n")
