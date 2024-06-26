import pygame

# Initialize Pygame
pygame.init()

# Set up the display
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Arcade Arena")

# Define colors
PINK = (255, 192, 203)
VIOLET = (238, 130, 238)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Load background image
background = pygame.image.load("background.jpg")
background = pygame.transform.scale(background, (WINDOW_WIDTH, WINDOW_HEIGHT))

# Define button dimensions
BUTTON_WIDTH = 200
BUTTON_HEIGHT = 50

# Define button positions
button_positions = [
    (200, 100),  # Brick Breaker
    (400, 100),  # Dino Run
    (200, 200),  # Flappy Bird
    (400, 200),  # Minesweeper
    (200, 300),  # Pacman
    (400, 300),  # Snake
    (200, 400),  # Space Invasion
    (400, 400),  # Tetris
    (300, 500)   # Exit, centered
]


# Define game paths
game_paths = {
    "Brick Breaker": "games/brick-breaker/src/main.py",
    "Dino Run": "games/dino-run/src/main.py",
    "Flappy Bird": "games/flappy-bird/src/main.py",
    "Minesweeper": "games/minesweeper/main.py",
    "Pacman": "games/pacman/src/main.py",
    "Snake": "games/snake/src/main.py",
    "Space Invasion": "games/space-invasion/src/main.py",
    "Tetris": "games/tetris/src/main.py"
}

# Define button text
button_text = [
    "Brick Breaker", "Dino Run", "Flappy Bird",
    "Minesweeper", "Pacman", "Snake",
    "Space Invasion", "Tetris", "Exit"
]

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if a button was clicked
            mouse_x, mouse_y = pygame.mouse.get_pos()
            for i, (x, y) in enumerate(button_positions):
                if x <= mouse_x <= x + BUTTON_WIDTH and y <= mouse_y <= y + BUTTON_HEIGHT:
                    if i == len(button_positions) - 1:  # Exit button
                        running = False
                    elif button_text[i]:  # Game button
                        game_path = game_paths.get(button_text[i], None)
                        if game_path:
                            # Run the game's main.py file
                            import subprocess
                            subprocess.run(["python", game_path])

    # Draw background
    window.blit(background, (0, 0))

    # Draw title
    font = pygame.font.Font(None, 80)
    text = font.render("Arcade Arena", True, WHITE, BLACK)
    text_rect = text.get_rect()
    text_rect.centerx = WINDOW_WIDTH // 2
    text_rect.top = 20
    window.blit(text, text_rect)

    # Draw border around title
    border_rect = text_rect.inflate(10, 10)
    pygame.draw.rect(window, BLACK, border_rect, 2)

    # Draw buttons
    for i, (x, y) in enumerate(button_positions):
        button_color = PINK if i % 3 == 0 else VIOLET if i % 3 == 1 else YELLOW
        pygame.draw.rect(window, button_color, (x, y, BUTTON_WIDTH, BUTTON_HEIGHT))
        text = button_text[i]
        if text:
            font = pygame.font.Font(None, 24)
            text_surface = font.render(text, True, (0, 0, 0))
            text_rect = text_surface.get_rect()
            text_rect.center = (x + BUTTON_WIDTH // 2, y + BUTTON_HEIGHT // 2)
            window.blit(text_surface, text_rect)

    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()