
def number_game(n, arr):
    pass


if __name__ == "__main__":
    t = int(input())
    outputs = []
    for i in range(t):
        n = int(input())
        arr = [int(i) for i in input().split()]
        outputs.append(number_game(n, arr))

    for output in outputs:
        print(output)