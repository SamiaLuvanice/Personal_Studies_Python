teams = {}
done  = False

# Função para listar times
def print_teams():
    print("Times Listados:")
    for i, team in enumerate(teams.values()):
        print(f"{i+1}. {team['name']} ({len(team['players'])} jogadores)")

# Funçaõ para listar jogadores de um time
def print_team_players(team):
    print(f"Jogadores do time {team['name']}:")
    for i, player in enumerate(team['players']):
        print(f" - {i+1}. {player}")

while not done:
    # Opções do programa
    print("O que você deseja fazer?")
    print("1. Adicionar time")
    print("2. Remover time")
    print("3. Listar times")
    print("4. Adicionar jogador a um time")
    print("5. Remover jogador de um time")
    print("6. Listar jogadores de um time")
    print("7. Sair")

    choice = input(">")
    if choice == "1":
        team_name = input("Digite o nome do time: ")
        teams[team_name] = {"name": team_name, "players": []}
        print(f"Time '{team_name}' adicionado com sucesso!")
    elif choice == "2":
        print_teams()
        team_num = int(input("Digite o número do time que deseja remover: "))
        if 1 <= team_num <= len(teams):
            team_name = list(teams.keys())[team_num - 1]
            del teams[team_name]
            print(f"Time '{team_name}' removido com sucesso!")
        else:
            print("Número de time inválido.")
    elif choice == "3":
        print_teams()
    elif choice == "4":
        print_teams()
        team_num = int(input("Digite o número do time para adicionar um jogador: "))
        if team_num <= len(teams):
            team_name = list(teams.keys())[team_num - 1]
            player_name = input("Digite o nome do jogador: ")
            teams[team_name]['players'].append(player_name)
            print(f"Jogador '{player_name}' adicionado ao time '{team_name}' com sucesso!")
        else:
            print("Número de time inválido.")
    elif choice == "5":
        print_teams()
        team_num = int(input("Digite o número do time para remover um jogador: "))
        if team_num <= len(teams):
            team_name = list(teams.keys())[team_num - 1]
            print_team_players(teams[team_name])
            player_num = int(input("Digite o número do jogador para remover: \n "))
            if player_num <= len(teams[team_name]['players']):
                del teams[team_name]['players'][player_num - 1]
                print(f"Jogador removido do time '{team_name}' com sucesso!")
            else:
                print("Número de jogador inválido.")
        else:
            print("Número de time inválido.")                
    elif choice == "6":
        print_teams()
        team_num = int(input("Digite o número do time para listar os jogadores: "))
        if team_num <= len(teams):
            team_name = list(teams.keys())[team_num - 1]
            print_team_players(teams[team_name])
        else:
            print("Número de time inválido.")
    elif choice == "7":
        done = True
    else:
        print("Opção inválida, tente novamente.")

        