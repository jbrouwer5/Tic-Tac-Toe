import pygame
pygame.init()

size = width, height = 460, 510

# initalizes the screen
screen = pygame.display.set_mode(size)

# defines the colors for the board
black = 0, 0, 0
white = 255, 255, 255
light_grey = 200, 200, 200
red = 255, 0, 0
blue = 0, 0, 255
green = 0, 255, 0

# initializes array representing board with every square set to empty
# value of 0 represents empty, 1 represents x, 2 represents o
board = [0, 0, 0, 0, 0, 0, 0, 0, 0]

# defines the x and o graphics for the board
font = pygame.font.SysFont(None, 150)
turn_font = pygame.font.SysFont(None, 36)
x_token = font.render('x', True, red)
o_token = font.render('o', True, blue)

play_again = turn_font.render("Play Again", True, black)

# tracks whose turn it is, starts with x
x_turn = True

# method for highlighting the square that the mouse is hovering on


def highlight_square(x, y):

    mouse_x = x
    mouse_y = y

    col = -1

    # checks column
    if mouse_x > 0 and mouse_x < 150:
        col = 0
    elif mouse_x > 155 and mouse_x < 305:
        col = 1
    elif mouse_x > 310 and mouse_x < 465:
        col = 2

    # checks row
    if col >= 0:
        if mouse_y > 50 and mouse_y < 200 and board[col] == 0:
            pygame.draw.rect(screen, light_grey, (col * 155, 50, 150, 150))
        if mouse_y > 205 and mouse_y < 355 and board[col + 3] == 0:
            pygame.draw.rect(screen, light_grey, (col * 155, 205, 150, 150))
        if mouse_y > 360 and mouse_y < 510 and board[col + 6] == 0:
            pygame.draw.rect(screen, light_grey, (col * 155, 360, 150, 150))

# contains actions when the user clicks the screen


def on_click(x, y):

    mouse_x = x
    mouse_y = y

    col = -1

    # checks column
    if mouse_x > 0 and mouse_x < 150:
        col = 0
    elif mouse_x > 155 and mouse_x < 305:
        col = 1
    elif mouse_x > 310 and mouse_x < 465:
        col = 2

    # checks row and changes array value if a square was clicked
    if col >= 0:
        if mouse_y > 50 and mouse_y < 200 and board[col] == 0:
            if x_turn:
                board[col] = 1
                return True
            else:
                board[col] = 2
                return True

        if mouse_y > 205 and mouse_y < 355 and board[col + 3] == 0:
            if x_turn:
                board[col + 3] = 1
                return True
            else:
                board[col + 3] = 2
                return True

        if mouse_y > 360 and mouse_y < 510 and board[col + 6] == 0:
            if x_turn:
                board[col + 6] = 1
                return True
            else:
                board[col + 6] = 2
                return True

        return False

# defines a method that draws the current board with the Xs and Os in the
# correct locations


