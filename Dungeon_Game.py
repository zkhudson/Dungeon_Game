#Create a game with a 2-dimensional map. Place the player, a door, and a monster into random spots in your map.
# Let the player move around in the map and, after each move, tell them if they've found the door or the monster.
# If they find either the game is over. The door is the win condition, the monster is the lose condition.

import random

# map code (a list of coordinates) - this is a constant
CELLS = [(0, 0), (1, 0), (2, 0),
         (0, 1), (1, 1), (2, 1),
         (0, 2), (1, 2), (2, 2)]


def get_locations():
    player = random.choice(CELLS)
    monster = random.choice(CELLS)
    door = random.choice(CELLS)

    if player == monster or monster == door or door == player:
        return get_locations()

    return player, monster, door

def move_player(player, move):
    #Take player location and adjust location based on move
    #check if spot is monster/door and if neither save player location
    x, y = player

    if move == 'LEFT':
        x -= 1
    elif move == 'RIGHT':
        x += 1
    elif move == 'UP':
        y -= 1
    elif move == 'DOWN':
        y += 1

    return x, y

def get_moves(player):
    #player = (x,y)
    #         [0,1]
    moves = ['LEFT', 'RIGHT', 'UP','DOWN']

    if player[0] == 0:
        moves.remove('LEFT')
    if player[0] == 2:
        moves.remove('RIGHT')
    if player[1] == 0:
        moves.remove('UP')
    if player[1] == 2:
        moves.remove('DOWN')

    return moves

def draw_map(player):
  print(' _ _ _')
  tile = '|{}'
  for idx, cell in enumerate(CELLS):
    if idx in [0, 1, 3, 4, 6, 7]:
      if cell == player:
        print(tile.format('X'), end='')
      else:
        print(tile.format('_'), end='')
    else:
      if cell == player:
        print(tile.format('X|'))
      else:
        print(tile.format('_|'))

monster, player, door = get_locations()
print('Welcome to the dungeon...')
print('To stop playing type QUIT')

while True:
    moves = get_moves(player)

    print('You are currently located at {}'.format(player)) #Display current player location

    draw_map(player)

    print('You can move {}'.format(moves)) #Show available moves
    print('Which direction should you move?')

    move = input('> ')
    move = move.upper()
    if move == 'QUIT':
        break
    if move in moves:
        player = move_player(player, move)
    else:
        print("You can't move that direction! Try again.")
        continue

    if player == door:
        print('You WIN!')
        break
    elif player == monster:
        print('You Lost')
        break



