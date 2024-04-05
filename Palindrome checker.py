def p(s):
    s=s.lower().replace(" ","")
    return s==s[::-1]
    
s=input("enter string to check palindrome:")
if p(s):
    print("'{}' is the palindrome".format(s))
else:
    print("not a palindrome ")









