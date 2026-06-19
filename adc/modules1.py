def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

if __name__ == '__main__':
    num = int(input('enter a number: '))
    print('factorial =', factorial(num))
