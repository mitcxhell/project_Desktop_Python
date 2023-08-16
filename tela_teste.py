import PySimpleGUI as sg
import sqlite3 as bbb

# Establish a connection to the database
conn = bbb.connect("clientes.db")
c = conn.cursor()

# Create the layout for the main menu
layout = [
    [sg.Menu([
        ['Cadastro', ['Cadastro Clientes',
                      'Cadastro Fornecedores', 'Cadastro Transportadora']],
        ['Consulta', ['Consulta Clientes',
                      'Consulta Fornecedores', 'Consulta Transportadora']],
        ['Relatórios', ['Relatórios Clientes',
                        'Relatórios Fornecedores', 'Relatórios Transportadora']]
    ], tearoff=False)]
]

# Create the main window
window_cliente = sg.Window("Sistema de cadastro de clientes 1.0", layout, size=(600, 400))

# Event loop for the main window
while True:
    event, values = window_cliente.read()

    if event == sg.WINDOW_CLOSED:
        break

    elif event == "Cadastro Clientes":
        cadastro_layout_clientes = [
            [sg.Text("Nome")],
            [sg.InputText(key="Nome")],
            [sg.Text("CPF")],
            [sg.InputText(key="CPF")],
            [sg.Text("Endereço")],
            [sg.InputText(key="Endereço")],
            [sg.Text("Telefone")],
            [sg.InputText(key="Telefone")],
            [sg.Text("Cidade")],
            [sg.InputText(key="Cidade")],
            [sg.Text("Estado")],
            [sg.InputText(key="Estado")],
            [sg.Button("Cadastro"), sg.Button("Cancelar")]
            # ... (Client registration window setup)
        ]

        # Create the client registration window
        cadastro_clientes = sg.Window("Cadastro de Clientes", cadastro_layout_clientes, size=(400, 400))

        # Event loop for the client registration window
        while True:
            event, values = cadastro_clientes.read()

            if event == sg.WINDOW_CLOSED or event == "Cancelar":
                cadastro_clientes.close()
                break

            # ... (Client registration logic)
            c.execute("INSERT INTO clientes (Nome, CPF, Endereço, Telefone, Cidade, Estado) VALUES (?, ?, ?, ?, ?, ?)",
                    (values["Nome"], values["CPF"], values["Endereço"], values["Telefone"], values["Cidade"], values["Estado"]))
            conn.commit()
        
            cadastro_clientes["Nome"].update("")
            cadastro_clientes["CPF"].update("")
            cadastro_clientes["Endereço"].update("")
            cadastro_clientes["Telefone"].update("")
            cadastro_clientes["Cidade"].update("")
            cadastro_clientes["Estado"].update("")
            sg.popup("Cadastro efetuado!")

    elif event == "Cadastro Fornecedores":
        fornecedor_layout = [            
            # ... (Supplier registration window setup)
                [sg.Text("ID")],
                [sg.InputText(key="Id_fornecedor")],
                [sg.Text("Nome")],
                [sg.InputText(key="Nome_fornecedor")],
                [sg.Text("Endereço")],
                [sg.InputText(key="Endereço")],
                [sg.Text("CEP")],
                [sg.InputText(key="CEP")],
                [sg.Text("Cidade")],
                [sg.InputText(key="Cidade")],
                [sg.Text("Estado")],
                [sg.InputText(key="Estado")],
                [sg.Text("País")],
                [sg.InputText(key="País")],
                [sg.Button("Cadastro"), sg.Button("Cancelar")]
 
        ]

        # Create the supplier registration window
        cadastro_fornecedor = sg.Window("Cadastro de Fornecedores", fornecedor_layout, size=(400, 400))

        # Event loop for the supplier registration window
        while True:
            event, values = cadastro_fornecedor.read()

            if event == sg.WINDOW_CLOSED or event == "Cancelar":
                cadastro_fornecedor.close()
                break

            # ... (Supplier registration logic)
            c.execute("INSERT INTO fornecedores (Id_fornecedor, Nome_fornecedor, Endereço, CEP, Cidade, Estado, País) VALUES (?, ?, ?, ?, ?, ?, ?)",
                        (values["Id_fornecedor"], values["Nome_fornecedor"], values["Endereço"], values["CEP"], values["Cidade"], values["Estado"], values["País"] ))
            conn.commit()
    
            cadastro_fornecedor["Id_fornecedor"].update("")
            cadastro_fornecedor["Nome_fornecedor"].update("")
            cadastro_fornecedor["Endereço"].update("")
            cadastro_fornecedor["CEP"].update("")
            cadastro_fornecedor["Cidade"].update("")
            cadastro_fornecedor["Estado"].update("")
            cadastro_fornecedor["País"].update("") 
            sg.popup("Cadastro efetuado!")


    elif event == "Cadastro Transportadora":
        transportadora_layout = [            
            # ... (Supplier registration window setup)
                [sg.Text("ID")],
                [sg.InputText(key="Id_transportadora")],
                [sg.Text("Nome")],
                [sg.InputText(key="Nome_transportadora")],
                [sg.Text("Telefone")],
                [sg.InputText(key="Telefone")],
                [sg.Button("Cadastro"), sg.Button("Cancelar")]
 
        ]

        # Criar a janela de cadastro do fornecedor
        cadastro_transportadora = sg.Window("Cadastro de Fornecedores", transportadora_layout, size=(400, 400))

        # Event loop para registrar os fornecedores no banco
        while True:
            event, values = cadastro_transportadora.read()

            if event == sg.WINDOW_CLOSED or event == "Cancelar":
                cadastro_transportadora.close()
                break

            # ... (Supplier registration logic)
            c.execute("INSERT INTO fornecedores (Id_Transportadora, Nome_trasnportadora, Telefone) VALUES (?, ?, ?)",
                        (values["Id_fornecedor"], values["Nome_fornecedor"], values["Telefone"]))
            conn.commit()
    
            cadastro_fornecedor["Id_transportadora"].update("")
            cadastro_fornecedor["Nome_transportadora"].update("")
            cadastro_fornecedor["Telefone"].update("") 
# Close all windows and the database connection
window_cliente.close()
conn.close()