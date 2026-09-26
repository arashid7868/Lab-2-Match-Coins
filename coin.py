"""
Program: Match Coins Game - Coin Class
Author: Arashid
Purpose: Represents a single coin that can be tossed and can show
         either Heads or Tails.
Starter Code: None. Created for Lab 2 - Chapter 9.
Date: September 26, 2026
"""

import random


class Coin:
    """Represents a single tossable coin."""

    def __init__(self):
        """Initialize the coin with a side of Heads."""
        self.__sideup = "Heads"

    def toss(self):
        """Toss the coin and randomly set it to Heads or Tails."""
        if random.randint(0, 1) == 0:
            self.__sideup = "Heads"
        else:
            self.__sideup = "Tails"

    def get_sideup(self):
        """Return the current side of the coin."""
        return self.__sideup