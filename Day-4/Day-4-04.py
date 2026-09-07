a=int(input("Enter a number: "))
b=int(input("Enter b number: "))
for i in range(1, 1000):
    if i % a == 0 and i % b == 0:
        print(i)
        break