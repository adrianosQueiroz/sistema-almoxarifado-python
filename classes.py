class Produto:
    def __init__(self, id_produto, nome, categoria, quantidade=0):
        self.id = id_produto
        self.nome = nome
        self.categoria = categoria
        self.quantidade = quantidade

    def __str__(self):
        return f"ID: {self.id: <5} | {self.nome: <20} | Cat: {self.categoria: <15} | Qtd: {self.quantidade}"

class Almoxarifado:
    def __init__(self):
        self.estoque = {}

    def cadastrar_produto(self, produto):
        self.estoque[produto.id] = produto
        print(f"✅ Produto '{produto.nome}' cadastrado!")

    def registrar_entrada(self, id_produto, qtd):
        if id_produto in self.estoque:
            self.estoque[id_produto].quantidade += qtd
            print(f"📥 ENTRADA: +{qtd} un. de {self.estoque[id_produto].nome}.")
        else:
            print("❌ Erro: Produto não cadastrado.")

    def registrar_saida(self, id_produto, qtd):
        if id_produto in self.estoque:
            prod = self.estoque[id_produto]
            if prod.quantidade >= qtd:
                prod.quantidade -= qtd
                print(f"📤 SAÍDA: -{qtd} un. de {prod.nome}.")
            else:
                print(f"⚠️ Alerta: Saldo insuficiente ({prod.nome}: {prod.quantidade}).")
        else:
            print("❌ Erro: Produto não cadastrado.")

    def relatorio_estoque(self):
        print("\n" + "="*65)
        print(f"{'INVENTÁRIO DO ALMOXARIFADO':^65}")
        print("="*65)
        for p in self.estoque.values():
            print(p)
        print("="*65)