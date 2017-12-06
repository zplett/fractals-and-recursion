#Zac Plett
#recstr.py
#6 October 2016
#
#I have adhered to the Honor Code on this assignment.

def main():
    s = input("Please enter a string: ")
    t = input("Please enter another string: ")
    
    print(rev(s))
    palindrome(s)
    if sub(s,t) == True:
        print("'",t,"'", "is a subsequence of","'",s,"'")
    else:
        print("'",t,"'", "is not a subsequence of","'",s,"'")
    
#prints the string s backwards
def rev(s):
    if len(s) == 0:
        return s
    else:
        return s[-1] + rev(s[:-1])
    
#determines whether or not a string is a palindrome    
def palindrome(s):
    if len(s) == 0:
        print("The input string s is a palindrome!")
    elif len(s) == 1:
        print("The input string s is a palindrome!")
    else:
        if s[0] == s[-1]:
            return palindrome(s[1:-1])
        else:
            print("The input string s is not a palindrome!")
            
#determines whether or not the string t is a subsequence found in s
def sub(s,t):
    if len(t) == 0:
        return True
    elif len(t) > len(s):
        return False
    elif s[0] == t[0]:
        s = s[1:]
        t = t[1:]
        return sub(s,t)
    else:
        s = s[1:]
        return sub(s,t)
        
main()  