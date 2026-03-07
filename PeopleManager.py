import json
import os

pasta = os.path.dirname(__file__)
caminho_arquivo = os.path.join(pasta, "pessoas.json")

pessoas = []
try:
    with open(caminho_arquivo, "r") as arquivo:
        pessoas = json.load(arquivo)
except (FileNotFoundError, json.JSONDecodeError):
    pessoas = []


# sistema para cadastrar pessoas, ver relatório e buscar por nome
while True:
    print("\n1 - Cadastrar pessoa")
    print("2 - Ver relatório")
    print("3 - Buscar pessoa por nome")
    print("4 - Sair")
    print("5 - Área do administrador")
    print()

# Opção para cadastrar uma pessoa
    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        nome = input("digite seu nome: ")
        while True:
            try:
                idade = int(input("digite sua idade: "))
                if idade <= 0:
                    print("Idade inválida. Por favor, digite uma idade válida.")
                else:
                    break
            except ValueError:
                print("Entrada inválida. Por favor, digite um número para a idade.")

        profissao = input("digite sua profissão: ")
        print(f"Pessoa cadastrada: {nome}, {idade} anos, {profissao}")
        pessoas.append({"nome": nome, "idade": idade, "profissao": profissao})

        with open(caminho_arquivo, "w") as arquivo:
            json.dump(pessoas, arquivo, indent=4)
        print("Pessoa cadastrada com sucesso!")

# Opção para ver o relatório de pessoas cadastradas
    elif opcao == "2":
        print("Relatório de pessoas cadastradas:")
        for pessoa in pessoas:
            print(
                f"- {pessoa['nome']}, {pessoa['idade']} anos, {pessoa['profissao']}")
        if len(pessoas) == 0:
            print("Nenhuma pessoa cadastrada.")
        else:
            print(f"Total de pessoas cadastradas: {len(pessoas)}")

# Cálculo da idade média, pessoa mais velha e mais nova
        soma = 0
        for pessoa in pessoas:
            soma += pessoa["idade"]
        media = soma / len(pessoas) if len(pessoas) > 0 else 0
        print(f"Idade média das pessoas cadastradas: {media:.2f} anos")
        if len(pessoas) > 0:
            maisvelha = pessoas[0]
            maisnova = pessoas[0]
            for pessoa in pessoas:
                if pessoa["idade"] > maisvelha["idade"]:
                    maisvelha = pessoa
                if pessoa["idade"] < maisnova["idade"]:
                    maisnova = pessoa
            print(
                f"Pessoa mais velha: {maisvelha['nome']} ({maisvelha['idade']} anos)")
            print(
                f"Pessoa mais nova: {maisnova['nome']} ({maisnova['idade']} anos)")

# Opção para buscar uma pessoa por nome
    elif opcao == "3":
        nome_busca = input("Digite o nome da pessoa que deseja buscar: ")
        encontrada = False
        for pessoa in pessoas:
            if pessoa["nome"].lower() == nome_busca.lower():
                print(
                    f"Pessoa encontrada: {pessoa['nome']}, {pessoa['idade']} anos, {pessoa['profissao']}")
                encontrada = True
                break
        if not encontrada:
            print("Pessoa não encontrada.")

# area do administrador
    elif opcao == "5":
        senha = input("Digite a senha de administrador: ")
        if senha == "admin123":
            print("Acesso concedido. Bem-vindo, administrador!")
            while True:
                print("\n--- MODO ADMINISTRADOR ---\n")
                print("1 - Excluir pessoa: ")
                print("2 - ver situação de trabalhos")
                print("3 - Editar pessoa: ")
                print("4 - Voltar para o menu principal: ")
                opcao_admin = input("Escolha uma opção: ")

                # excluir pessoa
                if opcao_admin == "1":
                    for i, pessoa in enumerate(pessoas):
                        print(
                            f"{i + 1} - {pessoa['nome']}, {pessoa['idade']} anos, {pessoa['profissao']}")
                    try:
                        indice = int(
                            input("Digite o número da pessoa que deseja excluir (ou 0 para cancelar): "))

                        if indice == 0:
                            print("Operação cancelada.")

                        elif 1 <= indice <= len(pessoas):
                            pessoa_excluida = pessoas.pop(indice - 1)

                            with open(caminho_arquivo, "w") as arquivo:
                                json.dump(pessoas, arquivo, indent=4)
                            print(
                                f"Pessoa excluída: {pessoa_excluida['nome']}")
                        else:
                            print("Número inválido. Por favor, tente novamente.")
                    except ValueError:
                        print("Indice inválido. Por favor, digite um número válido.")

                # opção de ver situação de trabalhos
                elif opcao_admin == "2":
                    print("\n--- Pessoas empregadas ---")
                    for pessoa in pessoas:
                        if pessoa["profissao"].lower() != "desempregado" and pessoa["profissao"].lower() != "estudante":
                            print(
                                f"- {pessoa['nome']}, {pessoa['idade']} anos, {pessoa['profissao']}")

                    print("\n--- Pessoas desempregadas ou estudantes ---")
                    for pessoa in pessoas:
                        if pessoa["profissao"].lower() == "desempregado" or pessoa["profissao"].lower() == "estudante":
                            print(
                                f"- {pessoa['nome']}, {pessoa['idade']} anos, {pessoa['profissao']}")

                    if len(pessoas) == 0:
                        print("Nenhuma pessoa cadastrada.")
                    else:
                        print(f"Total de pessoas cadastradas: {len(pessoas)}")

                # opção para editar pessoa
                elif opcao_admin == "3":
                    for i, pessoa in enumerate(pessoas):
                        print(
                            f"{i + 1} - {pessoa['nome']}, {pessoa['idade']} anos, {pessoa['profissao']}")
                    try:
                        indice = int(
                            input("Digite o número da pessoa que deseja editar (ou 0 para cancelar): "))

                        if indice == 0:
                            print("Operação cancelada.")

                        elif 1 <= indice <= len(pessoas):
                            pessoa_editada = pessoas[indice - 1]
                            novo_nome = input(
                                f"Digite o novo nome para {pessoa_editada['nome']} (ou pressione Enter para manter o nome atual): ")
                            nova_idade = input(
                                f"Digite a nova idade para {pessoa_editada['nome']} (ou pressione Enter para manter a idade atual): ")
                            nova_profissao = input(
                                f"Digite a nova profissão para {pessoa_editada['nome']} (ou pressione Enter para manter a profissão atual): ")

                            if novo_nome:
                                pessoa_editada['nome'] = novo_nome
                            if nova_idade:
                                try:
                                    pessoa_editada['idade'] = int(nova_idade)
                                except ValueError:
                                    print(
                                        "Idade inválida. Mantendo a idade atual.")
                            if nova_profissao:
                                pessoa_editada['profissao'] = nova_profissao

                            with open(caminho_arquivo, "w") as arquivo:
                                json.dump(pessoas, arquivo, indent=4)
                            print(
                                f"Pessoa editada: {pessoa_editada['nome']}")
                        else:
                            print("Número inválido. Por favor, tente novamente.")
                    except ValueError:
                        print("Indice inválido. Por favor, digite um número válido.")

                # Opção para voltar para o menu principal
                elif opcao_admin == "4":
                    print("Voltando para o menu principal...")
                    break
                else:
                    print("Opção inválida. Por favor, escolha uma opção válida.")
        else:
            print("Senha incorreta. Acesso negado.")

    # Opção para sair do programa
    elif opcao == "4":
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
