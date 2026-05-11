from conta import conta
conta1 = conta("Guilherme", 1643, "1759-7")
conta1.extrato()
conta1.deposito(1000)
conta1.saque(200)
conta1.saque(1500)
conta1.extrato()
conta1.transferir(Conta2, 300)
