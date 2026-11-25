
def dynamicArray(n, queries):
    arr = [[] for _ in range(n)]

    lastAnswer = 0
    answers = []

    for query in queries:
        q_type, x, y = query

        idx = (x ^ lastAnswer) % n

        if q_type == 1:
            arr[idx].append(y)

        elif q_type == 2:
            lastAnswer = arr[idx][y % len(arr[idx])]
            answers.append(lastAnswer)

    return answers


if __name__ == '__main__':
    first_multiple_input = input().split()

    n = int(first_multiple_input[0])
    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().split())))

    result = dynamicArray(n, queries)

    print('\n'.join(map(str, result)))
