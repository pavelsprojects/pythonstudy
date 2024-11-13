def max_or_minus(b, c):
    a = int(input("Введите число a: "))
    if a > 0:
        maximus = max(a, b, c)
        return maximus
    else:
        return -1
result = max_or_minus(2, 22) #здесь менять b и c
print(result)