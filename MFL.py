"""
MFL - Phone Number Info Lookup (using phonenumbers library – public info only)

Reality check (March 2026):
• This uses the OPEN-SOURCE 'phonenumbers' Python library (pip install phonenumbers)
• Gives PUBLIC info like: country, region/city (NOT precise GPS/street – that's impossible legally without carrier access / consent)
• Other details: carrier, timezone, validity, type (mobile/fixed/voip)
• Data comes from offline databases – accurate for most numbers, but not always up-to-date
• For "precise location": Legally/ethically, you CAN'T get real-time GPS from just a number without apps like Find My Device or law enforcement warrants
• If you need more (e.g., owner name) → paid services like Intelius/BeenVerified, but that's not anonymous/free and varies by country laws

Install: pip install phonenumbers
"""

import time
import random
import sys
import os

try:
    import phonenumbers
    from phonenumbers import geocoder, carrier, timezone
except ImportError:
    print("Missing library! Run: pip install phonenumbers")
    sys.exit(1)

def magnificent_hi():
    lines = [
        "███╗   ███╗███████╗██╗      ",
        "████╗ ████║██╔════╝██║      ",
        "██╔████╔██║█████╗  ██║      ",
        "██║╚██╔╝██║██╔══╝  ██║      ",
        "██║ ╚═╝ ██║███████╗███████╗ ",
        "╚═╝     ╚═╝╚══════╝╚══════╝ ",
        "",
        "P H O N E   N U M B E R   I N F O   L O O K U P",
        "          (public data only – no precise tracking)         "
    ]

    colors = ['\033[95m', '\033[94m', '\033[96m', '\033[92m', '\033[93m', '\033[91m']

    for line in lines:
        color = random.choice(colors)
        print(color + line.center(60) + '\033[0m')
        time.sleep(0.07)

    print("\n" + "═" * 60 + "\n")


def get_phone_info(full_number: str) -> dict:
    try:
        parsed = phonenumbers.parse(full_number)
        if not phonenumbers.is_valid_number(parsed):
            return {"error": "Invalid phone number format or unknown prefix."}

        info = {
            "Valid": "Yes",
            "Country": geocoder.country_name_for_number(parsed, "en"),
            "Region/Location": geocoder.description_for_number(parsed, "en") or "Unknown",
            "Carrier": carrier.name_for_number(parsed, "en") or "Unknown",
            "Timezones": ", ".join(timezone.time_zones_for_number(parsed)) or "Unknown",
            "Type": "Mobile" if phonenumbers.number_type(parsed) == phonenumbers.PhoneNumberType.MOBILE else
                    "Fixed Line" if phonenumbers.number_type(parsed) == phonenumbers.PhoneNumberType.FIXED_LINE else
                    "VoIP" if phonenumbers.number_type(parsed) == phonenumbers.PhoneNumberType.VOIP else
                    "Toll-Free" if phonenumbers.number_type(parsed) == phonenumbers.PhoneNumberType.TOLL_FREE else
                    "Unknown"
        }

        return info

    except phonenumbers.NumberParseException as e:
        return {"error": f"Parse error: {e}"}
    except Exception as e:
        return {"error": f"Unexpected error: {e}"}


def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    magnificent_hi()

    print("  !! PUBLIC INFO ONLY !!")
    print("  • Region is city/state level at best – NOT precise address/GPS")
    print("  • Data from open databases – may not be 100% accurate\n")

    while True:
        country_code = input("Enter country code (with + sign, e.g., +1, +44, +91) → ").strip()

        if not country_code.startswith('+'):
            print("→ Must start with +\n")
            continue
        if not country_code[1:].isdigit():
            print("→ Invalid digits after +\n")
            continue
        if len(country_code) < 2 or len(country_code) > 5:
            print("→ Typical country codes are 1-4 digits\n")
            continue
        break

    while True:
        number = input(f"Enter phone number (without {country_code}) → ").strip()

        if not number.isdigit():
            print("→ Only digits please\n")
            continue
        if len(number) < 6 or len(number) > 14:
            print("→ Most numbers are 7-14 digits\n")
            continue

        full_number = country_code + number
        print(f"→ Full number: {full_number}")
        if input("Correct? (y/n) → ").lower() != 'y':
            continue
        break

    print("\n" + "═" * 60)
    print(f"  Looking up: {full_number}")
    print("═" * 60 + "\n")

    print("Fetching info... ", end="", flush=True)
    for _ in range(8):
        time.sleep(0.3)
        print(".", end="", flush=True)
    print()

    info = get_phone_info(full_number)

    if "error" in info:
        print(f"\nError: {info['error']}")
    else:
        print("\n" + " " * 15 + "【 PHONE INFO 】")
        for key, value in info.items():
            print(f"  {key:<12}: {value}")

    print("\nNote: For more details (e.g., owner name), use paid services legally.")
    print("Precise real-time location requires consent/apps – not possible here.")

    again = input("\nLookup another number? (y/n) → ").lower()
    if again == 'y':
        print("\n" + "-"*70 + "\n")
        main()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nGoodbye.")
    except Exception as e:
        print(f"\nUnexpected error: {e}")
