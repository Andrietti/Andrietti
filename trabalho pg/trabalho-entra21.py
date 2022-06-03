import PySimpleGUI as sg
import io, os
from PIL import Image

file_types = [('Imagens', '*.png *.jpg *.jpeg *.bmp'), ('Todos os arquivos', '*.*')]

lista_dia = []
lista_mes = []
lista_ano = []
for i in range(1, 32):
    lista_dia.append(str(i))
for i in range(1, 13):
    lista_mes.append(str(i))
for i in range(1940, 2023):
    lista_ano.append(str(i))

lista_usuarios = []
lista_senhas = []


# Criar as janelas e estilos (layout)

def janela_login():
    sg.theme('SystemDefaultForReal')
    layout = [
        [sg.Image(filename='entra.png')],
        [sg.Text('Usuário',font=("Helvetica", 12), size=(8, 1)), sg.InputText(key='usuario')],
        [sg.Text('Senha',font=("Helvetica", 12), size=(8, 1)), sg.InputText(key='senha', password_char='*')],
        [sg.Checkbox('Salvar Login?', key='lembrar')],
        [sg.Button('Entrar', size=(10, 1)), sg.Button('Cadastrar', size=(10, 1))],
        [sg.Text('', size=(10, 1), key='mensagem')]
        
    ]

    return sg.Window('Login', layout=layout, finalize=True, element_justification='center')

def janela_cadastro():
    sg.theme('SystemDefaultForReal')
    layout = [

        [
        sg.FileBrowse(file_types=file_types, key='foto', size=(10, 1), enable_events=True, button_text='Selecionar Foto')
        ],

        [sg.Text('PAINEL DE CADASTRO',font=("Helvetica", 20), size=(20, 1))],
        [sg.Text('Nome',font=("Helvetica", 12), size=(5, 1)), sg.InputText(key='nome', size=(54, 1))],

        [sg.Text('Data de Nasc.', font=("Helvetica", 12), size=(11, 1)),
        sg.Combo(lista_dia, key='dia', size=(3, 1)),
        sg.Text('/'),
        sg.Combo(lista_mes, key='mes', size=(3, 1)),
        sg.Text('/'),
        sg.Combo(lista_ano, key='ano', size=(5, 1)),
        sg.Text('Sexo', font=("Helvetica", 12), size=(4, 1)), 
        sg.Combo(('Masculino', 'Feminino'), key='sexo', size=(10, 1))],
        [sg.Text('Telefone', font=("Helvetica", 12), size=(7, 1)), sg.InputText(key='telefone', size=(20, 1)), sg.Text('Celular', font=("Helvetica", 12), size=(7, 1)), sg.InputText(key='celular', size=(20, 1))],
         
        [sg.Text('E-mail', font=("Helvetica", 12), size=(5, 1)), sg.InputText(key='email', size=(40, 1))],
        [sg.Text('Usuário', font=("Helvetica", 12), size=(6, 1)), sg.InputText(key='usuario', size=(30, 1))],
        [sg.Text('Senha', font=("Helvetica", 12), size=(5, 1)), sg.InputText(key='senha', password_char='*', size=(31, 1))],
        [sg.Text('Confirmar Senha', font=("Helvetica", 12), size=(13, 1)), sg.InputText(key='confirmar', password_char='*', size=(21, 1))],
        [sg.Button(button_text='cadastrar', size=(10, 1)), sg.Button('Voltar', size=(10, 1))],

    ]

    return sg.Window('Cadastro', layout=layout, finalize=True)

janela1, janela2 = janela_login(), None

# Criar um loop de leitura de eventos
while True:
    window,event,values = sg.read_all_windows()
    # Quando a janela for fechada
    if window == janela1 and event == sg.WIN_CLOSED:
        break
    elif window == janela2 and event == sg.WIN_CLOSED:
        break

    # Quando o botão de cadastro for clicado
    if window == janela1 and event == 'Cadastrar':
        janela2 = janela_cadastro()
        janela1.hide()
    # Quando o botão de voltar for clicado
    if window == janela2 and event == 'Voltar':
        janela2.hide()
        janela1.un_hide()

    if window == janela2 and event == 'cadastrar':
        lista_usuarios.append(values['usuario'])
        lista_senhas.append(values['senha'])
        print(lista_usuarios)
        print(lista_senhas)
    if window == janela1 and event == 'Entrar':
        if values["usuario"] in lista_usuarios:
                try:
                    if lista_usuarios.index(values["usuario"]) == lista_senhas.index(values["senha"]):
                        print("Senha válida")
                        print("Logado com sucesso!")
                    elif lista_usuarios.index(values["usuario"]) != lista_senhas.index(values["senha"]):
                        print("Senha inválida!")
                except:
                    print("Senha inválida")
        else:
            print("Usuário inválido")
        
        