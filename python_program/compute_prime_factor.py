#26. Compute Prime Factors of an Integer ..??

n= int(input("enter the no of terms:"))
for i in range(2,n+1):
    for j in range(2,i):
        if (i%j==0):
            break
    else:
        print(i)
