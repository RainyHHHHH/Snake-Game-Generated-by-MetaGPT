"""
Game module for the Snake Game.
Contains the Game class that manages the main game loop, events, and state.
"""

import pygame
import sys
from typing import Optional
from config import Config
from snake import Snake
from food import Food


class Game:
    """Main game class that manages the game state and loop."""
    
    def __init__(self, width: int, height: int) -> None:
        """
        Initialize the game.
        
        Args:
            width: Screen width
            height: Screen height
        """
        self.screen_width: int = width
        self.screen_height: int = height
        self.score: int = 0
        self.game_over: bool = False
        
        # Initialize snake and food
        start_x, start_y = Config.get_initial_snake_position()
        self.snake: Snake = Snake(start_x, start_y, Config.BLOCK_SIZE)
        self.food: Food = Food(Config.BLOCK_SIZE)
    
    def handle_events(self) -> None:
        """Handle pygame events including keyboard input."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.KEYDOWN:
                # Handle game reset (available in any state)
                if event.key == pygame.K_r:
                    self.reset_game()
                    continue  # Skip further processing after reset
                
                # Handle direction changes (only when game is running)
                if not self.game_over:
                    if event.key == pygame.K_UP:
                        self.snake.change_direction("UP")
                    elif event.key == pygame.K_DOWN:
                        self.snake.change_direction("DOWN")
                    elif event.key == pygame.K_LEFT:
                        self.snake.change_direction("LEFT")
                    elif event.key == pygame.K_RIGHT:
                        self.snake.change_direction("RIGHT")
    
    def update(self) -> None:
        """Update game state including snake movement and collision detection."""
        if not self.game_over:
            # Move the snake
            self.snake.move()
            
            # Check if snake ate food
            snake_head = self.snake.get_head_position()
            food_position = self.food.get_position()
            
            if snake_head == food_position:
                self.snake.grow()
                self.score += 1
                self.food.generate_new_position(self.screen_width, self.screen_height)
            
            # Check for collisions
            if self.snake.check_collision(self.screen_width, self.screen_height):
                self.game_over = True
    
    def draw(self, screen: pygame.Surface) -> None:
        """
        Draw all game elements on the screen.
        
        Args:
            screen: Pygame surface to draw on
        """
        # Clear screen
        screen.fill(Config.BACKGROUND_COLOR)
        
        # Draw snake and food
        self.snake.draw(screen)
        self.food.draw(screen)
        
        # Draw score
        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score: {self.score}", True, Config.TEXT_COLOR)
        screen.blit(score_text, (10, 10))
        
        # Draw game over message if applicable
        if self.game_over:
            game_over_font = pygame.font.Font(None, 72)
            game_over_text = game_over_font.render("GAME OVER", True, Config.TEXT_COLOR)
            restart_text = font.render("Press R to restart", True, Config.TEXT_COLOR)
            
            # Center the game over text
            game_over_rect = game_over_text.get_rect(center=(self.screen_width // 2, self.screen_height // 2 - 50))
            restart_rect = restart_text.get_rect(center=(self.screen_width // 2, self.screen_height // 2 + 20))
            
            screen.blit(game_over_text, game_over_rect)
            screen.blit(restart_text, restart_rect)
    
    def reset_game(self) -> None:
        """Reset the game to initial state."""
        start_x, start_y = Config.get_initial_snake_position()
        self.snake = Snake(start_x, start_y, Config.BLOCK_SIZE)
        self.food = Food(Config.BLOCK_SIZE)
        self.score = 0
        self.game_over = False
    
    def is_game_over(self) -> bool:
        """
        Check if the game is over.
        
        Returns:
            bool: True if game is over, False otherwise
        """
        return self.game_over
