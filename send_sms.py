
import twilio.rest
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = 'AC17edf098792d89f24d5308f808f59a85'
auth_token = 'badc269eddac42e48151da2882ce19d6'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_='+19856038576',
                     to='+14317266122'
                 )

print(message.sid)
print("done")
