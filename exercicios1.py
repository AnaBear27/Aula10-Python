class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
    
    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
        else:
            print("Saldo Insuficiente!")

    def consultar_saldo(self):
        print(f"Saldo atual: R$ {self.saldo:.2f}")

conta1 = ContaBancaria("João", 1000)

conta1.consultar_saldo()
conta1.depositar(500)
conta1.sacar(200)
conta1.consultar_saldo()