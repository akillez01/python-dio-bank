class SistemaBancario:
    def __init__(self):
        self.saldo = 0.0
        self.extrato = []
        self.saques_realizados = 0
        self.LIMITE_SAQUES = 3
        self.LIMITE_POR_SAQUE = 500.00

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato.append(f"Depósito: R$ {valor:.2f}")
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("Operação falhou! O valor informado é inválido.")

    def sacar(self, valor):
        excedeu_saques = self.saques_realizados >= self.LIMITE_SAQUES
        excedeu_limite = valor > self.LIMITE_POR_SAQUE
        sem_saldo = valor > self.saldo

        if excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")
        elif excedeu_limite:
            print(f"Operação falhou! O valor do saque excede o limite de R$ {self.LIMITE_POR_SAQUE:.2f}.")
        elif sem_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        elif valor > 0:
            self.saldo -= valor
            self.saques_realizados += 1
            self.extrato.append(f"Saque:    R$ {valor:.2f}")
            print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("Operação falhou! O valor informado é inválido.")

    def ver_extrato(self):
        print("\n================ EXTRATO ================")
        if not self.extrato:
            print("Não foram realizadas movimentações.")
        else:
            for movimento in self.extrato:
                print(movimento)
        print(f"\nSaldo atual: R$ {self.saldo:.2f}")
        print("=========================================")

def main():
    sistema = SistemaBancario()
    
    while True:
        print("\n=============== MENU ===============")
        print("[1] Depositar")
        print("[2] Sacar")
        print("[3] Extrato")
        print("[4] Sair")
        print("=================================")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            try:
                valor = float(input("Informe o valor do depósito: "))
                sistema.depositar(valor)
            except ValueError:
                print("Valor inválido. Por favor, digite um número.")
        elif opcao == "2":
            try:
                valor = float(input("Informe o valor do saque: "))
                sistema.sacar(valor)
            except ValueError:
                print("Valor inválido. Por favor, digite um número.")
        elif opcao == "3":
            sistema.ver_extrato()
        elif opcao == "4":
            print("Obrigado por usar nosso sistema bancário!")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção de 1 a 4.")

if __name__ == "__main__":
    main()