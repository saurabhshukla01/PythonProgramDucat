#115.   How Many Times a Given Letter Occurs in a String Recursively .??

def check(string,ch):
    if not string:
        return 0
    elif string[0] == ch:
        return 1 + check(string[1:], ch)
    else:
        return check(string[1:], ch)
string = input("Enter string:")
ch = input("Enter character to check:")
print("Count is:",check(string, ch))