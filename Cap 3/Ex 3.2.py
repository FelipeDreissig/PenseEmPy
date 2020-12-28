def do_twice(f, k):
    """

    :param f: função objeto
    :param k: argumento
    :return: chamada de função (nula)
    """
    f(k)
    f(k)


def print_twice(a):
    print(a)
    print(a)


def do_four(f, a):
    """
    Está função chamará a (do_twice) duas vezes.
    :param f: a função objeto
    :param a: argumento desta função objetivo
    :return: a própria função objetivo
    """
    do_twice(f, a)
    do_twice(f, a)


do_twice(print, 'spam')
do_four(print, 'spam')
