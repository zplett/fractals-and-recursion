#Zac Plett
#recnum.py
#6 September 2016
#
#I affirm that I have adhered to the Honor Code on this assignment.

def main():
    
    n = eval(input("Please enter the first non-negative integer: "))
    k = eval(input("Please enter the second non-negative integer: "))
    
    print(n, "raised to the power of", k, "is:", powers(n,k))
    print("The sum of the first", n, "squares is:", sums(n))
    print(n, "choose", k, "is:", choose(n,k))

#raises integer n to the power k     
def powers(n,k):
    if k <= 0:
        return 1
    else:
        return n*powers(n,k-1)

#finds the sum of the first n perfect squares    
def sums(n):
    if n <= 1:
        return 1
    else:
        return sums((n-1)) + n*n

def choose(n,k):  
    if k > n:
        return 0
    elif k == n or k == 0:
        return 1
    else:
        return choose(n-1,k) + choose(n-1,k-1)

main()