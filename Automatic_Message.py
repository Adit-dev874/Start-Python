import pywhatkit as pwk

# Define the recipient's phone number (with country code) and the message
phone_number = "+919960173149"
message = "Hello this message is automated by Aditya using python!"

# Send message instantly
pwk.sendwhatmsg_instantly(phone_number, message)
