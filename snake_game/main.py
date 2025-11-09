"""
Main module for the Snake Game.
Entry point that initializes pygame and runs the main game loop.
"""

import pygame
from config import Config
from game import Game


def main() -> None:
    """Main function to initialize and run the Snake game."""
    # Initialize pygame
    pygame.init()
    
    # Set up the display
    screen = pygame.display.set_mode((Config.SCREEN_WIDTH, Config.SCREEN_HEIGHT))
    pygame.display.set_caption("Snake Game")
    
    # Create clock for controlling frame rate
    clock = pygame.time.Clock()
    
    # Create game instance
    game = Game(Config.SCREEN_WIDTH, Config.SCREEN_HEIGHT)
    
    # Main game loop
    running: bool = True
    while running:
        # Handle events
        game.handle_events()
        
        # Update game state
        game.update()
        
        # Draw everything
        game.draw(screen)
        
        # Update the display
        pygame.display.flip()
        
        # Control frame rate
        clock.tick(Config.FPS)
    
    # Quit pygame
    pygame.quit()


if __name__ == "__main__":
    main()
