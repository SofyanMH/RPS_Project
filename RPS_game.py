import random

#!/usr/bin/env python3

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def __init__(self):
        self.score = 0
        self.my_move = ""
        self.their_move = ""

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move


class ReflectPlayer(Player):
    def move(self):
        if self.their_move not in moves:
            return random.choice(moves)
        else:
            return self.their_move


class CyclePlayer(Player):
    def move(self):
        if self.my_move == 'rock':
            return 'paper'
        elif self.my_move == 'paper':
            return 'scissors'
        elif self.my_move == 'scissors':
            return 'rock'
        else:
            return random.choice(moves)


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


class HumanPlayer(Player):
    def move(self):
        move = ""
        while move not in moves:
            move = (input("Rock, paper, scissors? ")).lower()
        return move


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()

        print(f"Player One: {move1}  Player Two: {move2}")
        if beats(move1, move2):
            self.p1.score += 1
            print("***** Player One wins the round! *****")
        elif beats(move2, move1):
            self.p2.score += 1
            print("***** Player Two wins the round! *****")
        else:
            print("***** TIE! *****")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        print("Score: Player One (" + (str(self.p1.score)) +
              ") Player Two (" + (str(self.p2.score)) + ")")
        print("")

    def play_game(self):
        print("Game start!")
        round = 1
        while abs(self.p1.score - self.p2.score) < 3:
            print(f"Round {round}:")
            self.play_round()
            round += 1
        print("******************Game over!******************")
        if self.p1.score > self.p2.score:
            print("********** Player One won the game! **********")
        elif self.p2.score > self.p1.score:
            print("********** Player Two won the game! **********")
        print("Final Score: Player One (" + (str(self.p1.score)) +
              ") Player Two (" + (str(self.p2.score)) + ")")


if __name__ == '__main__':
    option1 = ""
    option2 = ""
    player1 = ""
    player2 = ""
    print("")
    print("Welcome to the Rock, Paper, Scissor Game!")
    while option1 not in ['simple', 'reflective',
                          'cyclic', 'random', 'human']:
        while option2 not in ['simple', 'reflective',
                              'cyclic', 'random', 'human']:
            print("")
            print("Choose Players:")
            print("1 : Simple")
            print("2 : Reflective")
            print("3 : Cyclic")
            print("4 : Random")
            print("5 : Human")
            option1 = input("Player One: ").lower()
            option2 = input("Player Two: ").lower()
    if option1 == "simple":
        player1 = Player()
    if option1 == "reflective":
        player1 = ReflectPlayer()
    if option1 == "cyclic":
        player1 = CyclePlayer()
    if option1 == "random":
        player1 = RandomPlayer()
    if option1 == "human":
        player1 = HumanPlayer()
    if option2 == "simple":
        player2 = Player()
    if option2 == "reflective":
        player2 = ReflectPlayer()
    if option2 == "cyclic":
        player2 = CyclePlayer()
    if option2 == "random":
        player2 = RandomPlayer()
    if option2 == "human":
        player2 = HumanPlayer()
    game = Game(player1, player2)
    game.play_game()
