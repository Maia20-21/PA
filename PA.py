print('PROGRESSÃO ARITMÉTICA: 10 TERMOS INICIAIS E TERMOS ADICIONAIS\n')

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))


decimo = primeiro + (10 - 1) * razao                                     # Calcula o décimo termo da PA
termo_atual = primeiro
termos = 1

while termo_atual <= decimo:                                             # Exibe os primeiros 10 termos da PA
    print(f'{termo_atual}', end = ' → ')
    termo_atual += razao
print('PAUSA')

while termos != 0:                                                        # Permite ao usuário adicionar mais termos à PA
    termos = int(input('\nQuantos termos você quer mostrar a mais: '))
    if termos == 0:
        break

    termo_final = termo_atual + (termos - 1) * razao                       # Calcula e exibe os termos adicionais
    while termo_atual <= termo_final:
        print(f'{termo_atual}', end = ' → ')
        termo_atual += razao
    print('PAUSA')
print('FIM')
