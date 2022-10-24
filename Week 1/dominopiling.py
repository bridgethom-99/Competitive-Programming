def solve(m, n):
    rectangularBoard = m * n
    domino = 2 * 1
    return rectangularBoard / domino
    # Integers only entered
if __name__ == "__main__":
    m, n = map(int, input().split(" "))
    print(solve(m, n))
