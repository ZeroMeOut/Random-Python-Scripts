# Given 2 int values, return True if one is negative and one is positive
# Expect it the parameter "negative" is True, then return True only if both are negative.

def pos_neg(a, b, negative):
    if not negative:
        if ((a < 0) and (b > 0)) or ((a > 0) and (b < 0)):
            return True
        return False

    if negative:
        if (a < 0) and (b < 0):
            return True
    return False


'''
#Approach 2
def pos_neg(a, b, negative):
    if not negative:
        return ((a < 0) and (b > 0)) or ((a > 0) and (b < 0))
    if negative:
        return (a < 0) and (b < 0)
'''
'''
#Approach 3
def pos_neg(a, b, negative):
    if not negative:
        return ((a < 0) and (b > 0)) or ((a > 0) and (b < 0))
    return (a < 0) and (b < 0)
'''

print(pos_neg(-1, -2, False))
