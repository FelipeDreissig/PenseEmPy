# exercício 7.2, função aval


def eval_loop():
    while True:
        k = str(input('(DONE para sair)\nDigite algo que possa verificar:'))
        if 'd' == k[0].lower():
            print(eval(j))
            print('Até mais.')
            break
        j = k
        print(eval(k))


eval_loop()
