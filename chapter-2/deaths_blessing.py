
def deaths_blessings(monsters, healths, strengths):
    pass


if __name__ == "__main__":
    t = int(input())
    outputs = []
    for i in range(t):
        monsters = int(input())
        healths = [int(i) for i in input().split()]
        strengths = [int(i) for i in input().split()]
        outputs.append(deaths_blessings(monsters, healths, strengths))
    for output in outputs:
        print(output)
