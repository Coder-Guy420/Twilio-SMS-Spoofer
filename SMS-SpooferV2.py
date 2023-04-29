# Imports libraries
from twilio.rest import Client
from time import sleep

# Get user input for account_sid and auth_token
account_sid = input("Enter your Twilio Account SID: ")
auth_token = input("Enter your Twilio Auth Token: ")

# Create Twilio client object
client = Client(account_sid, auth_token)

# Get user input for message body, from number and to number
body = input("Enter the message you want to send: ")
from_number = input("Enter the number you want to spoof: ")
to_number = input("Enter the recipient's phone number: ")

# Send message from the spoofed number
message = client.messages.create(
    body=body,
    from_=from_number,
    to=to_number
)

print("███████╗███╗   ███╗███████╗    ███████╗██████╗  ██████╗  ██████╗ ███████╗███████╗██████╗ ")
print("██╔════╝████╗ ████║██╔════╝    ██╔════╝██╔══██╗██╔═══██╗██╔═══██╗██╔════╝██╔════╝██╔══██╗")
print("███████╗██╔████╔██║███████╗    ███████╗██████╔╝██║   ██║██║   ██║█████╗  █████╗  ██████╔╝")
print("╚════██║██║╚██╔╝██║╚════██║    ╚════██║██╔═══╝ ██║   ██║██║   ██║██╔══╝  ██╔══╝  ██╔══██╗")
print("███████║██║ ╚═╝ ██║███████║    ███████║██║     ╚██████╔╝╚██████╔╝██║     ███████╗██║  ██║")
print("╚══════╝╚═╝     ╚═╝╚══════╝    ╚══════╝╚═╝      ╚═════╝  ╚═════╝ ╚═╝     ╚══════╝╚═╝  ╚═╝")
print("                                                                by: SyfonSec             ")
print(" ")
print(" ")
print("                                 Sending Message...")
print(message.sid)
print("                                 Message Sent                                            ")
print(" ")
print(" ")
print("                                 Thanks for Using SMS-Spoofer                            ")
print("                                 Please Come Back Soon!                                  ")
