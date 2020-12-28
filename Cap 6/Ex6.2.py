# exercício 6.2


def ack(m, n):
    if m == 0:
        n = n + 1
        return n
    elif n == 0:
        return ack((m - 1), 1)
    return ack(m - 1, ack(m, n - 1))


print(ack(2, 5))

# acontece que o py chega no máximo da recursividade.
