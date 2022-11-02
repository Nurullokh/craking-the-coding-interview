
def weird_dev(n, b):
    count = 0
    if n > 9:
        for i in range(1, 10):
            if i % b == 0:
                count += 1
    else:
        for i in range(1, n):
            if i % b == 0:
                count += 1
        return count
    for i in range(10, n+1):
        n_s = str(i)
        s = ""
        for k in n_s:
            s += str(int(k) // b)
        if int(s) == i / b:
            count += 1
    return count
        



if __name__ == "__main__":
    t = int(input())
    out = []
    for i in range(t):
        n, b = [int(i) for i in input().split()]
        out.append(weird_dev(n, b))
    for o in out:
        print(o)