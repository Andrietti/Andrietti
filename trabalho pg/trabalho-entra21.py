from tkinter import Button
from weakref import finalize
import PySimpleGUI as sg
import io, os
from PIL import Image
from sqlalchemy import column

file_types = [('Imagens', '*.png *.jpg *.jpeg *.bmp'), ('Todos os arquivos', '*.*')]

lista_dia = []
lista_mes = ['jan.', 'fev.', 'mar.', 'abr.', 'maio', 'jun.' , 'jul.', 'ago.', 'set.', 'out.', 'nov.', 'dez.']
lista_ano = []
for i in range(1, 32):
    lista_dia.append(str(i))
for i in range(1940, 2023):
    lista_ano.append(str(i))

lista_usuarios = ["123"]
lista_senhas = ["321"]
lista_nomes = []
lista_sobrenomes = []



# Criar as janelas e estilos (layout)

def janela_login():
    sg.theme('SystemDefaultForReal')
    layout = [
        [sg.Image(filename='entra.png')],
        [sg.Text('Email', font=("Helvetica", 12), size=(8, 1)), sg.InputText(key='email')],
        [sg.Text('Senha', font=("Helvetica", 12), size=(8, 1)), sg.InputText(key='senha', password_char='*')],
        [sg.Checkbox('Salvar Login?', key='lembrar')],
        [sg.Button('Entrar', size=(10, 1)), sg.Button('Cadastrar', size=(10, 1))],
        [sg.Text('', size=(10, 1), key='mensagem')]

    ]

    return sg.Window('Login', layout=layout, finalize=True, element_justification='center')


def janela_cadastro():
    sg.theme('SystemDefaultForReal')
    layout = [

        [sg.Text('Primeiro nome')],
        [sg.Input(key='primeironome')],
        [sg.Text('Ultimo nome')],
        [sg.Input(key='sobrenome')],
        [sg.Text('Email')],
        [sg.Input(key='email')],
        [sg.Text('Exemplo: nome@exemplo.com')],
        [sg.Text('Senha')],
        [sg.Input(key='senha', password_char= "*")],
        [sg.Text('Confirmar senha')],
        [sg.Input(key='confirmar', password_char= "*")],
        [sg.Button('Salvar'), sg.Button('Voltar')]
    ]

    return sg.Window('Cadastro', layout=layout, finalize=True)


# btn_layout = [
#     [sg.Image(key="-IMAGE-")],
#     [sg.FileBrowse('Procurar Img', file_types=file_types, key="-FILE-", size=(11, 1)),
#      sg.Button("Load Image", size=(11, 1)), ],
# ]


def janela_perfil():
    sg.theme('SystemDefaultForReal')
    sg.theme("Reddit")

    layout = [
        [sg.Image(key="-IMAGE-")],
        [sg.FileBrowse('Procurar Img', file_types=file_types, key="-FILE-", size=(11, 1)),
        sg.Button("Load Image", size=(11, 1)), ],
        [sg.Text('Nome:')],
        [sg.Input(key='abc')],
        [sg.Input(size=(62, 1))],



        [sg.Text('Data de Nasc.'),
         sg.Combo(lista_dia, key='dia'),
         sg.Text('/'),
         sg.Combo(lista_mes, key='mes'),
         sg.Text('/'),
         sg.Combo(lista_ano, key='ano'),
         sg.Text('Sexo'),
         sg.Combo(('Masculino', 'Feminino'), key='sexo', size=(10, 1))],
        [sg.Text('Telefone'), sg.InputText(key='telefone', size=(21, 1)),
         sg.Text('Celular'), sg.InputText(key='celular', size=(22, 1))],
        [sg.Button("Voltar"), sg.Button('Salvar')]
    ]

    return sg.Window("Seu perfil", layout=layout, finalize=True)


janela1, janela2, janela3 = janela_login(), None, None

# Criar um loop de leitura de eventos
while True:
    window, event, values = sg.read_all_windows()
    # Quando a janela for fechada
    if window == janela1 and event == sg.WIN_CLOSED:
        break
    elif window == janela2 and event == sg.WIN_CLOSED:
        break
    elif window == janela3 and event == sg.WIN_CLOSED:
        break

    # Quando o botão de cadastro for clicado
    if window == janela1 and event == 'Cadastrar':
        janela1.hide()
        janela2 = janela_cadastro()
    # Quando o botão de voltar for clicado
    if window == janela2 and event == 'Voltar':
        janela2.close()
        janela1 = janela_login()

    if window == janela3 and event == "Voltar":
        janela3.close()
        janela1 = janela_login()

    if event == "Load Image":
        filename = values["-FILE-"]
        if os.path.exists(filename):
            image = Image.open(values["-FILE-"])
            image.thumbnail((200, 200), Image.ANTIALIAS)
            bio = io.BytesIO()
            # Actually store the image in memory in binary
            image.save(bio, format="PNG")
            # Use that image data in order to
            window["-IMAGE-"].update(data=bio.getvalue())

    if window == janela2 and event == 'Salvar':

        
        if values['senha'] == "" or values['email'] == "":
            sg.popup("Informações inválidas")
        elif values["senha"] == values["confirmar"]:

            lista_usuarios.append(values['email'])
            lista_senhas.append(values['senha'])
            lista_nomes.append(values['primeironome'])
            lista_sobrenomes.append(values['sobrenome'])
            sg.popup("Cadastrado com sucesso")
            janela2.close()
            janela1 = janela_login()
        else:
            sg.popup("As senhas não coincidem")

    if window == janela1 and event == 'Entrar':
        if values["email"] in lista_usuarios:
            try:
                if lista_usuarios.index(values["email"]) == lista_senhas.index(values["senha"]):
                    sg.popup("Logado com sucesso!")
                    janela1.close()
                    janela3 = janela_perfil()
                elif lista_usuarios.index(values["email"]) != lista_senhas.index(values["senha"]):
                    sg.popup("Senha inválida!")
            except:
                sg.popup('Usuário inválido')

        else:
            sg.popup("Usuário não cadastrado!")
        
