'''/*
3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
	• O menor valor de faturamento ocorrido em um dia do mês;
	• O maior valor de faturamento ocorrido em um dia do mês;
	• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

IMPORTANTE:
	a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
	b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;
*/'''

import json

def abrir_json(caminho):
    with open("dados.json", encoding='utf-8') as file:
        data = json.load(file)
    return data
    
def dias_com_menor_valor(arquivo):
    menor = min(arquivo, key=lambda x: x['valor'])
    menores = [i for i in arquivo if i['valor'] == menor['valor']]
    return menores

def dia_com_maior_valor(arquivo):
    maior = max(arquivo, key=lambda x: x["valor"])
    return maior

def media(valores):
    soma = contador = 0
    for valor in valores:
        if(valor != 0):
            soma = soma + valor
            contador+=1

    media_valores = soma / contador 
    return media_valores

def dias_maiores_que_media(arquivo):
    valores = [d['valor'] for d in arquivo]
    m = media(valores)
    valores_maiores_media = []
    for d in arquivo:
        if d['valor'] > m:
            valores_maiores_media.append(d)
    print(f"A média mensal foi de: R${m:.2f}")
    return valores_maiores_media

def menu(arquivo):
    while(True):
        print(f"\n           MENU\n")
        print("     1 - Dia com maior rendimento do mês \n")
        print("     2 - Dia com menor rendimento do mês \n")
        print("     3 - Dias com valores maiores que a média do rendimento mensal \n")
        print("     4 - Sair do programa \n")
        
        x = int(input("     Digite a opção desejada: "))
        print('\n')
        if x == 1:
            maior = dia_com_maior_valor(arquivo)
            print(f'     O dia que mais rendeu foi: {maior["dia"]} rendeu: R${maior["valor"]:.2f}')
                
            
        if x == 2:
            menores = dias_com_menor_valor(arquivo)
            
            for i in menores:
                print(f'     Dia(s): {i["dia"]} rendeu: R${i["valor"]:.2f}')
            
        if x == 3:
            dias = dias_maiores_que_media(arquivo)
            print("\n")
            for i in dias:
                print(f'     Dia(s): {i["dia"]} rendeu: R${i["valor"]:.2f}')
            
        if x == 4:
            break

arquivo = abrir_json("/")
menu(arquivo)

