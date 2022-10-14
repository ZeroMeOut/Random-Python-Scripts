# Given a string, return a new string where "not" has been added to the font
# However, if the string already begins with "not", return the string unchanged
"""
def not_string(str):
    if not str[0:3] == 'not':
        return "not " + str
    return str


print(not_string('hello'))
"""


def not_string(str):
    if len(str) >= 3 and str[0:3] == 'not':
        return str
    return "not " + str


print(not_string('hello'))
