print('faça teu mano pro fortnite battle royale')

# aqui o sistema pede o nome do usuario
nome= input('me fale teu nome ai')
# aqui o sistema pede a idade
idade= int(input('me fale tua idade ai'))
# aqui o sistema pede o genero do usuario
genero= input('tu é homem ou mulher?')

print(f'bem vindo ao fortnite battle royale {nome}, você tem {idade} anos tendeu, e tu é {genero}')

def menu():
print('como posso te ajudar hoje?')
print('1 - madeira')
print ('2 - tijolo')
print ('3 - metal')

opc_user= int(input('digite o numero da opção do teu material'))
    # aqui começa a lógica
if opc_user == 1:
    print('tome suas madeiras, mas é horrivel pra fight')
elif opc_user == 2:
 print('pegue seus tijolos, assim o lobo mau não vai te pegar')
elif opc_user == 3:
print('receba seus metais, boa papai agora é só full box e 200')
 else:
 print('opção errada! escolha apenas uns dos 3 materiais')
menu()