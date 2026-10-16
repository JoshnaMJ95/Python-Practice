def fibo(n):
    if n<=1:
        return n
    else:
        return (fibo (n-1)+fibo(n-2))
nterms=int(input("Enter the number: "))
print("Fibonacci series: ")
for i in range(nterms):
         print(fibo(i),end = '')
