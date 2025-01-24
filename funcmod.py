def reverse(n):
    rev=0
    while n>0:
        d=n%10
        rev=rev*10+d
        n=n//10
    return rev
def palin(n):
    rev=reverse(n)
    if rev==n:
        print(n,"is a palindrome")
    else:
        print(n,"is not a palindrome")
palin(131)