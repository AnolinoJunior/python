#Operadores lógicos
# and (e) or (ou) not (não)
# and - todas as condições precisam ser
# verdadeiras.
#Se qualquer valor for considerado falso,
#a expressão inteira será avaliada naquele valor
#São considerados falsy (que você já viu)
# 0.0.0 '' False
#Também existe o tipo None que é 
#usado para representar um não valor

entrada = input('[E]ntrar [S]air:')
senha_digitada = input('Senha: ')
senha_permitida = '123456'

#if só é executada quando a condição for TRUE

if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
    print('Entrar na programacao')
else:
    print('Sair') 

#Avaliação de curto circuito
#print(True and True and True)
#senha = input('senha: ') or 'Sem senha'
#print(senha)
