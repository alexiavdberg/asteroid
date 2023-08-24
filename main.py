from if3_game.engine import init, Game, Layer
from game_objects import RESOLUTION, Spaceship, Asteroid

init(RESOLUTION, "Asteroid !!!")

game = Game()
game_layer = Layer()
game.add(game_layer)

spaceship = Spaceship((400, 300))
game_layer.add(spaceship)

missile = Asteroid((200, 200), (-150, 30))
game_layer.add(missile)

# --- LAST LINE --- #

game.run()