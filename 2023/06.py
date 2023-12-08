races = """Time:        62649190
Distance:   553101014731074"""

import re
import numpy as np
from tqdm import tqdm

times = [int(i) for i in re.findall("\d+", races.split("\n")[0])]
distances = [int(i) for i in re.findall("\d+", races.split("\n")[1])]

ways_to_win = [0] * len(times)
for race, time_allowed in enumerate(times):
    for loading_time in tqdm(range(1, time_allowed)):
        speed = loading_time
        distance = (time_allowed - loading_time) * speed
        if distance > distances[race]:
            ways_to_win[race] += 1

print(ways_to_win)


print(np.prod(ways_to_win))
