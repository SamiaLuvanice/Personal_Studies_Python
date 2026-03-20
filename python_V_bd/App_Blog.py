from Blog import show_menu, add_user, add_post, query_user_posts

while True:
    show_menu()
    choice = input("Escolha uma opção: ")

    if choice == '1':
        add_user()
    elif choice == '2':
        add_post()
    elif choice == '3':
        query_user_posts()
    elif choice == '4':
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
