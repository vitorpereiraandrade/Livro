convidados = ['Vitor', 'Magaly', 'Vinicius']
print(convidados)
print(f'Gostaria de convidar o Sr {convidados[0]} para jantar')
print(f'Gostaria de convidar a Sra {convidados[1]} para jantar')
print(f'Gostaria de convidar o Sr {convidados[2]} para jantar')
print('')

saiu = convidados.pop()
print(f'O Convidado {saiu} nao podera comparecer ao jantar')
print('')

convidados.append('Zion')
print(convidados)
print(f'Gostaria de convidar o Sr {convidados[0]} para jantar')
print(f'Gostaria de convidar a Sra {convidados[1]} para jantar')
print(f'Gostaria de convidar o Sr {convidados[2]} para jantar')
print('')

print('Senhores convidados achei uma mesa com mais 3 lugares')
convidados.insert(0, 'Zucky')
convidados.insert(2,'Bruno')
convidados.append('Bel')
print(convidados)
print(f'Gostaria de convidar o Sr {convidados[0]} para jantar')
print(f'Gostaria de convidar a Sr {convidados[1]} para jantar')
print(f'Gostaria de convidar o Sr {convidados[2]} para jantar')
print(f'Gostaria de convidar o Sra {convidados[3]} para jantar')
print(f'Gostaria de convidar o Sr {convidados[4]} para jantar')
print(f'Gostaria de convidar o Sra {convidados[5]} para jantar')
print('')

print('Infelizmente a mesa foi cancelada, estamos só com 2 lugares')
print(convidados)
saiu1 = convidados.pop()
print(f'Sinto muito {saiu1} por nao poder convidar para o jantar')
saiu2 = convidados.pop()
print(f'Sinto muito {saiu2} por nao poder convidar para o jantar')
saiu3 = convidados.pop()
print(f'Sinto muito {saiu3} por nao poder convidar para o jantar')
saiu4 = convidados.pop()
print(f'Sinto muito {saiu4} por nao poder convidar para o jantar')
print(convidados)
print('')

print(f'Senhor {convidados[0]} continua convidado para o jantar')
print(f'Senhor {convidados[1]} continua convidado para o jantar')
print(convidados)
print('')

del convidados[0]
print(convidados)
del convidados[0]
print(convidados)


