from conta import Conta
conta1 = conta("Guilherme", 1643, "1759-7")
conta1.extrato()
conta1.deposito(1000)
conta1.saque(200)
conta1.saque(1500)
conta1.extrato()
conta2 = Conta("Guilherme", 1234, "7070-0")
conta2.extrato()
conta1.transferir(300, conta2)
conta1.extrato()
conta2.extrato()
conta2.titular = "Guilherme"
print(f"Olá, {conta2.titular}! :)")
