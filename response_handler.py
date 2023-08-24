from dotenv import load_dotenv
import os

# checks if prefix is present and if it is correct one
# def prefix_check(message):
#     load_dotenv()
#     PREFIX = os.getenv('PREFIX')

#     message_prefix = message[0]

#     if message_prefix == PREFIX:
#         return True
#     else: 
#         return False

def handle_all(message):
    # if prefix_check(message) == True:
        message = message[1:]
        msg_low = message.lower()

        #simple response to hello
        if msg_low == "hello":
            return 'Haiiii <3'

        # preparation for help command
        if msg_low == "help":
            return 'At the moment I unfortunately cant run commands yet :C'
        