"""
Escopo de funções em Pythoon
Escopo significa o local onde aquele código pode atingir.
Existe o escopo global e local.
O escopo global é o escopo onde todo o código é alcançavel.
O escopo local é o esocopo onde apenas nomes do mesmo local
podem ser alcançados.
"""

x = 1

def escopo():
    x = 25
    x = 20

    
    def outra_funcao():
        y = 2
        x = 11
        print(x, y)
    
    outra_funcao()
    print(x)
   
print(x)
escopo()
print(x) 