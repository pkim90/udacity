from twilio.rest import TwilioRestClient

account_sid = "AC23a87c1d34766367fd178184c149d01f"
auth_token = "db4dfa48d2288051314dc4d310112068"
client = TwilioRestClient(account_sid, auth_token)

message = client.sms.messages.create(
    body = "Hi, testing the body",
    to = "+19803392650",
    from_ = "+19803301024")
print (message.sid)





#auth token = db4dfa48d2288051314dc4d310112068
#Account sid = AC23a87c1d34766367fd178184c149d01f

#Twilio number = (980) 330-1024
#My number = 980 339 2650
