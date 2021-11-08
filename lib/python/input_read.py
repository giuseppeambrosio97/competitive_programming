import sys
input = sys.stdin.readline

############ ---- Input Functions ---- ############


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


def insr():
    """
    For taking string inputs.

    :return: List of Characters
    """
    s = input()
    return(list(s[:len(s) - 1]))


def invr():
    """
    For taking space separated integer variable inputs

    :return: a map
    """
    return(map(int, input().split()))
