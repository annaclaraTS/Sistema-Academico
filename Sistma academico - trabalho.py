# ------------------------------------------------------------
# SISTEMA ACADÊMICO – Revisão completa da disciplina
# ALUNA - Anna Clara Thomaz Sarmento
# ------------------------------------------------------------

# Listas de cadastro
L_nome = []
L_idade = []
L_data = []
L_cpf = []
L_email = []
L_disciplina = []
L_notas = []

def menu():
    print('--------------- Sistema Academico ---------------')
    print(' ')
    print('MENU:')
    print('1 - Cadastrar estudante')
    print('2 - Cadastrar disciplinas')
    print('3 - Cadastrar notas')
    print('4 - Situação das disciplinas')
    print('5 - Situação do aluno')
    print('6 - Ficha completa do estudante')
    print('7 - Sair')

    numero = int(input('Qual opção: '))

    while numero in [1,2,3,4,5,6,7]:
        if numero == 1:
            c_estudante()
        elif numero == 2:
            c_disciplinas()
        elif numero == 3:
            c_notas()
        elif numero == 4:
            s_disciplina()
        elif numero == 5:
            s_aluno()
        elif numero == 6:
            t_cadastros()
        elif numero == 7:
            exit()
    else:
        print('Número inválido!\n')
        menu()

def c_estudante():
     print('------- CADASTRO ESTUDANTE -------')
     nome = str(input('Nome completo: '))
     idade = int(input('Idade: '))
     data = str(input('Data de nascimento: '))
     cpf = str(input('CPF: '))
     email = str(input('Email: '))

     L_nome.append(nome)
     L_idade.append(idade)
     L_data.append(data)
     L_cpf.append(cpf)
     L_email.append(email)

     print('\nCadastro realizado!\n')
     menu()

def c_disciplinas():
     print('------- CADASTRO DISCIPLINAS -------')
     L_disciplina.clear()

     for i in range(5):
         entrada = input(f'Digite o nome da disciplina {i+1}: ')
         L_disciplina.append(entrada)

     print('\nDisciplinas cadastradas!\n')
     menu()

def c_notas():
     print('------- CADASTRO NOTAS -------')
     L_notas.clear()

     for i in range (5):
         nota = float(input(f'Digite a nota final de {L_disciplina[i]}: '))

         while nota < 0 or nota > 10:
             print('Nota inválida! Digite entre 0 e 10.')
             nota = float(input(f'Digite a nota de {L_disciplina[i]}: '))

         L_notas.append(nota)

     print('\nNotas cadastradas!\n')
     menu()

def s_disciplina():
    print('------- SITUAÇÃO DAS DISCIPLINAS -------\n')

    for i in range(5):
        nota = L_notas[i]

        if nota == 10:
            situacao = "Aprovado com distinção"
        elif nota >= 6:
            situacao = "Aprovado"
        else:
            situacao = "Reprovado"

        print(f"{L_disciplina[i]} - Nota: {nota} => {situacao}")

    print('\n----------------------------------\n')
    menu()

def s_aluno():
    print("------- SITUAÇÃO DO ALUNO -------\n")

    reprovadas = 0

    for nota in L_notas:
        if nota < 6:
            reprovadas += 1

    # regra da situação do aluno
    if reprovadas == 0:
        situacao = "Passou de ano direto"
    elif reprovadas <= 2:
        situacao = "Passou de ano com dependência"
    else:
        situacao = "Retido"

    print(f"O aluno {L_nome[0]} está: {situacao}\n")

    menu()

def t_cadastros():
    print('------- FICHA COMPLETA DO ESTUDANTE -------\n')

    print(f"Nome: {L_nome[0]}")
    print(f"Idade: {L_idade[0]}")
    print(f"Nascimento: {L_data[0]}")
    print(f"CPF: {L_cpf[0]}")
    print(f"Email: {L_email[0]}\n")

    print('------- Situação das disciplinas -------')
    for i in range(5):
        nota = L_notas[i]
        if nota == 10:
            situacao = "Aprovado com distinção"
        elif nota >= 6:
            situacao = "Aprovado"
        else:
            situacao = "Reprovado"

        print(f"{L_disciplina[i]} - Nota: {nota} => {situacao}")

    print('\n------- Situação geral do aluno -------')
    reprovadas = 0
    for nota in L_notas:
        if nota < 6:
            reprovadas += 1

    if reprovadas == 0:
        situacao = "Passou de ano direto"
    elif reprovadas <= 2:
        situacao = "Passou de ano com dependência"
    else:
        situacao = "Retido"

    print(situacao)
    print('\n----------------------------------------\n')

    menu()

menu()