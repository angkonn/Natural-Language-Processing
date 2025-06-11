import re
string = "Tiger is the national animal of India. Tiger is a wild animal."
pattern = "Tiger"
result = re.match(pattern,string).group(0)
print(result)