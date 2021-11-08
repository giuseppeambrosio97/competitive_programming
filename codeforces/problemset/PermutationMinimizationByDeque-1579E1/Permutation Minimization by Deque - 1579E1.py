import sys
input = sys.stdin.readline


def inp():
    """
    For taking integer inputs

    :return: int
    """
    return(int(input()))


def inlt():
    """
    For taking List inputs

    :return: List
    """
    return(list(map(int, input().split())))


def solve(n, perm):
    deque = []
    deque.append(perm[0])
    del perm[0]
    for i in perm:
        if i < deque[0]:
            deque.insert(0, i)
        else:
            deque.append(i)
    return deque


def main():
    number_of_test = inp()
    for _ in range(number_of_test):
        n = inp()
        perm = inlt()
        #print(solve(n, perm))
        sys.stdout.write(" ".join(map(str, solve(n, perm))) + "\n")


main()

# print(solve(1, [3, 1, 2, 4]))
