nome = 'vitor'
print(f'Ola {nome}, você gostaria de aprender Python ')
print(f'Ola {nome.upper()}') # Letra maiuscula
print(f'Ola {nome.lower()}') # Letra minuscula
print(f'Ola {nome.title()}')
print('Albert Einstein certa vez disse: "Uma pessoa que nunca cometeu um erro jamais tentou algo novo"')
pessoa_famosa = 'Albert Einstein'
messagem = 'Uma pessoa que nunca cometeu um erro jamais tentou nada novo'
print(f'{pessoa_famosa}: "{messagem}"')
nome2 = '   Magaly         '
print(nome2)
print(f'\t{nome2}')     # da um tab
print(f'\n{nome2}')     # pula uma linha
print(nome2.lstrip())   # elimina espaco em branco a esquerda
print(nome2.rstrip())   # elimina espaco em branco direita
print(nome2.strip())    # elimina todos espaços em branco