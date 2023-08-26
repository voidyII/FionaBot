def handle_all(message):
    msg_low = message.lower()

    # simple response to hello
    if msg_low == "hello":
        return 'Haiiii <3'

    # preparation for help command
    if msg_low == "help":
            return 'Are you trying to get help without using commands??! Stop that, BAKA!!!'
        