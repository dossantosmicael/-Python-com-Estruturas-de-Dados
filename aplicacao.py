from GUI import *
import backend as core

app = None

def view_command():
    rows = core.view()
    app.listClientes.delete(0, END)
    for r in rows:
        app.listClientes.insert(END, r)

def search_command():
    app.listClientes.delete(0, END)
    rows = core.search(app.txtNome.get(), app.txtSobrenome.get(), app.txtEmail.get(), app.txtCPF.get())
    for r in rows:
        app.listClientes.insert(END, r)

def insert_command():
    core.insert(app.txtNome.get(), app.txtSobrenome.get(), app.txtEmail.get(), app.txtCPF.get())
    view_command()

def update_command():
    core.update(selected[0], app.txtNome.get(), app.txtSobrenome.get(), app.txtEmail.get(), app.txtCPF.get())
    view_command()

def del_command():
    id = selected[0]
    core.delete(id)
    view_command()

def getSelectedRow(event):
    global selected
    if app.listClientes.curselection():  # Certificando que há um item selecionado
        index = app.listClientes.curselection()[0]
        selected = app.listClientes.get(index)

        app.entNome.delete(0, END)
        app.entNome.insert(END, selected[1])

        app.entSobrenome.delete(0, END)
        app.entSobrenome.insert(END, selected[2])

        app.entEmail.delete(0, END)
        app.entEmail.insert(END, selected[3])

        app.entCPF.delete(0, END)
        app.entCPF.insert(END, selected[4])

if __name__ == "__main__":
    window = Tk()
    app = Gui(window)

    # Vinculando eventos e comandos aos botões e lista
    app.listClientes.bind('<<ListboxSelect>>', getSelectedRow)

    app.btnViewAll.configure(command=view_command)
    app.btnBuscar.configure(command=search_command)
    app.btnInserir.configure(command=insert_command)
    app.btnUpdate.configure(command=update_command)
    app.btnDel.configure(command=del_command)
    app.btnClose.configure(command=app.window.destroy)

    app.run()
