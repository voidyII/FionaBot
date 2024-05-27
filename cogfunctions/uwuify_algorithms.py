import random
import string

def uwuify_string(args):
    #make this work better than whatever this shit is
    args = ' '.join(args)
    rm_love = args.replace("love", "luv")
    rm_you = rm_love.replace("you", "u")
    rm_na = rm_you.replace("na", "nya")
    rm_no = rm_na.replace("no", "nyo")
    rm_r = rm_no.replace("r", "w")
    uwuified_text = rm_r.replace("l", "w")
    return uwuified_text