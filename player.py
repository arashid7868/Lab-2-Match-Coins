"""
Program: Match Coins Game - Player Class
Author: Arashid
Purpose: Represents a player with a name, wallet, and Coin object.
         Demonstrates composition by using the Coin class.
Starter Code: None. Created for Lab 2 - Chapter 9.
Date: September 26, 2026
"""

from coin import Coin


class Player:
    """Represents a player in the Match Coins game."""

    def __init__(self, name):
        """Initialize the player with a name, 20 coins, and a Coin object."""
        self.__name = name
        self.__wallet = 20
        self.__coin = Coin()

    def toss_coin(self):
        """Toss the player's coin."""
        self.__coin.toss()

    def get_coin_side(self):
        """Return the current side of the player's coin."""
        return self.__coin.get_sideup()

    def win_coin(self):
        """Add one coin to the player's wallet."""
        self.__wallet += 1

    def lose_coin(self):
        """Remove one coin from the player's wallet."""
        self.__wallet -= 1

    def get_wallet(self):
        """Return the player's current number of coins."""
        return self.__wallet

    def get_name(self):
        """Return the player's name."""
        return self.__name