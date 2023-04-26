#!/usr/bin/env python
# coding: utf-8

# In[18]:


import matplotlib.pyplot as plt

# função para plotar gráfico de cada opção
def plotar_grafico(bits, opcao):
    tamanho = len(bits)
    nivel = 1
    # Codificação NRZ-I
    # Codificação NRZ-I
    if opcao == 1:
        cod_nrzi = []
        cod_nrzi.append(1)
        for bit in bits:
            if bit == 0:
                cod_nrzi.append(cod_nrzi[-1])
            else:
                cod_nrzi.append(-cod_nrzi[-1])
        cod_nrzi.pop(0)
        plt.step(range(tamanho), cod_nrzi, where='post', color='red')
        plt.ylabel('NRZ-I')
        plt.plot([tamanho-1,tamanho], [cod_nrzi[-1], cod_nrzi[-1]], color='red', linestyle='-')


    # Codificação NRZ-L
    elif opcao == 2:
        cod_nrzl = []
        for bit in bits:
            if bit == 0:
                cod_nrzl.append(nivel)
            else:
                cod_nrzl.append(-nivel)
        plt.step(range(tamanho), cod_nrzl, where='post', color='red')
        plt.ylabel('NRZ-L')
        plt.plot([tamanho-1,tamanho], [cod_nrzl[-1], cod_nrzl[-1]], color='red', linestyle='-')

    # Codificação AMI
    elif opcao == 3:
        cod_ami = []
        for bit in bits:
            if bit == 0:
                cod_ami.append(0)
            else:
                cod_ami.append(nivel)
                nivel = -nivel
        plt.step(range(tamanho), cod_ami, where='post', color='red')
        plt.ylabel('AMI')
        plt.plot([tamanho-1,tamanho], [cod_ami[-1], cod_ami[-1]], color='red', linestyle='-')

    # Codificação Pseudoternário
    elif opcao == 4:
        alterna = 0
        cod_pseudoternario = []
        for bit in bits:
            if bit == 0:
                if alterna == 0:
                    cod_pseudoternario.append(nivel)
                    alterna = 1
                else:
                    cod_pseudoternario.append(-nivel)
                    alterna = 0
            else:
                cod_pseudoternario.append(0)
        plt.step(range(tamanho), cod_pseudoternario, where='post', color='red')
        plt.ylabel('Pseudoternário')
        plt.plot([tamanho-1,tamanho], [cod_pseudoternario[-1], cod_pseudoternario[-1]], color='red', linestyle='-')

    # Codificação Manchester
    elif opcao == 5:
        cod_manchester = []
        for bit in bits:
            if bit == 0:
                cod_manchester.extend([1, -1])
            else:
                cod_manchester.extend([-1, 1])
        plt.step(range(2*tamanho), cod_manchester, where='mid', color='red')
        plt.ylabel('Manchester')

    # Codificação Manchester Diferencial
    elif opcao == 6:
        cod_manchester_diff = []
        polaridade = -1
        for bit in bits:
            if bit == 0:
                cod_manchester_diff.extend([polaridade, -polaridade])
            else:
                polaridade = -polaridade
                cod_manchester_diff.extend([polaridade, -polaridade])
        plt.step(range(2*tamanho), cod_manchester_diff, where='mid', color='red')
        plt.ylabel('Manchester Diferencial')

    # Codificação RZ Unipolar
    elif opcao == 7:
        cod_rz_unipolar = []
        for bit in bits:
            if bit == 0:
                cod_rz_unipolar.append(0)
                cod_rz_unipolar.append(0)
            else:
                cod_rz_unipolar.extend([1, 0])
        plt.step(range(2*tamanho), cod_rz_unipolar, where='mid', color='red')
        plt.ylabel('RZ Unipolar')
        
    # Codificação RZ Bipolar
    elif opcao == 8:
        alterna = 0
        cod_rz_bipolar = []
        for bit in bits:
            if bit == 0:
                cod_rz_bipolar.append(0)
                cod_rz_bipolar.append(0)
            else:
                if alterna == 0:
                    cod_rz_bipolar.extend([1, 0])
                    alterna = 1
                else:
                    cod_rz_bipolar.extend([-1, 0])
                    alterna = 0
        plt.step(range(2*tamanho), cod_rz_bipolar, where='mid', color='red')
        plt.ylabel('RZ Bipolar')    
    
    if(opcao < 5):
        plt.xticks(range(tamanho), bits)
        x_positions = [i + 0.5 for i in range(len(bits))] #!!!!!!!!!!!!!!!!!!!!!!!!#
        plt.xticks(x_positions, bits[:])                  #!!!!!!!!!!!!!!!!!!!!!!!!#
        
        plt.xlabel('Bits')
        plt.axhline(y=0, color='black', linestyle='solid', alpha=0.3)
        for i in range(0, tamanho+1):
            plt.axvline(x=i, color='gray', linestyle='--', alpha=0.3) #Traçado vertical
    else:
        plt.xticks(range(tamanho), bits)
        x_positions = [2*i + 0.7 for i in range(len(bits))] #!!!!!!!!!!!!!!!!!!!!!!!!#
        plt.xticks(x_positions, bits[:])
        plt.xlabel('Bits')
        plt.axhline(y=0, color='black', linestyle='solid', alpha=0.3)

        
    plt.ylim(-tamanho*0.5, tamanho*0.5) # Definindo a escala do eixo y
    plt.yticks([], [])  # Remove os ticks e valores do eixo y
    plt.show()

# leitura dos bits
bits = input("Insira a sequência de bits usando 1 e 0: ")
bits = [int(bit) for bit in bits]

# escolha da opção
print("Escolha a opção de codificação que deseja usar e gerar o gráfico:")
print("1 - NRZ-I")
print("2 - NRZ-L")
print("3 - AMI")
print("4 - Pseudoternário")
print("5 - Manchester")
print("6 - Manchester Diferencial")
print("7 - RZ Unipolar")
print("8 - RZ Bipolar")
opcao = int(input())

# plotagem do gráfico da opção escolhida
plotar_grafico(bits, opcao)
