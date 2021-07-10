(lambda g: [None for g["regex_integer_in_range"],g["regex_alternating_repetitive_digit_pair"] in [(r"^[1-9][0-9]{5}$",r"(\d)(?=.\1)")]])(globals())

#Boilerplate code, can't remove
import re
P = input()

print (bool(re.match(regex_integer_in_range, P)) 
and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)