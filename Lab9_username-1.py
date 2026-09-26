"""
Program: Match Coins Game
Author: Arashid
Purpose: Runs an interactive Match Coins game using the Player class
         and demonstrates object-oriented programming and composition.
Starter Code: None. Created for Lab 2 - Chapter 9.
Date: September 26, 2026
"""

from player import Player


def main():
    """Run the Match Coins game."""

    print("--- Coin Match Game ---")

    player1 = Player("Player 1")
    player2 = Player("Player 2")

    print(f"{player1.get_name()} has {player1.get_wallet()} coins.")
    print(f"{player2.get_name()} has {player2.get_wallet()} coins.")

    play_again = "y"

    while play_again.lower() == "y":
        print("\nTossing...")

        player1.toss_coin()
        player2.toss_coin()

        side1 = player1.get_coin_side()
        side2 = player2.get_coin_side()

        print(f"{player1.get_name()} tossed {side1}")
        print(f"{player2.get_name()} tossed {side2}")

        if side1 == side2:
            player1.win_coin()
            player2.lose_coin()
            print("...It's a Match! Player 1 wins a coin.")
        else:
            player2.win_coin()
            player1.lose_coin()
            print("...No Match! Player 2 wins a coin.")

        print()
        print(f"{player1.get_name()} has {player1.get_wallet()} coins.")
        print(f"{player2.get_name()} has {player2.get_wallet()} coins.")

        # End the game if either player has no coins.
        if player1.get_wallet() == 0 or player2.get_wallet() == 0:
            print("\nA player has no coins left. Game over!")
            break

        play_again = input("\nDo you want to toss the coins? (y/n): ")

    print("\n--- Final Score ---")
    print(f"{player1.get_name()}: {player1.get_wallet()}")
    print(f"{player2.get_name()}: {player2.get_wallet()}")

    if player1.get_wallet() > player2.get_wallet():
        print(f"{player1.get_name()} wins the game!")
    elif player2.get_wallet() > player1.get_wallet():
        print(f"{player2.get_name()} wins the game!")
    else:
        print("It's a draw!")


if __name__ == "__main__":
    main()