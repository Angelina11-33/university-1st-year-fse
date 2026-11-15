N = int(input("Введите число от 1 до 9: "))

if 1 <= N <= 9:
    print(r"    _~_    " * N)
    print(r"   (o o)   " * N)
    print(r"  /  V  \  " * N)
    print(r" /(  _  )\ " * N)
    print(r"   ^^ ^^   " * N)
else:
    print("Ошибка, введите число от 1 до 9")
