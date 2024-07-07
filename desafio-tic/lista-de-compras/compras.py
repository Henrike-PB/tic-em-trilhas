class ListaDeCompras:
    def __init__(self):
        self.produtos = []
        self.id_counter = 1

    def exibir_cabecalho(self):
        print("=== Lista de Compras Simples ===")

    def exibir_menu(self):
        print("\nMenu de Opções:")
        print("1. Adicionar produto")
        print("2. Remover produto")
        print("3. Pesquisar produtos")
        print("4. Sair do programa")

    def adicionar_produto(self):
        nome = input("Nome do produto: ")
        unidade = input("Unidade de medida (Quilograma/Grama/Litro/Mililitro/Unidade/Metro/Centímetro): ")
        quantidade = float(input("Quantidade: "))
        descricao = input("Descrição: ")

        produto = {
            "id": self.id_counter,
            "nome": nome,
            "unidade": unidade,
            "quantidade": quantidade,
            "descricao": descricao
        }
        self.produtos.append(produto)
        self.id_counter += 1
        print(f"Produto '{nome}' adicionado com sucesso!")

    def remover_produto(self):
        id_produto = int(input("Digite o ID do produto a ser removido: "))
        produto_removido = None

        for produto in self.produtos:
            if produto["id"] == id_produto:
                produto_removido = produto
                break

        if produto_removido:
            self.produtos.remove(produto_removido)
            print(f"Produto '{produto_removido['nome']}' removido com sucesso!")
        else:
            print("Produto não encontrado.")

    def pesquisar_produtos(self):
        termo_pesquisa = input("Digite o nome ou parte do nome do produto: ")
        resultados = [produto for produto in self.produtos if termo_pesquisa.lower() in produto["nome"].lower()]

        if resultados:
            print(f"Resultados para '{termo_pesquisa}':")
            for produto in resultados:
                print(f"ID {produto['id']}: {produto['nome']} ({produto['quantidade']} {produto['unidade']})")
            print(f"Total de produtos encontrados: {len(resultados)}")
        else:
            print("Nenhum produto encontrado.")

    def listar_produtos(self):
        if self.produtos:
            print("\nProdutos na lista:")
            for produto in self.produtos:
                print(f"ID {produto['id']}: {produto['nome']} ({produto['quantidade']} {produto['unidade']})")
        else:
            print("Nenhum produto na lista.")

    def executar(self):
        self.exibir_cabecalho()
        while True:
            self.exibir_menu()
            opcao = input("Selecione uma opção: ")

            if opcao == "1":
                self.adicionar_produto()
            elif opcao == "2":
                self.remover_produto()
            elif opcao == "3":
                self.pesquisar_produtos()
            elif opcao == "4":
                print("Obrigado por utilizar a Lista de Compras!")
                break
            else:
                print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    lista = ListaDeCompras()
    lista.executar()
