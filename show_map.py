import os
from gym_pcgrl.envs.probs.zelda_prob import ZeldaProblem
from gym_pcgrl.envs.probs.ddave_prob import DDaveProblem
from gym_pcgrl.envs.reps.narrow_rep import NarrowRepresentation
from gym.envs.classic_control import rendering
from gym_pcgrl.envs.reps import REPRESENTATIONS
from gym_pcgrl.envs.pcgrl_env import PcgrlEnv
from PIL import Image

import numpy as np
import random
import csv
import time
import random


TILES_MAP = {"g": "door",
             "+": "key",
             "A": "player",
             "1": "bat",
             "2": "spider",
             "3": "scorpion",
             "w": "solid",
             ".": "empty"}
#
# TILES_MAP = {"g": "door",
#              "+": "key",
#              "A": "player",
#              "1": "bat",
#              "2": "spider",
#              "3": "scorpion",
#              "w": "solid",
#              ".": "empty"}
#
# INT_MAP = {
#     "empty": 0,
#     "solid": 1,
#     "player": 2,
#     "key": 3,
#     "door": 4,
#     "bat": 5,
#     "scorpion": 6,
#     "spider": 7
# }
#
# # For hashing maps to avoid duplicate goal states
# CHAR_MAP = {"door": 'a',
#             "key": 'b',
#             "player": 'c',
#             "bat": 'd',
#             "spider": 'e',
#             "scorpion": 'f',
#             "solid": 'g',
#             "empty": 'h'}


# gameCharacters = " #@H$V*"
gameCharacters = '.wA+g132'
REV_TILES_MAP = dict((s, gameCharacters[i]) for i, s in enumerate(["empty", "solid", "player", "key", "door", "bat", "scorpion", "spider"]))
print(REV_TILES_MAP)

# Reverse the k,v in TILES MAP for persisting back as char map .txt format
# REV_TILES_MAP = {"door": "g",
#                   "key": "+",
#                   "player": "A",
#                   "bat": "1",
#                   "spider": "2",
#                   "scorpion": "3",
#                   "solid": "w",
#                   "empty": "."}


TILES_MAP = {v:k for k,v in REV_TILES_MAP.items()}

print(TILES_MAP)
# TILES_MAP = {"g": "door",
#              "+": "key",
#              "A": "player",
#              "1": "bat",
#              "2": "spider",
#              "3": "scorpion",
#              "w": "solid",
#              ".": "empty"}

INT_MAP = {k[0]: i for i,k in enumerate(REV_TILES_MAP.items())}
print(INT_MAP)
# INT_MAP = {
#     "empty": 0,
#     "solid": 1,
#     "player": 2,
#     "key": 3,
#     "door": 4,
#     "bat": 5,
#     "scorpion": 6,
#     "spider": 7
# }



# Reads in .txt playable map and converts it to string[][]
def to_2d_array_level(file_name):
    level = []

    with open(file_name, 'r') as f:
        rows = f.readlines()
        for row in rows:
            new_row = []
            for char in row:
                if char != '\n':
                    new_row.append(TILES_MAP[char])
            level.append(new_row)

    # Remove the border
    truncated_level = level[1: len(level) - 1]
    level = []
    for row in truncated_level:
        new_row = row[1: len(row) - 1]
        level.append(new_row)
    return level


# Converts from string[][] to 2d int[][]
def int_arr_from_str_arr(map):
    int_map = []
    for row_idx in range(len(map)):
        new_row = []
        for col_idx in range(len(map[0])):
            new_row.append(INT_MAP[map[row_idx][col_idx]])
        int_map.append(new_row)
    return int_map


def str_arr_from_int_arr(map):
    translation_map = {v:k for k,v in INT_MAP.items()}
    str_map = []
    for row_idx in range(len(map)):
        new_row = []
        for col_idx in range(len(map[0])):
            new_row.append(translation_map[map[row_idx][col_idx]])
        str_map.append(new_row)
    # print(str_map)
    return str_map


def int_map_to_onehot(int_map):
    new_map = []
    for row_i in range(len(int_map)):
        new_row = []
        for col_i in range(len(int_map[0])):
            new_tile = [0]*8
            new_tile[int_map[row_i][col_i]] = 1
            new_row.append(new_tile)
        new_map.append(new_row)
    return new_map

"""Start with random map"""
def gen_random_map(random, width, height, prob):
    map = random.choice(list(prob.keys()),size=(height,width),p=list(prob.values())).astype(np.uint8)
    return map


# This code is for generating the maps
def render_map(map, prob, rep, filename='', ret_image=False):
    # format image of map for rendering
    if not filename:
        img = prob.render(map)
    else:
        img = to_2d_array_level(filename)
    img = rep.render(img, tile_size=32, border_size=(1, 1)).convert("RGB")
    # img = np.array(img)
    if ret_image:
        return img
    else:
        ren = rendering.SimpleImageViewer()
        ren.imshow(img)
        input(f'')
        time.sleep(0.3)
        ren.close()


actions_list = [act for act in list(TILES_MAP.values())]
prob = ZeldaProblem()
rep = NarrowRepresentation()
rep._x = 0
rep._y = 0


def pixel_map_to_image_map(pixel_map):
    for row in pixel_map:
        for rgb in row:
            print(rgb)
    # get_closest_pixel()


for i in os.listdir("/Users/matt/gym_pcgrl/gym-pcgrl/playable_maps"):
    playable_map = to_2d_array_level(f'/Users/matt/gym_pcgrl/gym-pcgrl/playable_maps/{i}')
    img = render_map(np.array(playable_map), prob, rep, filename="", ret_image=True)
    img.save(f"zelda_playable_map_imgs/{i.split('.txt')[0]}.png")

# swap 3 with 5