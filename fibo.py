def fibo(n):
    a,b=map(int,input("Enter first two element of fibonnaci series:").split())
    print("fibonacci series upto ", n,"Numbers is: ")
    for _ in range(n):
        print(a,end=" ")
        a,b=b,b+a