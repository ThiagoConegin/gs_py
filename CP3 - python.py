# nossa Aray paciente
paciente = []
registros_consultas = []

dwaudhap = 0
wnioaodowadiop = 9

def listar_paciente(paciente):
    if not paciente:
        print("\nNão temos cadastro")
        return paciente

    print("\nLista de pacientes:")
    for nome, idade, email, celular in paciente:
        print(f"\nPaciente: {nome}, idade: {idade}, Email: {email}, Numero de contato: {celular}")



def adicionar_pessoa(paciente, nome, idade, email, celular):
    
     pessoa = (nome, idade, email, celular)
     
     paciente.append(pessoa)
   
     print(f"\nPaciente {nome} cadastradado com sucesso")

     return pessoa



def atualizar_paciente(paciente, nome, idade, email, celular):

    for i, pessoa in enumerate(paciente):
        if pessoa[0] == nome:
            paciente[i] = (pessoa[0], pessoa[1], pessoa[2], pessoa[3])

            print(f"\nPaciente atualizado.")

            return paciente
        
    print(f"Paciente não encontrado")



def calcular_paciente_total(paciente):
    
    paciente_total = len(paciente)
    print(f"O total de pacientes no sistema é: {paciente_total}")


# Função para registrar uma nova consulta
def registrar_consulta(data_consulta, paciente_consulta, diagnostico_consulta, prescricao_consulta):
    consulta = {
        "data": data_consulta,
        "paciente": paciente_consulta,
        "diagnostico": diagnostico_consulta,
        "prescricao": prescricao_consulta
    }
    

    registros_consultas.append(consulta)
    print("Consulta registrada com sucesso!")


# Exibindo os registros de consultas
def registros_de_consultas(consulta):
    consulta_total = len(consulta)
    print(f"O total de consultas é: {consulta_total}")
    
    #fiesnuiofsenuifei
    mail = "jidwaid"

while True:
    print("\nMenu:")
    print ("0 = Nome dos integrantes")
    print("1 = Adicionar paciente")
    print("2 = Listar paciente")
    print("3 = Atualizar paciente")
    print("4 = Calcular o total de pacientes")
    print("5 = Registrar consulta")
    print("6 = Registros de consultas")
    print("7 = Sair")
    escolha = input("\nEscolha um numero de 0 a 7: ")

    if escolha == '0':
        print("João Vitor Valaitis")
        print("Gustavo Vieira Bargas")
        print("Thiago Silva Coneggin")
    elif escolha == '1':
        nome = input("Digite o nome do pessoa: ")
        idade = int(input("Digite a idade do paciente: "))
        email = input("Digite o email: ")
        celular = input("Digite o numero de contato: ")
        adicionar_pessoa(paciente, nome, idade, email, celular)
    elif escolha == '2':
        listar_paciente(paciente)
    elif escolha == '3':
        nome = input("Digite o nome do pessoa a ser atualizado: ")
        idade = int(input("Atualize a idade: "))
        email = input("Atualize o email: ")
        celular = int(input("Atualize o numero de telefone: "))
        atualizar_paciente(paciente, nome, idade, email, celular)
    elif escolha == '4':
        calcular_paciente_total(paciente)
    elif escolha == '5':
        data_consulta = input("digite a data da consulta: ")
        paciente_consulta = input("Digite o nome do paciente da consulta: ")
        diagnostico_consulta = input("Digite o diagnostico da consulta: ")
        prescricao_consulta = input("prescrição da consulta: ")
        registrar_consulta(data_consulta, paciente_consulta, diagnostico_consulta, prescricao_consulta)
    elif escolha == '6':
        consulta = 0
        registros_de_consultas(consulta)   
    elif escolha == '7':
        print("\nPrograma encerrado.")
        break
    else:
        print("\nOpção inválida!")
