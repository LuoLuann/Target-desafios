'''
4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:

	SP - R$67.836,43
	RJ - R$36.678,66
	MG - R$29.229,88
	ES - R$27.165,48
	Outros - R$19.849,53

Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve 
dentro do valor total mensal da distribuidora.
'''

dados = {
    "SP":  "R$67.836,43",
    "RJ": "R$36.678,66",
	"MG": "R$29.229,88",
	"ES": "R$27.165,48",
	"Outros": "R$19.849,53"
}
def converter_valores(dados):
    valores = []
    for k, v in dados.items():
        # replace  value: the comma with dot
        v = v.replace(".", "").replace(",", ".")

        # remove non-digit and non-dot characters
        v = "".join(filter(lambda c: c.isdigit() or c == ".", v))

        # convert to float and append to list
        valores.append({k: float(v)})
    return valores

def soma(valores):
    soma = 0
    for i, v in enumerate(valores):
        for value in v.values():
            soma = soma + value
    return soma
    
def percentual(dados):
    valores = converter_valores(dados)
    soma_total = soma(valores)
    lista_percentuais = []
    for i, v in enumerate(valores):
        for value in v.values():
            lista_percentuais.append((value * 100)/soma_total)
    
    return lista_percentuais
           
x = percentual(dados)
valores = converter_valores(dados)
print("Porcentagem de cada estado em relação ao rendimento total da distribuidora")
for k, x in zip(dados.keys(), x):
    print(f"{k}: faturou {x:.2f}% do total", end="\n")
