ZELDA_TILES_MAP = {"g": "door",
             "+": "key",
             "A": "player",
             "1": "bat",
             "2": "spider",
             "3": "scorpion",
             "w": "solid",
             ".": "empty"}

ZELDA_CHAR_TO_INT_MAP = {
    ".": 0,
    "w": 1,
    "A": 2,
    "+": 3,
    "g": 4,
    "1": 5,
    "3": 6,
    "2": 7
}

ZELDA_INT_MAP = {
    "empty": 0,
    "solid": 1,
    "player": 2,
    "key": 3,
    "door": 4,
    "bat": 5,
    "scorpion": 6,
    "spider": 7
}

# For hashing maps to avoid duplicate goal states
ZELDA_CHAR_MAP = {"door": 'a',
            "key": 'b',
            "player": 'c',
            "bat": 'd',
            "spider": 'e',
            "scorpion": 'f',
            "solid": 'g',
            "empty": 'h'}

ZELDA_REV_TILES_MAP = { "door": "g",
                  "key": "+",
                  "player": "A",
                  "bat": "1",
                  "spider": "2",
                  "scorpion": "3",
                  "solid": "w",
                  "empty": "."}

ZELDA_TILE_TO_GRAY_SCALE_VALUE_MAP = {
    "g": 0.125,
    "+": 0.25,
    "A": 0.375,
    "1": 0.5,
    "2": 0.625,
    "3": 0.75,
    "w": 0.875,
    ".": 1.0
}


ZELDA_TILE_TO_RGB_VALUE_MAP = {
    "g": [153, 76, 0],
    "+": [255, 255, 0],
    "A": [255, 229, 204],
    "1": [0, 0, 0],
    "2": [153, 51, 255],
    "3": [255, 0, 0],
    "w": [153, 0, 0],
    ".": [192, 192, 192]
}

