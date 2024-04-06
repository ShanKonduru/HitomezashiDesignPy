import random
import matplotlib.pyplot as plt
import numpy as np

import consts

def get_grid_size(phrase):
    return len(phrase) + 1

def connect_dots_x_axis(ax, x, y, phrase):
    dot_connections = []
    dot_index = 0
    vowels = 'aeiou'
    print(f"X-Axis Phrase {phrase}")

    x_index_min = 0
    x_index_max = get_grid_size(phrase)

    y_index_min = 0
    y_index_max = get_grid_size(phrase)

    for i in range(y_index_min, len(phrase)):
        char = phrase[dot_index % len(phrase)].lower()
        px = x_index_min
        py = i

        if char in vowels:
            for j in range(x_index_min, x_index_max, 2):
                px = j
                dot_connections.extend([(px, py), (px+1, py)])
        else:
            for j in range(x_index_min, x_index_max, 2):
                px = j
                dot_connections.extend([(px+1, py), (px+2, py)])
        dot_index += 1
    
    for i in range(0, len(dot_connections), 2):
        ax.plot([dot_connections[i][0], dot_connections[i+1][0]], [dot_connections[i][1], dot_connections[i+1][1]], 'w-', linewidth=0.5)
        
def connect_dots_y_axis(ax, x, y, phrase):
    dot_connections = []
    dot_index = 0
    vowels = 'aeiou'
    print(f" Y-Axis Phrase {phrase}")

    x_index_min = 0
    x_index_max = get_grid_size(phrase)

    y_index_min = 0
    y_index_max = get_grid_size(phrase)

    for i in range(x_index_min, len(phrase)):
        char = phrase[dot_index % len(phrase)].lower()
        px = i
        py = y_index_min

        if char in vowels:
            for j in range(y_index_min, y_index_max, 2):
                py = j
                dot_connections.extend([(px, py), (px, py+1)])
        else:
            for j in range(y_index_min, y_index_max, 2):
                py = j
                dot_connections.extend([(px, py+1), (px, py+2)])
        dot_index += 1
    
    for i in range(0, len(dot_connections), 2):
        ax.plot([dot_connections[i][0], dot_connections[i+1][0]], [dot_connections[i][1], dot_connections[i+1][1]], 'w-', linewidth=0.5)
        
if __name__ == '__main__':

    phrases = [
        "The quick brown fox jumps over the lazy dog",
        "A stitch in time saves nine",
        "Beauty is in the eye of the beholder",
        "Actions speak louder than words",
        "Don't count your chickens before they hatch",
        "Every cloud has a silver lining",
        "Fortune favors the bold",
        "Good things come to those who wait",
        "Honesty is the best policy",
        "It's a piece of cake",
        "aeiou"
    ]

    for my_phrase in phrases:
        print(my_phrase)
        # Random English phrase
        original_phrase = my_phrase
        y_phrase = original_phrase.replace(' ', '')
        GRID_SIZE = get_grid_size(y_phrase)
        # Create 50x50 grid of dots
        x = np.arange(0, GRID_SIZE)
        y = np.arange(0, GRID_SIZE)
        X, Y = np.meshgrid(x, y)
            
        # Flatten the grid
        x_flat = X.flatten()
        y_flat = Y.flatten()

        filename = y_phrase + '.jpeg'

        # Adjust the phrase length to match the grid size
        while len(y_phrase) < GRID_SIZE:
            y_phrase += original_phrase.replace(' ', '')
        
        y_phrase = y_phrase[:GRID_SIZE]  # Trim the phrase to match the grid size
    
        # Plot the dots
        fig, ax = plt.subplots()
        ax.plot(x_flat, y_flat, 'ko', markersize=2)
        
        # Connect the dots based on the rules along y axis
        connect_dots_y_axis(ax, x_flat, y_flat, y_phrase)

        x_phrase = y_phrase # random.choice(phrases)

        # Connect the dots based on the rules along x axis
        connect_dots_x_axis(ax, x_flat, y_flat, x_phrase)

        ax.set_aspect('equal', 'box')
        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_xlim(-1, GRID_SIZE)
        ax.set_ylim(-1, GRID_SIZE)
        ax.set_facecolor('blue')  # Set background color to blue
        plt.savefig(f'./Output/{filename}')
        # plt.show()
