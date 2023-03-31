#Imports libraries
from twilio.rest import Client
from time import sleep

# Your Account SID and Auth Token from twilio.com/console
account_sid = 'your_account_sid'
auth_token = 'your_auth_token'

client = Client(account_sid, auth_token)
#Create the Message from the spoofed number
message = client.messages \
                .create(
                     body="The Message You Want",
                     from_='your_twilio_number',
                     to='recipient_phone_number'
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
print('                                 Please Come Back Soon!                                  ")
