print('This is string')
print('This is also a string')
print('I told my friend, "Python is my favorite language !"')
print("The language 'Python' is named after Monty Python, not the snake")
print("One of Python´s strengths is its diverse and supportive community")

print('')
# Letras maiuscula e minuscula

name = 'ada lovelace'
print(name.title())

name2 = 'Ada Lovelace2'
print(name2.upper())
print(name2.lower())
print('')

# Combinando ou concatenando strings

first_name = 'ada'
last_name = 'lovelace'
full_name = first_name + ' ' + last_name
print(full_name)
print('Hello, ' + full_name.title() + '!')
print(f'Hello, {full_name.title()}!')

message = 'Hello, ' + full_name.title() + '!'
print(message)
print('')

# Acrescentando espacos em branco em strings com tabulacoes ou quebras de linha
# Acrescentar tabulacao no texto  \t (pula um tab)
print('Python')
print('\tPython')
print('')

# Quebra de linha
#   \n
print('Languages:\nPython\nC\nJavaScript')
print('Languages:\n\tPython\n\tC\n\tJavaScript')
print('')

# Removendo espacos em branco
# Remover espacos em branco do lado direito usa: rstrip() e do lado esquerdo: lstrip() e Remover dos 2 lados: strip
favorite_language = 'Python '
print(favorite_language)
print(len(favorite_language))
print(len(favorite_language.rstrip()))

#Remover permanente
favorite_language = favorite_language.rstrip()
print(len(favorite_language))
print('')

# Remover lado esquerdo
language = '   Python2  '
print(len(language))
print(len(language.lstrip()))
print(len(language.strip()))






