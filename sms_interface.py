from twilio.rest import Client
def send_update_text(text):
    # Find these values at https://twilio.com/user/account
    account_sid = "--"
    auth_token = "--"

    client = Client(account_sid, auth_token)

    client.messages.create(
        to="+19707697884",
        from_="+19708251178",
        body=text
    )
