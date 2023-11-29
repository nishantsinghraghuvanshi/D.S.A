def ispalindrome(a):
    if (a.lower() == (a[::-1]).lower()):
        return True
    else:
        return False
Word = input("Enter the word : ")
print(ispalindrome(Word))