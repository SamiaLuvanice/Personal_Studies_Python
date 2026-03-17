from agenda import add_contact, view_contacts, delete_contacts

def main():
    while True:
        print("__Agenda de Contatos__")
        print("1. Adicionar contato")
        print("2. Listar contatos")
        print("3. Remover contatos")
        print("4. Sair")

        choice = input("Escolha uma opção (1-4):\n")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            delete_contacts()
        elif choice == '4':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()