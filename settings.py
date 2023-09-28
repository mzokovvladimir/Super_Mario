import os

# mario.py
WIN_WIDTH: int, WIN_HEIGHT: int = 800, 640
DISPLAY: tuple = (WIN_WIDTH, WIN_HEIGHT)
BACKGROUND_COLOR: str = '#000000'
FPS: int = 60
SCREEN_START: tuple = (0, 0)
FILE_DIR: str = os.path.dirname(__file__)
FILE_PATH: str = '%s/levels/1.txt' % FILE_DIR
MUSIC_PATH: str = 'audio/level_music.wav'

# monsters.py
MONSTER_WIDTH: int, MONSTER_HEIGHT: int, MONSTER_COLOR: str = 32, 32, '#2111FF'
ICON_DIR: str = os.path.dirname(__file__)
ANIMATION_MONSTER_HORIZONTAL: list[tuple[str]] = [('%s/monsters/fire1.png' % ICON_DIR), ('%s/monsters/fire2.png' % ICON_DIR)]

# blocks.py
PLATFORM_WIDTH: int, PLATFORM_HEIGHT: int, PLATFORM_COLOR: str = 32, 32, '#000000'
# ICON_DIR: str = os.path.dirname(__file__)
ANIMATION_BLOCK_TELEPORT: list[tuple[str]] = [('%s/blocks/portal1.png' % ICON_DIR), ('%s/blocks/portal2.png' % ICON_DIR)]
ANIMATION_PRINCESS: list[tuple[str]] = [('%s/blocks/princess_l.png' % ICON_DIR), ('%s/blocks/princess_r.png' % ICON_DIR)]
PATH_BLOCK_PLATFORM: str = '%s/blocks/platform.png' % ICON_DIR
PATH_BLOCK_DIE: str = '%s/blocks/dieBlock.png' % ICON_DIR

# player.py
MOVE_SPEED: int = 7
MOVE_EXTRA_SPEED: float = 2.5
WIDTH: int, HEIGHT: int, COLOR: str = 22, 32, '#888888'
JUMP_POWER: int, JUMP_EXTRA_POWER: int, GRAVITY: float = 10, 1, 0.25
ANIMATION_DELAY: float, ANIMATION_SUPER_SPEED_DELAY: float = 0.1, 0.05

PLATFORM_IMAGE: str = "%s/blocks/platform.png" % ICON_DIR

ANIMATION_LEFT: list[tuple[str]] = [('%s/mario/l1.png' % ICON_DIR),
                  ('%s/mario/l2.png' % ICON_DIR),
                  ('%s/mario/l3.png' % ICON_DIR),
                  ('%s/mario/l4.png' % ICON_DIR),
                  ('%s/mario/l5.png' % ICON_DIR)
                  ]

ANIMATION_RIGHT: list[tuple[str]] = [('%s/mario/r1.png' % ICON_DIR),
                   ('%s/mario/r2.png' % ICON_DIR),
                   ('%s/mario/r3.png' % ICON_DIR),
                   ('%s/mario/r4.png' % ICON_DIR),
                   ('%s/mario/r5.png' % ICON_DIR)
                   ]

ANIMATION_JUMP: list[tuple[str]] = [('%s/mario/j.png' % ICON_DIR, ANIMATION_DELAY)]
ANIMATION_JUMP_LEFT: list[tuple[str]] = [('%s/mario/jl.png' % ICON_DIR, ANIMATION_DELAY)]
ANIMATION_JUMP_RIGHT: list[tuple[str]] = [('%s/mario/jr.png' % ICON_DIR, ANIMATION_DELAY)]
ANIMATION_STAY: list[tuple[str]] = [('%s/mario/0.png' % ICON_DIR, ANIMATION_DELAY)]

# pyganim.py
PLAYING: str, PAUSED: str, STOPPED: str = 'playing', 'paused', 'stopped'
# Ці значення використовуються в методі anchor().
NORTH: str, SOUTH: str, WEST: str, EAST: str, CENTER: str = 'north', 'south', 'west', 'east', 'center'
NORTH_WEST: str, SOUTH_WEST: str, NORTH_EAST: str, SOUTH_EAST: str = 'northwest', 'southwest', 'northeast', 'southeast'
