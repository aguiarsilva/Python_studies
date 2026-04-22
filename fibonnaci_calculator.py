def fibonacci(n: int):
    if n == 0:
        return 0
    if n == 1:
        return 1

    sequence = [0, 1]

    #use dynamic programming to build the rest of the sequence
    for i in range(2, n + 1):
        next_value = sequence[i - 1] + sequence[i - 2]
        sequence.append(next_value)
    
    return sequence[n]
