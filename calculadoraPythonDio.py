# Solicita entrada dos usuários
number_1 = float(input('Digite o primeiro número: '))
number_2 = float(input('Digite o segundo número: '))

# Menu de operações
print("\nEscolha a operação:")
print("1. Soma")
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")

choice = input("Digite o número da operação desejada: ")

# Realiza a operação selecionada
if choice == '1':
    result = number_1 + number_2
elif choice == '2':
    result = number_1 - number_2
elif choice == '3':
    result = number_1 * number_2
elif choice == '4':
    result = number_1 / number_2
else:
    print("Opção inválida. Tente novamente.")
    exit()

print(f"Resultado: {result:.2f}")