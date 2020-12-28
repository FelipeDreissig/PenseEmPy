# 1. Em uma instrução print, o que acontece se você omitir um dos parênteses ou ambos?
"""O que se pretendia realizar não ocorre. Isto é, nada é 'pintado' e se for um IDE tipo paycharm, apresentará erro no código."""

# 2 Se estiver tentando imprimir uma string, o que acontece se omitir uma das aspas ou ambas?
"""Neste caso, a omissão das duas aspas o IDE entendera que isso é um objeto. Como ele não existe porque nao é um objeto 
ele dirá que isso não está definido. Isto é, a variável nao existe. E não existe mesmo, não é variável.
A omissão de uma aspas é erro de sintaxa, o IDE apresentará erro.
"""
# 3 Você pode usar um sinal de menos para fazer um número negativo como -2.
# O que  acontece se puser um sinal de mais antes de um número? E se escrever assim: 2++2?
"""Você estará apenas dizendo que o número é positivo com uma quantidade de caracteres maior que o necessário."""

# exemplos
x = -2
k = 2++2
l = +2

#4. Na notação matemática, zeros à esquerda são aceitáveis, como em 02. O que
#acontece se você tentar usar isso no Python?
"""Ele simplicicará para 2."""

#5. O que acontece se você tiver dois valores sem nenhum operador entre eles?
"""Erro de sintaxe."""
