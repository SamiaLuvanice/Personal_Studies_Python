import os

# Defein o caminho absoluto do arquivo de contatos
contacts_file = os.path.join(os.path.dirname(__file__), 'contacts.txt')

def add_contact():
    name = input('Informe o nome:')
    address = input('Informe o endereço:')
    phone = input('Informe o telefone:')

    contact = f"Nome: {name}\nEndereço: {address}\nTelefone: {phone}\n\n"

    with open(contacts_file, 'a', encoding='utf-8') as file:
        file.write(contact)

def view_contacts():
    if not os.path.exists(contacts_file):
        print('Nenhum contato encontrado.')
        return
    with open(contacts_file, 'r', encoding='utf-8') as file:
        contacts = file.read()
    print("Lista de Contatos:")
    print(contacts)

def delete_contacts():
    if not os.path.exists(contacts_file):
        print('Lista de contatos está vazia.')
        return
    with open(contacts_file, 'w', encoding='utf-8') as file:
        file.write('')

    print('Todos os contatos foram deletados.')