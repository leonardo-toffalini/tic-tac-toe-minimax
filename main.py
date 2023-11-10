import pygame
from board import Board
from game import Game


def main():
    screen = pygame.display.set_mode((600, 600))
    board = Board(screen, 600, 600, 'X')
    game = Game(board)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                board.handle_click(*pos)
            if event.type == pygame.KEYDOWN:
                print(game.minimax())

        if game.check_winner() is not None:
            if (winner := game.check_winner()) in ['O', 'X']:
                print(f'Winner: {winner}')
            else:
                print('Tie')
            running = False

        board.draw()
        pygame.display.update()

if __name__ == '__main__':
    main()