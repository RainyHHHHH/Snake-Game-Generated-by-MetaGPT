"""
Snake module for the Snake Game.
Contains the Snake class that handles snake movement, growth, and collision detection.
"""

import pygame
from typing import List, Tuple
from config import Config


class Snake:
    """Snake class representing the player-controlled snake in the game."""
    
    def __init__(self, x: int, y: int, block_size: int) -> None:
        """
        Initialize the snake.
        
        Args:
            x: Initial x-coordinate of snake head
            y: Initial y-coordinate of snake head  
            block_size: Size of each snake segment block
        """
        self.body: List[Tuple[int, int]] = [(x, y)]
        self.direction: str = "RIGHT"
        self.block_size: int = block_size
        self.growth_pending: bool = False
    
    def move(self) -> None:
        """Move the snake in the current direction."""
        head_x, head_y = self.body[0]
        
        # Calculate new head position based on direction
        if self.direction == "UP":
            new_head = (head_x, head_y - self.block_size)
        elif self.direction == "DOWN":
            new_head = (head_x, head_y + self.block_size)
        elif self.direction == "LEFT":
            new_head = (head_x - self.block_size, head_y)
        elif self.direction == "RIGHT":
            new_head = (head_x + self.block_size, head_y)
        else:
            new_head = (head_x, head_y)
        
        # Add new head to the front
        self.body.insert(0, new_head)
        
        # Remove tail if not growing
        if not self.growth_pending:
            self.body.pop()
        else:
            self.growth_pending = False
    
    def grow(self) -> None:
        """Mark the snake to grow on next move."""
        self.growth_pending = True
    
    def change_direction(self, new_direction: str) -> None:
        """
        Change the snake's movement direction.
        
        Args:
            new_direction: New direction ("UP", "DOWN", "LEFT", "RIGHT")
        """
        # Prevent 180-degree turns (can't go opposite direction)
        if (new_direction == "UP" and self.direction != "DOWN") or \
           (new_direction == "DOWN" and self.direction != "UP") or \
           (new_direction == "LEFT" and self.direction != "RIGHT") or \
           (new_direction == "RIGHT" and self.direction != "LEFT"):
            self.direction = new_direction
    
    def check_collision(self, width: int, height: int) -> bool:
        """
        Check if the snake has collided with walls or itself.
        
        Args:
            width: Screen width
            height: Screen height
            
        Returns:
            bool: True if collision detected, False otherwise
        """
        head_x, head_y = self.body[0]
        
        # Check wall collision
        if (head_x < 0 or head_x >= width or 
            head_y < 0 or head_y >= height):
            return True
        
        # Check self collision (head hits body)
        # Skip the head when checking for collisions with body segments
        if self.body[0] in self.body[1:]:
            return True
        
        return False
    
    def get_head_position(self) -> Tuple[int, int]:
        """
        Get the current position of the snake's head.
        
        Returns:
            tuple: (x, y) coordinates of snake head
        """
        return self.body[0]
    
    def get_body(self) -> List[Tuple[int, int]]:
        """
        Get the entire snake body.
        
        Returns:
            list: List of (x, y) coordinates representing snake body segments
        """
        return self.body.copy()
    
    def draw(self, screen: pygame.Surface) -> None:
        """
        Draw the snake on the screen.
        
        Args:
            screen: Pygame surface to draw on
        """
        for segment in self.body:
            pygame.draw.rect(
                screen, 
                Config.SNAKE_COLOR, 
                pygame.Rect(segment[0], segment[1], self.block_size, self.block_size)
            )
