# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'ACd69fe18314aef47a63d803b7977477df'
auth_token = '455921567a21e3880afbe3111a19c4eb'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Sms Sending Correct",
                     from_='++12017785782',
                     to='+917799396333'
                 )

print(message.sid)
