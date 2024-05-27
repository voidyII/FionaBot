import random
import string

def convert_string(args):
    #learn how to work with tuples man, this is terrible
    args = ''.join(args)
    converted_text = args.replace("l", "w")
    return converted_text