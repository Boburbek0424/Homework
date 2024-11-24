def find_factors():
    num=int(input("Enter a positive integer: "))
    for i in range(1,num+1):
        if num%i==0:
            print(f"{i} is the factor of {num}")
find_factors()