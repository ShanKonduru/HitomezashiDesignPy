import matplotlib.pyplot as plt
import numpy as np

def connect_dots(ax, x, y, phrase):
    dot_connections = []
    dot_index = 0
    vowels = 'aeiou'
    
    for i in range(min(len(y), len(phrase))):
        char = phrase[dot_index % len(phrase)].lower()
        
        if char in vowels:
            if i + 1 < len(y):
                dot_connections.extend([(x[i], y[i]), (x[i], y[i + 1])])
        else:
            if i + 1 < len(y):
                dot_connections.extend([(x[i], y[i]), (x[i], y[i + 1])])
        
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
    
    # Plot the dots
    fig, ax = plt.subplots()
    ax.plot(x_flat, y_flat, 'ko', markersize=2)
    
    # Connect the dots based on the rules
    # connect_dots(ax, x_flat, y_flat, phrase)
    
    ax.set_aspect('equal', 'box')
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xlim(-1, 50)
    ax.set_ylim(-1, 50)
    ax.set_facecolor('blue')  # Set background color to blue
    plt.show()