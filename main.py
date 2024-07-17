import json

lista_produtos = []
def menu_principal():
    print("(1) Mostra produtos do Estoque: ")
    print("(2) Incluir produtos no Estoque: ")
    print("(3) Remover produtos do Estoque: ")
    print("(4) Editar produtos do Estoque: ")
    print("(0) Sair")
    return int(input("Digite uma das opções acima: "))

''' Mostra Produtos do Estoque '''
def mostrar_produtos(lista_produtos, arquivo_produto):
    lista_produtos = ler_arquivo(arquivo_produto)
    if len(lista_produtos) == 0:
        print("Nenhum produto foi encontrado")
    else:
        for produto in lista_produtos:
            print(produto)

''' Incluir produtos no Estoque '''
def incluir_produto(arquivo_produto):
    codigo = int(input("Digite o código do produto: "))
    nome = input("Digite o nome do produto: ")
    quantidade = int(input("Digite o quantidade do produto: "))
    novo_produto = {
        "Código": codigo,
        "Nome": nome,
        "Quantidade": quantidade
    }
    lista_produtos = ler_arquivo(arquivo_produto)
    lista_produtos.append(novo_produto)
    salvar_produtos(lista_produtos, arquivo_produto)

''' Remover produtos no Estoque '''
def remover_produto(codigo, arquivo_produto):
    produto_para_remover = None
    lista_produtos = ler_arquivo(arquivo_produto)
    for produto in lista_produtos:
        if produto["Código"] == codigo:
            produto_para_remover = produto
            break
    if produto_para_remover is not None:
        lista_produtos.remove(produto_para_remover)
        salvar_produtos(lista_produtos, arquivo_produto)
    else:
        print("Código não encontrado")

''' Editar produtos no Estoque '''
def editar_produto(codigo, arquivo_produto):
    lista_produtos = ler_arquivo(arquivo_produto)
    for produto in lista_produtos:
        if produto["Código"] == codigo:
            produto["Nome"] = input("Digite um novo nome do produto: ")
            produto["Quantidade"] = input("Digite a quantidade do produto: ")
            salvar_produtos(lista_produtos, arquivo_produto)
            return
    print("Código não encontrado")

def salvar_produtos(lista_produtos, arquivo_produto):
    with open(arquivo_produto, "w", encoding='utf-8') as arquivo_produto:
        json.dump(lista_produtos, arquivo_produto, ensure_ascii=False)

def ler_arquivo(arquivo_produto):
    try:
        with open(arquivo_produto, "r", encoding='utf-8') as arquivo_produto:
            lista_produtos = json.load(arquivo_produto)
            return lista_produtos
    except:
        return []


arquivo_produto = "produtos.json"

while True:
    opcao = menu_principal()
    if opcao == 1:
        print(f"Você escolheu a opção {opcao}")
        while True:
            mostrar_produtos(lista_produtos, arquivo_produto)
            break

    elif opcao == 2:
        print(f"Você escolheu a opção {opcao}")
        incluir_produto(arquivo_produto)

    elif opcao == 3:
        print(f"Você escolheu a opção {opcao}")
        codigo = int(input("Digite o código do produto para remover: "))
        remover_produto(codigo, arquivo_produto)

    elif opcao == 4:
        print(f"Você escolheu a opção {opcao}")
        codigo = int(input("Digite o código do produto para editar: "))
        editar_produto(codigo, arquivo_produto)

    elif opcao == 0:
        print("Encerrando programa...")
        break
    else:
        print("Você digitou uma opção inválida")


