import random

def d2():
    roll_var = random.randint(1, 2)
    if(roll_var == 1):
        roll_var = "Tails"
    else: roll_var = "Heads"
    return roll_var

def d4():
    roll_var = random.randint(1, 4)    
    return roll_var

def d6():
    roll_var = random.randint(1, 6)    
    return roll_var

def d8():
    roll_var = random.randint(1, 8)    
    return roll_var

def d10():
    roll_var = random.randint(0, 9)    
    return roll_var

def d12():
    roll_var = random.randint(1, 12)    
    return roll_var

def d20():
    roll_var = random.randint(1, 20)    
    return roll_var

def d100():
    roll_var = random.randint(1, 100)    
    return roll_var