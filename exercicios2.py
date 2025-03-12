class Contato:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone

    def exibir_info(self):
        print(f"Nome: {self.nome}, Telefone: {self.telefone}")

contatos = []

contato1 = Contato("João", "11111111")
contato2 = Contato("Maria", "22222222")
contato3 = Contato("Pedro", "33333333")

contatos.append(contato1)
contatos.append(contato2)
contatos.append(contato3)

for contato in contatos:
    contato.exibir_info()