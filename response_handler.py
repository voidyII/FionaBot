def handle_all(message):
    msg_low = message.lower()

    # simple response to hello
    if msg_low == "hello":
        return 'Haiiii <3'

    # funny help response
    if msg_low == "help":
            return 'Are you trying to get help without using commands??! Stop that, BAKA!!!'
        