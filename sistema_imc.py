usuarios = []

while True:
    print("\nMenu:")
    print("1 - Cadastrar usuário")
    print("2 - Listar usuários")
    print("3 - Analisar IMC dos usuários")
    print("4 - Sair:")

    comando = input("Escolha uma opção: ")

    match comando:
        case "1":
            nome = input("Nome: ")
            email = input("E-mail: ")

            if "@" not in email or "." not in email:
                print("E-mail inválido")
                continue

            idade = int(input("Idade: "))
            peso = float(input("Peso (kg): "))
            altura = float(input("Altura (m): "))

           

            imc = peso / (altura ** 2)

            usuarios.append({
                "nome": nome,
                "email": email,
                "idade": idade,
                "peso": peso,
                "altura": altura,
                "imc": imc
            })

            print(f"{nome} cadastrado com sucesso!")

        case "2":
            if not usuarios:
                print("Nenhum usuário cadastrado")
                continue

            print("\nLista de usuários:")

            for usuario in usuarios:
                print(f"{usuario['nome']} ({usuario['email']}) - Idade: {usuario['idade']}")

        case "3":
            if not usuarios:
                print("Nenhum usuário para analisar")
                continue

            for usuario in usuarios:
                print(f"\nAnálise de {usuario['nome']}:")
                print(f"IMC: {usuario['imc']:.2f}")

                if usuario['imc'] < 18.5:
                    print("Status: Abaixo do peso")
                elif 18.5 <= usuario['imc'] < 25:
                    print("Status: Peso normal")
                elif 25 <= usuario['imc'] < 30:
                    print("Status: Sobrepeso")
                else:
                    print("Status: Obesidade")

            else:
                print("\nTodos os usuários foram analisados")

        case "4":
            print("Encerrando o sistema...")
            break

        case _:
            print("Opção inválida. Tente novamente...")
            pass
