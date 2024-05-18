#!/usr/bin/python3
import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class Minesweeper:
    def __init__(self, width: int = 10, height: int = 10, mines: int = 10):
        self.width = width
        self.height = height
        self.mines = set(random.sample(range(width * height), min(mines, width * height)))
        self.field = [[' ' for _ in range(width)] for _ in range(height)]
        self.revealed = [[False for _ in range(width)] for _ in range(height)]

    def print_board(self, reveal: bool = False):
        clear_screen()
        print('   ' + ' '.join(f'{i:2}' for i in range(self.width)))
        for y in range(self.height):
            print(f'{y:2} ', end='')
            for x in range(self.width):
                if reveal or self.revealed[y][x]:
                    if (y * self.width + x) in self.mines:
                        print('* ', end='')
                    else:
                        count = self.count_mines_nearby(x, y)
                        print(f'{count} ' if count > 0 else '  ', end='')
                else:
                    print('. ', end='')
            print()

    def count_mines_nearby(self, x: int, y: int) -> int:
        count = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height and (ny * self.width + nx) in self.mines:
                    count += 1
        return count

    def reveal(self, x: int, y: int) -> bool:
        if (y * self.width + x) in self.mines:
            return False
        self.revealed[y][x] = True
        if self.count_mines_nearby(x, y) == 0:
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < self.width and 0 <= ny < self.height and not self.revealed[ny][nx]:
                        self.reveal(nx, ny)
        return True

    def play(self):
        while True:
            self.print_board()
            try:
                coords = input("Enter coordinates (x y): ").split()
                if len(coords) != 2:
                    raise ValueError("Please enter two numbers separated by a space.")
                x, y = map(int, coords)
                if not (0 <= x < self.width and 0 <= y < self.height):
                    raise ValueError("Coordinates out of bounds.")
                if not self.reveal(x, y):
                    self.print_board(reveal=True)
                    print("Game Over! You hit a mine.")
                    break
            except ValueError as e:
                print(f"Invalid input: {e}. Please try again.")

if __name__ == "__main__":
    while True:
        game = Minesweeper()
        game.play()
        if input("Play again? (y/n): ").lower() != 'y':
            break
