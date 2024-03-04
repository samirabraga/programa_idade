soma_idades = 0
pessoa_mais_velha = {'nome': '', 'idade': 0}
pessoas_menos_de_20 = 0
pessoas_mais_de_40 = 0
pessoa_mais_nova = {'nome': '', 'idade': float('inf')}
sexos = []

for i in range(5):
    print(f"\nDigite as informações da {i+1}ª pessoa:")
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    sexo = input("Sexo (M/F): ").upper()


    soma_idades += idade


    if idade > pessoa_mais_velha['idade']:
        pessoa_mais_velha['nome'] = nome
        pessoa_mais_velha['idade'] = idade


    if idade < 20:
        pessoas_menos_de_20 += 1


    if idade > 40:
        pessoas_mais_de_40 += 1


    if idade < pessoa_mais_nova['idade']:
        pessoa_mais_nova['nome'] = nome
        pessoa_mais_nova['idade'] = idade
        pessoa_mais_nova['sexo'] = sexo

    sexos.append(sexo)


media_idade = soma_idades / 5

print("\nResultados:")
print(f"Média de idade do grupo: {media_idade:.2f} anos")
print(f"Pessoa mais velha: {pessoa_mais_velha['nome']} (idade: {pessoa_mais_velha['idade']} anos)")
print(f"Pessoas com menos de 20 anos: {pessoas_menos_de_20}")
print(f"Pessoas com mais de 40 anos: {pessoas_mais_de_40}")
print(f"Sexo da pessoa mais nova: {pessoa_mais_nova['sexo']}")
