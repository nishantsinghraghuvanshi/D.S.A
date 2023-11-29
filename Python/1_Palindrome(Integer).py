def ispalindrome(a):
    b = str(a)
    c = b[::-1]
    if(c == b):
        return True
    else:
        False
Number = int(input("Enter a number : "))
print(ispalindrome(Number))