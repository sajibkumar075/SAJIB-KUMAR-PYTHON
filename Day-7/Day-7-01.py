n = int(input(" "))
x = 0
for i in range(n):
    input_num = input(" ")
    if "++" in input_num:
        x = x + 1
    else:
        x = x - 1

print(x)