def add_tokens():

    for i in range(9):

        if i % 3 == 0:
            x = 75
        elif i % 3 == 1:
            x = 230
        else:
            x = 385

        y = (i // 3) * 155 + 125

        if board[i] == 1:
            textRect = x_token.get_rect()
            textRect.center = x, y
            screen.blit(x_token, textRect)
        elif board[i] == 2:
            textRect = o_token.get_rect()
            textRect.center = x, y
            screen.blit(o_token, textRect)

# checks if the board is full


def full_board():
    if (board[0] != 0 and
        board[1] != 0 and
        board[2] != 0 and
        board[3] != 0 and
        board[4] != 0 and
        board[5] != 0 and
        board[6] != 0 and
        board[7] != 0 and
            board[8] != 0):

        return True

    return False

# checks to see if the game has been won by looking for 3 in a row


def is_winner():
    winner = 0

    if board[0] == board[1] == board[2] != 0:
        winner = board[0]
        pygame.draw.rect(screen, black, (55, 127.5, 350, 5))
    if board[3] == board[4] == board[5] != 0:
        winner = board[3]
        pygame.draw.rect(screen, black, (55, 282.5, 350, 5))
    if board[6] == board[7] == board[8] != 0:
        winner = board[6]
        pygame.draw.rect(screen, black, (55, 437.5, 350, 5))
    if board[0] == board[3] == board[6] != 0:
        winner = board[0]
        pygame.draw.rect(screen, black, (73.75, 105, 5, 355))
    if board[1] == board[4] == board[7] != 0:
        winner = board[1]
        pygame.draw.rect(screen, black, (228.75, 105, 5, 355))
    if board[2] == board[5] == board[8] != 0:
        winner = board[2]
        pygame.draw.rect(screen, black, (383.75, 105, 5, 355))
    if board[0] == board[4] == board[8] != 0:
        winner = board[0]
        poly = ((61, 113), (64, 111), (399, 446), (396, 449))
        pygame.draw.polygon(screen, black, poly)
    if board[2] == board[4] == board[6] != 0:
        winner = board[2]
        poly = ((61, 446), (64, 449), (399, 114), (396, 111))
        pygame.draw.polygon(screen, black, poly)

    if winner != 0:
        return winner

    if full_board():
        return -1

    return 0

# defines a method that declares the winner and adds a play again button
# after a win


def on_end(result):
    if result == -1:
        res = turn_font.render("Tie Game", True, black)
        resRect = res.get_rect()
        resRect.center = 232.5, 25
        screen.blit(res, resRect)
    elif result == 1:
        res = turn_font.render("X Wins!", True, black)
        resRect = res.get_rect()
        resRect.center = 232.5, 25
        screen.blit(res, resRect)
    elif result == 2:
        res = turn_font.render("O Wins!", True, black)
        resRect = res.get_rect()
        resRect.center = 232.5, 25
        screen.blit(res, resRect)

    #pygame.draw.rect(screen, black, (305, 5, 140, 36))
    pygame.draw.rect(screen, black, (305, 5, 140, 36), 1)
    againRect = play_again.get_rect()
    againRect.center = 375, 24
    screen.blit(play_again, againRect)

# draws an empty game board with lines separating the rows and columns


def draw_board():
    # fills the screen with white
    screen.fill((255, 255, 255))

    # a line to separate the board from the top section
    pygame.draw.rect(screen, black, (0, 45, 465, 5))

    # draws the tic-tac-toe board lines
    pygame.draw.rect(screen, black, (150, 50, 5, 460))
    pygame.draw.rect(screen, black, (305, 50, 5, 460))
    pygame.draw.rect(screen, black, (0, 200, 460, 5))
    pygame.draw.rect(screen, black, (0, 355, 460, 5))


# runs the game
while 1:
    click = False
    placed = False
    again = False

    # checks for quitting the tab and clicking
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if (event.type == pygame.MOUSEBUTTONDOWN and
                pygame.mouse.get_pressed()[0]):
            click = True

    mouse_x = pygame.mouse.get_pos()[0]
    mouse_y = pygame.mouse.get_pos()[1]

    draw_board()

    if click:
        placed = on_click(mouse_x, mouse_y)

    result = is_winner()

    # checks of the game is still going and if so changes the turn
    if result == 0:
        if x_turn:
            turn = turn_font.render("Turn: X", True, black)
        else:
            turn = turn_font.render("Turn: O", True, black)

        turnRect = turn.get_rect()
        turnRect.center = 50, 25
        screen.blit(turn, turnRect)

    add_tokens()
    highlight_square(mouse_x, mouse_y)

    if placed:
        x_turn = not x_turn

    # checks if the game is over
    if result != 0:
        on_end(result)

        pygame.display.flip()

        while (not again):

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

                mouse_x = pygame.mouse.get_pos()[0]
                mouse_y = pygame.mouse.get_pos()[1]

                # checks if the user clicks play again
                # if clicked it resets the board
                if (event.type == pygame.MOUSEBUTTONDOWN and
                        pygame.mouse.get_pressed()[0]):

                    if (mouse_x >= 305 and mouse_x <= 445 and
                            mouse_y >= 10 and mouse_y <= 40):
                        again = True

                        board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
                        x_turn = True

                if (mouse_x >= 305 and mouse_x <= 445 and
                        mouse_y >= 10 and mouse_y <= 40):
                    pygame.draw.rect(screen, light_grey, (305, 5, 140, 36))
                    pygame.draw.rect(screen, black, (305, 5, 140, 36), 1)
                else:
                    pygame.draw.rect(screen, white, (305, 5, 140, 36))
                    pygame.draw.rect(screen, black, (305, 5, 140, 36), 1)

                againRect = play_again.get_rect()
                againRect.center = 375, 24
                screen.blit(play_again, againRect)
                pygame.display.flip()

    # displays the board
    pygame.display.flip()
