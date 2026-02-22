from classes import Produto, Almoxarifado

def executar_sistema():
    # 1. Instancia o almoxarifado
    meu_estoque = Almoxarifado()

    # 2. Cria e cadastra os produtos iniciais
    itens = [
        Produto("A01", "Caneta Azul", "Escritório", 50),
        Produto("B05", "Sacola Plástica G", "Embalagens", 200),
        Produto("U02", "Uniforme Tam G", "Uniformes", 15),
        Produto("E10", "Papel A4", "Escritório", 20)
    ]

    for item in itens:
        meu_estoque.cadastrar_produto(item)

    # 3. Simulação de movimentações
    print("\n--- Processando Movimentações ---")
    meu_estoque.registrar_entrada("A01", 20)  # Chegaram canetas
    meu_estoque.registrar_saida("U02", 5)     # Saíram uniformes
    meu_estoque.registrar_saida("B05", 250)   # Tentativa de saída maior que estoque

    # 4. Exibe o resultado final
    meu_estoque.relatorio_estoque()

if __name__ == "__main__":
    executar_sistema()