from trip import Trip


def create_trips() -> list[Trip]:
    return [
        Trip("Paris"),
        Trip("New York"),
        Trip("Tokyo"),
        Trip("Sydney"),
        Trip("Rio de Janeiro"),
    ]


def show_menu(traveler: str, trips: list[Trip]) -> None:
    print("Temos as seguintes viagens disponíveis:")
    print(f"Olá, {traveler}! Para onde você gostaria de viajar?")
    for i, trip in enumerate(trips, start=1):
        print(f"{i}. {trip.destiny}")


def read_choice(total: int) -> int | None:
    try:
        choice = int(input("Digite o número da viagem desejada:\n"))
    except ValueError:
        print(f"Entrada inválida. Digite um número entre 1 e {total}.")
        return None

    if 1 <= choice <= total:
        return choice

    print(f"Opção inválida. Por favor, escolha um número entre 1 e {total}.")
    return None


def main() -> None:
    trips = create_trips()
    traveler = input("Digite seu nome para começar:\n").strip()

    if not traveler:
        print("Nome inválido.")
        return

    show_menu(traveler, trips)
    choice = read_choice(len(trips))
    if choice is None:
        return

    selected_trip = trips[choice - 1]
    print(f"Ótima escolha, {traveler}! Você escolheu viajar para {selected_trip.destiny}.")


if __name__ == "__main__":
    main()
