"""
Configuration module for the Snake Game.
Contains all game constants and configuration parameters.
"""


class Config:
    """Game configuration constants."""
    
    # Screen dimensions
    SCREEN_WIDTH: int = 800
    SCREEN_HEIGHT: int = 600
    
    # Game block size
    BLOCK_SIZE: int = 20
    
    # Game frame rate
    FPS: int = 10
    
    # Colors (RGB)
    BACKGROUND_COLOR: tuple = (0, 0, 0)
    SNAKE_COLOR: tuple = (0, 255, 0)
    FOOD_COLOR: tuple = (255, 0, 0)
    TEXT_COLOR: tuple = (255, 255, 255)
    
    # Initial snake position (centered on screen)
    @classmethod
    def get_initial_snake_position(cls) -> tuple:
        """Get the initial snake position centered on the screen."""
        center_x = (cls.SCREEN_WIDTH // cls.BLOCK_SIZE) // 2 * cls.BLOCK_SIZE
        center_y = (cls.SCREEN_HEIGHT // cls.BLOCK_SIZE) // 2 * cls.BLOCK_SIZE
        return center_x, center_y
