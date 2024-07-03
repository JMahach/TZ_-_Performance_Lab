import sys


def pathfinder(n, m):
    array = list(range(1, n + 1))
    result = []
    start_current_index = 0

    while True:
        result.append(array[start_current_index])
        last_current_index = (start_current_index + m - 1) % n

        if array[last_current_index] == 1:
            break

        start_current_index = last_current_index
    return result


if __name__ == "__main__":
    n, m = map(int, (sys.argv[1], sys.argv[2]))
    print("".join(map(str, pathfinder(n, m))))
