arquivo_contatos = open('dados/contatos-write.csv', encoding='latin_1', mode='w+')

contatos = ['11,Carol,carol@carol.com.br\n',
            '12,Ana,ana@ana.com.br\n',
            '13,Tais,tais@tais.com.br\n',
            '14,Felipe,felipe@felipe.com.br\n']

for contato in contatos:
    arquivo_contatos.write(contato)

arquivo_contatos.seek(29)
arquivo_contatos.write('12,Ana,ana@ana.com.br\n'.upper())

input("foo")
