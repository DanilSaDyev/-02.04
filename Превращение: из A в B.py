def transform_number(a, b):
    if a > b:
        print("It is impossible to transform number a to number b")
        return
    
    while a != b:
        if b % 2 == 0 and b > a:
            b //= 2
        elif str(b)[-1] == '1' and b > a:
            b = int(str(b)[:-1])
        else:
            print("It is impossible to transform number a to number b")
            return
    
    print("Number b can be obtained from number a")

# Пример использования:
a = 3
b = 45
transform_number(a, b)
