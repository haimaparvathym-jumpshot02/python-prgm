def print_table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

if __name__ == '__main__':
    num = int(input('enter a number: '))
    print_table(num)


