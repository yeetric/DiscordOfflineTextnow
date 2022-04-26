import pytextnow
# my sid cookie
#  s%3ACPyraqk8YbdKDhLNjMThwSwPSVtpdEsb.TGedwHmjcZ82uFARzF5fiXhJ6ohDMWWOVw0Uq27JXgI
# my csrf cookie
# s%3AIUtsySojIO94oiFnIho3Ee0n.OJJ%2F5y4fnrF3vxvVVh9y8Toz57NGPbcMd7iKNTXgIaw
#  my username
# yeetricstorage
client = pytextnow.Client("yeetricstorage", sid_cookie="s%3ACPyraqk8YbdKDhLNjMThwSwPSVtpdEsb.TGedwHmjcZ82uFARzF5fiXhJ6ohDMWWOVw0Uq27JXgI", csrf_cookie="s%3AIUtsySojIO94oiFnIho3Ee0n.OJJ%2F5y4fnrF3vxvVVh9y8Toz57NGPbcMd7iKNTXgIaw")
while True:
    new_messages = client.get_unread_messages()

    for message in new_messages:
        message.mark_as_read()
        print(message)
        print(message.number)
        print(message.content)
#     add update thing
#    add shut down program thing
