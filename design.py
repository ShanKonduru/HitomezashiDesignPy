import matplotlib.pyplot as plt
import numpy as np

def connect_dots(ax, x, y, phrase):
    dot_connections = []
    dot_index = 0
    vowels = 'aeiou'

    x_index_min = 0
    x_index_max = 50

    y_index_min = 0
    y_index_max = 50

    
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
    # Create 50x50 grid of dots
    x = np.arange(0, 50)
    y = np.arange(0, 50)
    X, Y = np.meshgrid(x, y)
        
    # Flatten the grid
    x_flat = X.flatten()
    y_flat = Y.flatten()
    
    # Random English phrase
    phrase = "The quick brown fox jumps over the lazy dog"
    
    phrase = phrase.replace(' ', '')

    # Plot the dots
    fig, ax = plt.subplots()
    ax.plot(x_flat, y_flat, 'ko', markersize=2)
    
    # Connect the dots based on the rules
    connect_dots(ax, x_flat, y_flat, phrase)
    
    ax.set_aspect('equal', 'box')
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xlim(-1, 50)
    ax.set_ylim(-1, 50)
    ax.set_facecolor('blue')  # Set background color to blue
    plt.show()