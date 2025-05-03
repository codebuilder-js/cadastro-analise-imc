# Sistema de Cadastro e Análise de IMC

Este é um programa em Python que permite cadastrar usuários, listar seus dados e analisar o IMC (Índice de Massa Corporal) de cada um.

## Funcionalidades

O programa funciona via terminal e oferece as seguintes opções de menu:

1. **Cadastrar usuário**  
   Permite ao usuário inserir nome, e-mail, idade, peso e altura. O sistema valida o e-mail e calcula automaticamente o IMC.

2. **Listar usuários**  
   Exibe uma lista com os nomes, e-mails e idades dos usuários cadastrados.

3. **Analisar IMC dos usuários**  
   Exibe o IMC de cada usuário e classifica o status de acordo com a tabela:
   - Abaixo do peso: IMC < 18.5
   - Peso normal: 18.5 ≤ IMC < 25
   - Sobrepeso: 25 ≤ IMC < 30
   - Obesidade: IMC ≥ 30

4. **Sair**  
   Encerra a execução do programa.

## Exemplo de uso

```bash
$ python sistema_imc.py

Menu:
1 - Cadastrar usuário
2 - Listar usuários
3 - Analisar IMC dos usuários
4 - Sair
Escolha uma opção: 1
Nome: João
E-mail: joao@example.com
Idade: 30
Peso (kg): 70
Altura (m): 1.75
João cadastrado com sucesso!
