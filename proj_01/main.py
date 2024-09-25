import json

# Abre o arquivo do json
with open("faturamento.json") as aqv_fat:
    fat_diario = json.load(aqv_fat)

# main
val_fat = []  # lista apenas com os valores faturados diariamente
media = 0
dias_faturados = 0
fat_maior_media = []

# inserir cada valor > 0 na lista val_fat
for i in fat_diario:
    if (i['faturamento']) > 0:
        val_fat.append(i['faturamento'])

dias_faturados = len(val_fat)

print(f'O menor valor é: {min(val_fat)}')
print(f'O maior valor é: {max(val_fat)}')

# calculo média
media = sum(val_fat) / dias_faturados

# rep para saber quantos dias o faturamento > media
for i in val_fat:
    if i > media:
        fat_maior_media.append(i)

print(f'Quantidade de dias no mês que o faturamento diário foi maior que a média mensal: {
      len(fat_maior_media)} dias')
