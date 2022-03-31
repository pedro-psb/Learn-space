contato_carol = '11,Carol,carol@carol.com.br\n'
contato_andreza = '12,Andreza,andreza@andreza.com.br\n'

def using_with():
    with open('dados/contatos-escrita.csv', encoding='latin_1', mode='w') as arquivo:
        arquivo.write(contato_carol)


    with open('dados/contatos-escrita.csv', encoding='latin_1', mode='a') as arquivo:
        arquivo.write(contato_andreza)

def using_normal_open():
    arquivo1 = open('dados/contatos-escrita.csv', encoding='latin_1', mode='w')
    arquivo2 = open('dados/contatos-escrita.csv', encoding='latin_1', mode='a')

    arquivo1.write(contato_carol)
    arquivo2.write(contato_andreza)

    arquivo1.close()
    arquivo2.close()

using_normal_open()
