try:
    print("1.", int('123е'))
except Exception as err:
    print("1.", type(err).__name__ + ":", err)
try:
    print("2.", int('91.4'))
except Exception as err:
    print("2.", type(err).__name__ + ":", err)

try:
    print("3.", int(524.345 ** 435345345311145345))
except Exception as err:
    print("3.", type(err).__name__ + ":", err)

try:
    print("4.", int('7.1 + 4'))
except Exception as err:
    print("4.", type(err).__name__ + ":", err)

try:
    print("5.", int('4' - 2))
except Exception as err:
    print("5.", type(err).__name__ + ":", err)

try:
    print("6.", int('4 - 2'))
except Exception as err:
    print("6.", type(err).__name__ + ":", err)

try:
    print("7.", int('42'))
except Exception as err:
    print("7.", type(err).__name__ + ":", err)

try:
    print("8.", int(-12.12))
except Exception as err:
    print("8.", type(err).__name__ + ":", err)