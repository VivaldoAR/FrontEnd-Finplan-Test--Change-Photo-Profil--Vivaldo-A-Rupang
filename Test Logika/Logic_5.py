def main():
    size = get_inp()

    print_pattern(size)


def get_inp():
    while True:
        s = int(input("Input: "))
        if s % 2 == 0:
            print("Input Harus Ganjil") 
        elif s % 2 != 0:
            return s


def print_pattern(s):
    for i in range(s):
        for j in range(s):
            if i == 0 or i == s - 1 or j == s - i - 1:
                print("X", end="")
            elif j == 0 or j == s - 1:
                print("X", end="")
            else:
                print("O", end="")
        print("")


main()