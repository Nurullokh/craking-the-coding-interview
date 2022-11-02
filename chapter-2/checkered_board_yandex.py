
def checkered_board(n, k):
    if (n * n) % k != 0 or n > k:
        return "No"
    out = []
    ls = list(range(1, k + 1))
    if n == k:
        for i in range(n):
            out.append(ls[i:] + ls[:i])
    elif n * n == k:
        temp = list(range(1, k + 1))
        start = 0
        end = n
        for i in range(n):
            out.append(temp[start:end])
            start = end
            end += n
    elif n < k:
        diff = int(k / n)
        start = 0
        end = n
        for i in range(diff):
            out.append(list(range(start+1, end+1)))
            start = end
            end += n
        out = out * int(((n * n) / k))
    else:
        diff = int(n / k)
        for i in range(n):
            out.append((ls[i:] + ls[:i]) * diff)
    return out
        
        


if __name__ == "__main__":
    n, k = [int(i) for i in input().split()]
    result = checkered_board(n, k)
    if result == "No":
        print("No")
    else:
        print("Yes")
        for row in result:
            # temp = [str(row[i]) for i in row]
            # temp = " ".join(temp)
            # print(temp)
            print(row)