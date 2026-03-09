import webbrowser

done = False

while not done:
    print('O que você deseja fazer?\n')
    print('1 - Aprender Python')
    print('2 - Aprender sobre módulos')
    print('3 - Aprender sobre Python, JavaScript, HTML e CSS')
    print('4 - Sair')

    choice = input('>')
    if choice == '1':
        webbrowser.open('https://docs.python.org/3/')
    elif choice == '2':
        webbrowser.open('https://docs.python.org/3/py-modindex.html')
    elif choice == '3':
        webbrowser.open('https://www.w3schools.com/')
    elif choice == '4':
        done = True
    else:
        print('Opção inválida. Tente novamente.')
