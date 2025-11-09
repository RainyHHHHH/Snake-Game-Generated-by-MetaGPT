"""
Food module for the Snake Game.
Contains the Food class that handles food generation, positioning, and drawing.
"""

import pygame
import random
from typing import Tuple
from config import Config


class Food:
    """Food class representing the food that the snake can eat."""
    
    def __init__(self, block_size: int) -> None:
        """
        Initialize the food.
        
        Args:
            block_size: Size of the food block
        """
        self.block_size: int = block_size
        self.x: int = 0
        self.y: int = 0
        self.generate_new_position(Config.SCREEN_WIDTH, Config.SCREEN_HEIGHT)
    
    def generate_new_position(self, width: int, height: int) -> None:
        """
        Generate a new random position for the food within the game boundaries.
        
        Args:
            width: Screen width
            height: Screen height
        """
        # Calculate maximum grid positions
        max_x = (width // self.block_size) - 1
        max_y = (height // self.block_size) - 1
        
        # Generate random grid position
        grid_x = random.randint(0, max_x)
        grid_y = random.randint(0, max_y)
        
        # Convert grid position to pixel position
        self.x = grid_x * self.block_size
        self.y = grid_y * self.block_size
    
    def get_position(self) -> Tuple[int, int]:
        """
        Get the current position of the food.
        
        Returns:
            tuple: (x, y) coordinates of food
        """
        return (self.x, self.y)
    
    def draw(self, screen: pygame.Surface) -> None:
        """
        Draw the food on the screen.
        
        Args:
            screen: Pygame surface to draw on
        """
        pygame.draw.rect(
            screen,
            Config.FOOD_COLOR,
            pygame.Rect(self.x, self.y, self.block_size, self.block_size)
        )
