## main.py

import pywhatkit as pwk

try:
    # Send message instantly
    phone_number = input("Whats the targets phone number? (include country code eg. +49)")
    msg_text("Enter the messages text")
    pwk.sendwhatmsg_instantly(phone_number, msg_text)
    print("Message sent successfully.")
except Exception as e:
    print(f"An error occurred: {e}")
