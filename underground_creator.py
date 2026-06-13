from random import randint

def create_map(w: int, h: int) -> list:
    return [[0 for i in range(w)] for j in range(h)]

def create_room(game_map:list) -> tuple:
    w, h = len(game_map[0]), len(game_map)
    room = [randint(0,w//2-1),randint(0,h//2-1)]
    for i in range(2):
        room_x2_y2 = room[i] 
        new_value = randint(room_x2_y2,w - room_x2_y2)
        room.append(new_value)
    return room

def create_rooms(game_map: list, tries:int = 3) -> list:
    return [tuple(create_room(game_map)) for i in range(tries)]
    
def add_room_to_map(game_map: list, *args: int) -> None:
    """*args = x1, y1, x2, y2"""
    x1, y1, x2, y2 = args
    for i in range(x1,x1+x2):
        for j in range(y1,y1+y2):
            game_map[i][j] = 1
def add_rooms_to_map(game_map:list, rooms: list) -> None:
    for room in rooms: add_room_to_map(game_map, *room) 

#game = create_map(25,25)
#rooms = create_rooms(game)
#add_rooms_to_map(game, rooms)
#for i in game: print(i, sep='\n')

# Не доделано, нужна проверка на столкновения комнат