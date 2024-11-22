for i in range(3):
    n = input()
    if n.isdigit():
        result = int(n) + (3 - i)
        if result % 3 == 0 and result % 5 == 0:
            print("FizzBuzz")
        elif result % 3 == 0:
            print("Fizz")
        elif result % 5 == 0:
            print("Buzz")
        else:
            print(result)
        break