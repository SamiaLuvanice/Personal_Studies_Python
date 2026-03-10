import tkinter as tk

# 1 - Criar a janela principal
root = tk.Tk()
root.geometry("300x150")
root.title("Gerenciador de Frases")

# 2 - Adicionando o Frame
frame = tk.Frame(root)
frame.pack(padx=10, pady=10, fill='x', expand=True)

# 3 - Adicionando o Label
label = tk.Label(frame, text="Hello, Tkinter!")
label.pack(fill='x', expand=True)

# 4 - Adicionando input de texto
frase_lab = tk.Label(frame, text='Frase')
frase_lab.pack(fill='x', expand=True)

frase_input = tk.Entry(frame)
frase_input.pack(fill='x', expand=True)

# 5 - Função para alterra o texto do label
def click():
    label.config(text=frase_input.get())

# 6 - Adicionando o botão
button = tk.Button(frame, text="Enviar", command=click)
button.pack(fill='x')

root.mainloop()
