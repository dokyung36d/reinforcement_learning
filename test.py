import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

SPRITE_SCALING_COIN = 2
SPRITE_SCALING_PLAYER = 0.2
COIN_COUNT = 50

coin = arcade.Sprite("coin_01.png", SPRITE_SCALING_COIN)

class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Create the sprite lists
        self.player_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()

        # Score
        self.score = 0

        # Set up the player
        # Character image from kenney.nl
        self.player_sprite = arcade.Sprite("character.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50 # Starting position
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        # Create the coins
        for i in range(COIN_COUNT):

            # Create the coin instance
            # Coin image from kenney.nl
            coin = arcade.Sprite("coin_01.png", SPRITE_SCALING_COIN)

            coin.height = 200
            coin.width = 200

            # Position the coin
            # coin.center_x = random.randrange(1, SCREEN_WIDTH / 2)
            # coin.center_y = random.randrange(1, SCREEN_HEIGHT / 2)

            # Add the coin to the lists
            self.coin_list.append(coin)

    def on_draw(self):
        """ Render the screen. """
        arcade.start_render()
        # Your drawing code goes here
        self.coin_list.draw()
        self.player_list.draw()

    def update(self, delta_time):
        """ All the logic to move, and the game logic goes here. """
        pass


def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()