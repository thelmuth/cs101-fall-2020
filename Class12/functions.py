
def average(num1, num2):
    """Average of 2 numbers."""
    result = (num1 + num2) / 2
    return result


# x = average(10, 15)
# # like I said: num1 = 10
# #              num2 = 15
# y = x * x
# 
# print(y)

def longer(string1, string2):
    """Returns the longer of two strings.
    If they're the same length, return string2"""
    if len(string1) > len(string2):
        return string1
    else:
        return string2
    print("This will never print")

    
z = longer("computer science", "biology")
print(z)
w = longer("hi", "hello")
print(w)
    
    
    
    