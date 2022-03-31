arquivo = open('dados/contatos-escrita.csv', encoding='latin_1')
print(type(arquivo.buffer))
arquivo.close()

arquivo = open('dados/contatos-escrita.csv', encoding='latin_1', mode='w')
print(type(arquivo.buffer))
arquivo.close()

arquivo = open('dados/contatos-escrita.csv', encoding='latin_1', mode='a')
print(type(arquivo.buffer))
arquivo.close()

arquivo = open('dados/contatos-escrita.csv', encoding='latin_1', mode='a+')
print(type(arquivo.buffer))
arquivo.close()