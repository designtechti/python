# -*- coding: utf-8 -*-

# Manipulando arquivos #

arquivo = open("hello world.html")

textoCompleto = arquivo.read() # Lê todo o conteúdo do arquivo

print(textoCompleto)

linha = arquivo.readline() # Lê o conteúdo do arquivo 

print(linha)

linhas = arquivo.readlines() 

print(linhas)

arquivo.close()

#####################################

w = open("arquivo2.txt", "w") # Abre um novo arquivo com permissões de somente escrita

w.write("Esse é o meu arquivo") # Escreve um conteúdo no arquivo criado anteriormente
w.close()

"""
	---------------------------------------------------------------------------------------------------------------------
	|  MODO  |		 FUNÇÃO 		|									DESCRIÇÃO										|
	---------------------------------------------------------------------------------------------------------------------
	|	r    |  leitura		  		|	Somente leitura.																|
	|	w    |  escrita 			|	Caso o arquivo já exista, ele será apagado e um novo arquivo vazio será criado.	|
	|	a    |  leitura & escrita 	|	Adiciona um novo conteúdo no fim do arquivo.									|
	|	r+   |  leitura & escrita 	|																					|
	|	w+	 |	escrita				|	Assim como o modo w também apaga o conteúdo do arquivo anterior.				|
	|	a+	 |	leitura & escrita	|	Abre o arquivo para atualização.												|
	---------------------------------------------------------------------------------------------------------------------
	
"""