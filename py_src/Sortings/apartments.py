def main():
    n, m, k = map(int, input().split())

    a = sorted(list(map(int, input().split())))
    b = sorted(list(map(int, input().split())))

    count, i, j = (
        0,
        0,
        0,
    )

    while i < n and j < m:
        if abs(a[i] - b[j]) <= k:
            count += 1
            j += 1
            i += 1
        elif a[i] < b[j]:
            i += 1
        else:
            j += 1

    print(count)


if __name__ == '__main__':
    main()
