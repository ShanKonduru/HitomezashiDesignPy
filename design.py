import random
import matplotlib.pyplot as plt
import numpy as np

def get_grid_size(phrase):
    return len(phrase) + 1

def connect_dots_x_axis(ax, x_index_min, x_index_max, y, phrase):
    dot_connections = []
    dot_index = 0
    vowels = 'aeiou'
    
    for i in range(y[0], y[-1] + 1):
        char = phrase[dot_index % len(phrase)].lower()
        
        if char in vowels:
            for j in range(x_index_min, x_index_max, 2):
                dot_connections.extend([(j, i), (j+1, i)])
        else:
            for j in range(x_index_min, x_index_max, 2):
                dot_connections.extend([(j+1, i), (j+2, i)])
        
        dot_index += 1
    
    for i in range(0, len(dot_connections), 2):
        ax.plot([dot_connections[i][0], dot_connections[i+1][0]], [dot_connections[i][1], dot_connections[i+1][1]], 'w-', linewidth=0.5)
        
def connect_dots_y_axis(ax, x, y_index_min, y_index_max, phrase):
    dot_connections = []
    dot_index = 0
    vowels = 'aeiou'
    
    for i in range(x[0], x[-1] + 1):
        char = phrase[dot_index % len(phrase)].lower()
        
        if char in vowels:
            for j in range(y_index_min, y_index_max, 2):
                dot_connections.extend([(i, j), (i, j+1)])
        else:
            for j in range(y_index_min, y_index_max, 2):
                dot_connections.extend([(i, j+1), (i, j+2)])
        
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
        "The King of Kings",
        "The Queen of My Heart",
        "Shan Konduru",
        "Ravi Bhushan Sarma Konduru",
        "Indu Kiran Konduru",
        "Sri Kari Sarma Konduru",
        "Trinaaga Sri Kari sarma Konduru",
        "Ohm Namah Shivaya",
        "Ohm Gam Ganapathaye Namaha",
        "Sri Matre Namaha"
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
        
        filename = y_phrase + '.jpeg'
        
        # Adjust the phrase length to match the grid size
        while len(y_phrase) < GRID_SIZE:
            y_phrase += original_phrase.replace(' ', '')
        
        y_phrase = y_phrase[:GRID_SIZE]  # Trim the phrase to match the grid size
        
        # Plot the dots
        fig, ax = plt.subplots()
        ax.plot(x, y, 'ko', markersize=1)  # Reduced dot size
        connect_dots_y_axis(ax, x, 0, GRID_SIZE, y_phrase)
        connect_dots_x_axis(ax, 0, GRID_SIZE, y, y_phrase)
        
        ax.set_aspect('equal', 'box')
        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_xlim(-1, GRID_SIZE)
        ax.set_ylim(-1, GRID_SIZE)
        ax.set_facecolor('blue')
        
        plt.savefig(f'./Output/{filename}')
