from tkinter import Tk, Label, Button

root = Tk()
root.title("Minha Primeira Janela")
root.geometry("300x200")

label = Label(root, text="Bem-vindo ao Tkinter!", font=("Arial", 14), fg="blue")
label.pack(pady=20)

def button_function():
    print("button pressed")

button = Button(root, text="Clique Aqui", command=button_function)
button.pack(pady=10)

root.mainloop()