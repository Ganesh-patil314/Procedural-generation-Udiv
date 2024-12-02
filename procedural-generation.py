import random

# Define constants
WIDTH = 120  # Width of the dungeon
HEIGHT = 50  # Height of the dungeon
WALL = '#'
EMPTY = ' '

# Dungeon grid initialization
dungeon = [[WALL for _ in range(WIDTH)] for _ in range(HEIGHT)]

def generate_room(x, y, room_width, room_height):
    """Generate a rectangular room with walls."""
    for i in range(y, y + room_height):
        for j in range(x, x + room_width):
            if 0 <= i < HEIGHT and 0 <= j < WIDTH:
                dungeon[i][j] = EMPTY

def create_corridor(x1, y1, x2, y2):
    """Create a corridor between two points."""
    if random.choice([True, False]):
        # Horizontal corridor first
        for x in range(min(x1, x2), max(x1, x2) + 1):
            if 0 <= y1 < HEIGHT and 0 <= x < WIDTH:
                dungeon[y1][x] = EMPTY
        # Then vertical corridor
        for y in range(min(y1, y2), max(y1, y2) + 1):
            if 0 <= y < HEIGHT and 0 <= x2 < WIDTH:
                dungeon[y][x2] = EMPTY
    else:
        # Vertical corridor first
        for y in range(min(y1, y2), max(y1, y2) + 1):
            if 0 <= x1 < WIDTH and 0 <= y < HEIGHT:
                dungeon[y][x1] = EMPTY
        # Then horizontal corridor
        for x in range(min(x1, x2), max(x1, x2) + 1):
            if 0 <= y2 < HEIGHT and 0 <= x < WIDTH:
                dungeon[y2][x] = EMPTY

def generate_dungeon():
    """Main dungeon generation function."""
    rooms = []
    for _ in range(10):  # Attempt to create 10 rooms
        room_width = random.randint(5, 10)
        room_height = random.randint(5, 10)
        x = random.randint(1, WIDTH - room_width - 1)
        y = random.randint(1, HEIGHT - room_height - 1)
        
        # Check if room intersects with existing rooms
        overlap = False
        for room in rooms:
            rx, ry, rw, rh = room
            if not (x + room_width < rx or x > rx + rw or y + room_height < ry or y > ry + rh):
                overlap = True
                break

        if not overlap:
            generate_room(x, y, room_width, room_height)
            rooms.append((x, y, room_width, room_height))

    # Create corridors between rooms
    for i in range(1, len(rooms)):
        x1, y1, _, _ = rooms[i - 1]
        x2, y2, _, _ = rooms[i]
        create_corridor(x1, y1, x2, y2)

def print_dungeon():
    """Print the dungeon to the terminal."""
    for row in dungeon:
        print(''.join(row))

# Generate and print the dungeon
generate_dungeon()
print_dungeon()

