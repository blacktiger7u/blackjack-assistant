
cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
def get_card_value(card):
    if card in ['J', 'Q', 'K']:
        return 10
    elif card == 'A':
        return 11
    else:
        return int(card)


def calculate_hand_value(hand):
    total = 0
    aces = 0

    for card in hand:
        if card == 'A':
            aces += 1
            total += 11
        else:
            total += get_card_value(card)

    while total > 21 and aces > 0:
        total -= 10
        aces -= 1

    return total


def analyze_move(player_cards, dealer_card):
    player_value = calculate_hand_value(player_cards)
    dealer_value = get_card_value(dealer_card)

    print(f"\n{'=' * 50}")
    print(f"ANALIZA: Cards: {player_cards} (value: {player_value})")
    print(f"Dealers card: {dealer_card} (value: {dealer_value})")
    print(f"{'=' * 50}")

    # Szansa na bust przy braniu karty
    bust_count = 0
    safe_count = 0

    for card in cards:
        new_value = calculate_hand_value(player_cards + [card])
        if new_value > 21:
            bust_count += 1
        else:
            safe_count += 1

    bust_probability = (bust_count / len(cards)) * 100
    safe_probability = (safe_count / len(cards)) * 100

    print(f"\n📊 STATS:")
    print(f"  Bust chance (> 21): {bust_probability:.1f}%")
    print(f"  Safe probability: {safe_probability:.1f}%")

    # Rekomendacja
    print(f"\n💡ADVICE:")
    if player_value >= 17:
        print(f"  👉 STAND- Stand, ur hand is good")
    elif player_value <= 11:
        print(f"  👉 HIT - Bust chance is low")
    elif bust_probability > 50:
        print(f"  👉 STAND - Bust chance is high")
    else:
        print(f"  👉 HIT -Chance to improve hand is high")


def main():
    print("=" * 50)
    print("Blackjack Assistant")
    print("=" * 50)

    while True:
        print("\n[1] Analyze")
        print("[2] Wyjdź")

        choice = input("\nWybór: ").lower()

        if choice == '1':
            player_input = input("Put your cards (np. K 5 A): ").upper().split()
            dealer_input = input("Put dealers cards (np. 7): ").upper()

            try:
                analyze_move(player_input, dealer_input)
            except:
                print("❌ ERROR")

        elif choice == '2':
            print("see ya")
            break
        else:
            print("Unknown command.")


if __name__ == "__main__":
    main()
