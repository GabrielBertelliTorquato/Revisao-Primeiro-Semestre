'''Exemplo prático'''

# Analisar uma base de dados de um arquivo txt e descobrir o faturamento da loja

with open('vendasloja.txt', 'r') as arquivo: # A função with open serve para ler um arquivo, o r significa read, que traduzido é: ler. -------- se quisessemos escrever neste arquivo, seria colocado um 'w'.
    texto = arquivo.read()
lista_texto = texto.split('\n') # Split divide a string usando o enter(que no Python é representado com \n) como delimitador.

faturamento = 0

# Excluir a 1ª linha

lista_texto = lista_texto[1:] # Assim nós basicamente falamos para o PY ignorar o primeiro item e pegar até o final

# Para cada linha do meu arquivo, eu quero somar o valor que vem depois do ;

for linha in lista_texto:
    posicao_pv = linha.find(';') # pv é ponto e vírgula abreviado --- o find mostra o local em que esta o: ';'
    valor = float(linha[posicao_pv + 1 : ]) # Aqui o py vai começar a ler um caractere depois do ';'
    faturamento += valor # Essa linha vai ler o antigo valor e somar com o novo valor.

print(faturamento)