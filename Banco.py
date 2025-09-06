print (" bem vindo ao banco girabank")
saldo = float (input ("Digite o saldo da sua conta: ")) 

Trasnferencia = float (input ("Digite o valor da transferência: "))

#valide se ela possui sakdo suficiente para transferencia
if saldo >= Trasnferencia:
    print ("saldo suficiente para transferência")
    saldo = saldo - Trasnferencia
    print ("Seu novo saldo é de: ", saldo)
   
else:
    print ("Saldo insuficiente para transferência") 
    print ("Seu saldo é de: ", saldo)
    
