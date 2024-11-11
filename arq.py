# Superclasse para Instrumentos
class Instrumento:
    def __init__(self, marca, modelo, preco, num_cordas):
        self.marca = marca
        self.modelo = modelo
        self.preco = preco
        self.num_cordas = num_cordas

class Baixo(Instrumento):
    def __init__(self, marca, modelo, preco, num_cordas, tipo_captador):
        super().__init__(marca, modelo, preco, num_cordas)
        self.tipo_captador = tipo_captador

class Guitarra(Instrumento):
    def __init__(self, marca, modelo, preco, num_cordas, tipo_ponte):
        super().__init__(marca, modelo, preco, num_cordas)
        self.tipo_ponte = tipo_ponte

class Violao(Instrumento):
    def __init__(self, marca, modelo, preco, num_cordas, tipo_corpo):
        super().__init__(marca, modelo, preco, num_cordas)
        self.tipo_corpo = tipo_corpo

class Funcionario:
    def __init__(self, nome, cpf, salario, cargo):
        self.nome = nome
        self.cpf = cpf
        self.salario = salario
        self.cargo = cargo
        self.loja = None  # Inicia sem loja

    def alocar_loja(self, loja):
        self.loja = loja

class Loja:
    def __init__(self, localizacao, loja_mais_proxima=None):
        self.localizacao = localizacao
        self.funcionarios = []  # Agregação: lista de funcionários
        self.estoque = []        # Composição: lista de instrumentos
        self.loja_mais_proxima = loja_mais_proxima

    def adicionar_funcionario(self, funcionario):
        funcionario.alocar_loja(self)
        self.funcionarios.append(funcionario)

    def remover_funcionario(self):
        if self.funcionarios:
            funcionario = self.funcionarios.pop()
            funcionario.alocar_loja(None)

    def adicionar_instrumento(self, instrumento):
        self.estoque.append(instrumento)

    def remover_instrumento(self):
        if self.estoque:
            self.estoque.pop()

    def contar_instrumentos(self):
        return {
            'guitarras': len([i for i in self.estoque if isinstance(i, Guitarra)]),
            'baixos': len([i for i in self.estoque if isinstance(i, Baixo)]),
            'violoes': len([i for i in self.estoque if isinstance(i, Violao)])
        }

    def contar_funcionarios_por_cargo(self):
        cargos = {}
        for funcionario in self.funcionarios:
            cargos[funcionario.cargo] = cargos.get(funcionario.cargo, 0) + 1
        return cargos

# Driver code para testar funcionalidades
if __name__ == "__main__":
    # Criação de lojas
    loja_rio = Loja("Rio de Janeiro")
    loja_sp = Loja("São Paulo", loja_mais_proxima=loja_rio)

    # Criação de funcionários
    funcionario1 = Funcionario("Carlos Souza", "123.456.789-00", 3000, "Gerente")
    funcionario2 = Funcionario("Ana Lima", "987.654.321-00", 2000, "Vendedor")

    # Adicionar funcionários a uma loja
    loja_rio.adicionar_funcionario(funcionario1)
    loja_rio.adicionar_funcionario(funcionario2)

    # Criação de instrumentos
    guitarra1 = Guitarra("Fender", "Stratocaster", 8000, 6, "Tremolo")
    baixo1 = Baixo("Ibanez", "SR500", 4500, 4, "Ativo")
    violao1 = Violao("Yamaha", "C40", 1000, 6, "Clássico")

    # Adicionar instrumentos ao estoque da loja
    loja_rio.adicionar_instrumento(guitarra1)
    loja_rio.adicionar_instrumento(baixo1)
    loja_rio.adicionar_instrumento(violao1)

    # Contar instrumentos e funcionários
    print("Estoque de instrumentos por tipo:", loja_rio.contar_instrumentos())
    print("Funcionários por cargo:", loja_rio.contar_funcionarios_por_cargo())
    
    # Remover funcionários e instrumentos
    loja_rio.remover_funcionario()
    loja_rio.remover_instrumento()

    # Contar novamente após remoção
    print("Estoque de instrumentos após remoção:", loja_rio.contar_instrumentos())
    print("Funcionários por cargo após remoção:", loja_rio.contar_funcionarios_por_cargo())
