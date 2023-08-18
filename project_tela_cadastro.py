import PySimpleGUI as sg
import sqlite3 as bbb

# Establish a connection to the database
conn = bbb.connect("clientes.db")
c = conn.cursor()

# Create the layout for the main menu
layout = [
    [sg.Menu([
        ['Cadastro', ['Cadastro Clientes', 'Cadastrar Produtos',
                      'Cadastro Fornecedores', 'Cadastro Transportadora']],
        ['Consulta', ['Consulta Clientes', 'Consultar Produto',
                      'Consulta Fornecedores', 'Consulta Transportadora']],
        ['Relatórios', ['Relatórios de Clientes', 'Relatórios de Produtos',
                        'Relatórios de Fornecedores', 'Relatórios de Transportadoras']]
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




    elif event == "Cadastrar Produtos":
        cadastro_produto_layout = [
            [sg.Text("Produto")],
            [sg.InputText(key="produto")],
            [sg.Text("Valor")],
            [sg.InputText(key="valor")],
            [sg.Button("Cadastro"), sg.Button("Cancelar")]
            # ... (Client registration window setup)
        ]

        # Create the client registration window
        cadastro_produto = sg.Window("Cadastro de Clientes", cadastro_produto_layout, size=(400, 400))

        # Event loop for the client registration window
        while True:
            event, values = cadastro_produto.read()

            if event == sg.WINDOW_CLOSED or event == "Cancelar":
                cadastro_produto.close()
                break

            # ... (Client registration logic)
            c.execute("INSERT INTO vendas (produto, valor) VALUES (?, ?)",
                    (values["produto"], values["valor"]))
            conn.commit()
        
            cadastro_produto["produto"].update("")
            cadastro_produto["valor"].update("")
            
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
        cadastro_transportadora = sg.Window("Cadastro de Transportadora", transportadora_layout, size=(400, 400))

        # Event loop para registrar os fornecedores no banco
        while True:
            event, values = cadastro_transportadora.read()

            if event == sg.WINDOW_CLOSED or event == "Cancelar":
                cadastro_transportadora.close()
                break

            # ... (Supplier registration logic)
            c.execute("INSERT INTO transportadora (Id_Transportadora, Nome_transportadora, Telefone) VALUES (?, ?, ?)",
                        (values["Id_transportadora"], values["Nome_transportadora"], values["Telefone"]))
            conn.commit()
    
            cadastro_transportadora["Id_transportadora"].update("")
            cadastro_transportadora["Nome_transportadora"].update("")
            cadastro_transportadora["Telefone"].update("")
            sg.popup("Cadastro efetuado!")

    elif event == "Relatórios de Produtos":
            relatorio_layout = [            
                # ... (Supplier registration window setup)
                    [sg.Text("Produto")],
                    [sg.InputText(key="produto")],
                    [sg.Button("Gerar relatório"), sg.Button("Cancelar")]
    
            ]


            # Criar a janela de cadastro do fornecedor
            relatorio_window = sg.Window("Relatório", relatorio_layout, resizable=True)

            # Event loop para registrar os fornecedores no banco
            while True:
                event, values = relatorio_window.read()

                if event == sg.WINDOW_CLOSED or event == "Cancelar":
                    relatorio_window.close()
                    break

                # ... (Supplier registration logic)
                produto_busca = values["produto"].upper()
                c.execute("SELECT * FROM vendas WHERE UPPER(produto) = ?", (produto_busca,))
                registro = c.fetchone()

                if registro:

                    with open("C:/Users/alunosenac/Desktop/Project_Desktop_Python/relatorio.html", "w") as f:
                        f.write("<html><head></head><body>")
                        f.write(f"<h1>Relatório</h1><table border='1'><tr><th>Produtos</th><th>Valor</th></tr>")
                        f.write(f"<tr><th>{registro[0]}</th><th>{registro[1]}</th></tr>")
                        f.write("</body></html>")
                
                    sg.popup("Relatório gerado com sucesso!", title="Relatório")
                
                else:
                    sg.popup("Produto não encontrado no banco de dados!", title="Relatório")

                relatorio_window["produto"].update("")

    elif event == "Relatórios de Clientes":
            relatorio_client_layout = [            
                # ... (Supplier registration window setup)
                    [sg.Text("Nome")],
                    [sg.InputText(key="Nome")],
                    [sg.Button("Gerar relatório"), sg.Button("Cancelar")]
    
            ]


            # Criar a janela de cadastro do fornecedor
            relatorio_client_window = sg.Window("Relatório", relatorio_client_layout, resizable=True)

            # Event loop para registrar os fornecedores no banco
            while True:
                event, values = relatorio_client_window.read()

                if event == sg.WINDOW_CLOSED or event == "Cancelar":
                    relatorio_client_window.close()
                    break

                # ... (Supplier registration logic)
                client_busca = values["Nome"].upper()
                c.execute("SELECT * FROM clientes WHERE UPPER(Nome) = ?", (client_busca,))
                registro_client = c.fetchone()

                if registro_client:

                    with open("C:/Users/alunosenac/Desktop/Project_Desktop_Python/relatorio_client.html", "w") as f:
                        f.write("<html><head></head><body>")
                        f.write(f"<h1>Relatório</h1><table border='1'><tr><th>Nome</th><th>CPF</th><th>Endereço</th><th>Telefone</th><th>Cidade</th><th>Estado</th></tr>")
                        f.write(f"<tr><th>{registro_client[0]}</th><th>{registro_client[1]}</th><th>{registro_client[2]}</th><th>{registro_client[3]}</th><th>{registro_client[4]}</th><th>{registro_client[5]}</th></tr>")
                        f.write("</body></html>")
                
                    sg.popup("Relatório gerado com sucesso!", title="Relatório")
                
                else:
                    sg.popup("Produto não encontrado no banco de dados!", title="Relatório")

                relatorio_client_window["Nome"].update("")   



    elif event == "Relatórios de Fornecedores":
            report_supplier_layout = [            
                # ... (Supplier registration window setup)
                    [sg.Text("Nome")],
                    [sg.InputText(key="Nome_fornecedor")],
                    [sg.Button("Gerar relatório"), sg.Button("Cancelar")]
    
            ]


            # Criar a janela de cadastro do fornecedor
            repport_supplier_window = sg.Window("Relatório", report_supplier_layout, resizable=True)

            # Event loop para registrar os fornecedores no banco
            while True:
                event, values = repport_supplier_window.read()

                if event == sg.WINDOW_CLOSED or event == "Cancelar":
                    repport_supplier_window.close()
                    break

                # ... (Supplier registration logic)
                supplier_search = values["Nome_fornecedor"].upper()
                c.execute("SELECT * FROM fornecedores WHERE UPPER(Nome_fornecedor) = ?", (supplier_search,))
                #record_supplier = c.fetchone()
                record_supplier = c.fetchone()

                if record_supplier:

                    with open("relatorio_fornecedor.html", "w") as f:
                        f.write("<html><head></head><body>")
                        f.write(f"<h1>Relatório</h1><table border='1'><tr><th>ID Supplier</th><th>Name</th><th>Address</th><th>Postal Code</th><th>C</th><th>City</th><th>State</th><th>Country</th></tr>")
                            
                       # for row in registro_f:
                        f.write("<tr><td>{row[0]}</td><td>{row[1]}</td></tr>")
                       #f.write("</table></body></html>")
                        f.write(f"<tr><th>{record_supplier[0]}</th><th>{record_supplier[1]}</th><th>{record_supplier[2]}</th><th>{record_supplier[3]}</th><th>{record_supplier[4]}</th><th>{record_supplier[5]}</th></tr>")
                        #f.write("</body></html>")
                
                    sg.popup("Relatório gerado com sucesso!", title="Relatório")
                
                else:
                    sg.popup("Produto não encontrado no banco de dados!", title="Relatório")

                repport_supplier_window["Nome_fornecedor"].update("") 
    


# Close all windows and the database connection
window_cliente.close()
conn.close()