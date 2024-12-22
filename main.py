import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np

# Coordinates for the letters
coordinates = {
    "F": [(1, 6), (1, 5), (1, 4), (1, 3), (1, 2), (2, 6), (2, 4)],
    "E": [(4, 6), (4, 5), (4, 4), (4, 3), (4, 2), (5, 6), (5, 4), (5, 2)],
    "L": [(7, 6), (7, 5), (7, 4), (7, 3), (7, 2), (8, 2)],
    "I": [(10, 6), (10, 5), (10, 4), (10, 3), (10, 2)],
    "Z": [
        (12, 6),
        (13, 6),
        (14, 6),
        (15, 6),
        (12, 2),
        (13, 2),
        (14, 2),
        (15, 2),
        (14, 5),
        (13, 4),
        (12, 3),
    ],
    "N": [
        (17, 6),
        (17, 5),
        (17, 4),
        (17, 3),
        (17, 2),
        (18, 5),
        (19, 4),
        (20, 6),
        (20, 5),
        (20, 4),
        (20, 3),
        (20, 2),
    ],
    "A": [
        (22, 6),
        (22, 5),
        (22, 4),
        (22, 3),
        (22, 2),
        (23, 6),
        (24, 6),
        (25, 6),
        (25, 5),
        (25, 4),
        (25, 3),
        (25, 2),
        (23, 4),
        (24, 4),
    ],
    "T": [(27, 6), (28, 6), (29, 6), (28, 5), (28, 4), (28, 3), (28, 2)],
    "A_2": [
        (31, 6),
        (31, 5),
        (31, 4),
        (31, 3),
        (31, 2),
        (32, 6),
        (33, 6),
        (34, 6),
        (34, 5),
        (34, 4),
        (34, 3),
        (34, 2),
        (32, 4),
        (33, 4),
    ],
    "L_2": [(36, 6), (36, 5), (36, 4), (36, 3), (36, 2), (37, 2)],
}

all_points = [point for letter in coordinates.values() for point in letter]

# Initialize plot
fig, ax = plt.subplots(figsize=(7, 2))
ax.set(xlim=[0, 39], ylim=[0, 7])
scat = ax.scatter([], [], color="red", s=100)


# Update function for each frame
def update(frame):
    x, y = zip(*all_points[: frame + 1])
    data = np.stack([x, y]).T
    scat.set_offsets(data)
    return [scat]


ani = animation.FuncAnimation(
    fig,
    update,
    frames=len(all_points),
    blit=True,
    interval=40,
)

plt.show()
