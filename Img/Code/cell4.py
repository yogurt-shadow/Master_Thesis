import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from math import sqrt

if __name__ == "__main__":
    # Define grid
    x = np.arange(-3, 3, 0.01)
    y = np.arange(-1, 3, 0.01)
    X, Y = np.meshgrid(x, y)

    # Define circle equations
    Z1 = (X - 1)**2 + (Y - 1)**2 - 3  # Circle centered at (1, 1)
    Z2 = (X + 1)**2 + (Y - 1)**2 - 3  # Circle centered at (-1, 1)

    # Plot the contours of both circles
    plt.contour(X, Y, Z1, levels=[0], colors='black')  # Circle 1 contour
    plt.contour(X, Y, Z2, levels=[0], colors='black')   # Circle 2 contour

    # Set axis properties
    plt.axis('equal')
    plt.yticks([0])
    plt.xticks([])

    ax = plt.gca()
    ax.spines['top'].set_color('none')
    ax.spines['right'].set_color('none')
    ax.spines['left'].set_color('none')
    ax.spines['bottom'].set_color('none')
    ax.spines['left'].set_position(('data', 0))
    ax.spines['bottom'].set_position(('data', 0))

    # Add arrows for axes
    ax.annotate('', xy=(3.4, 0), xytext=(-3.4, 0), arrowprops=dict(arrowstyle="->", lw=1.5))
    ax.annotate('', xy=(0, 3.3), xytext=(0, -0.8), arrowprops=dict(arrowstyle="->", lw=1.5))

    # Add axis labels
    plt.text(2.9, -0.2, 'x', fontsize=12)
    plt.text(-0.2, 2.9, 'y', fontsize=12)

    # Set plot range
    plt.xlim(-3.5, 3.5)
    plt.ylim(-1, 3.2)
    plt.xticks([-3, -2, -1, 1, 3])

    # draw points
    points = [
        [-3, 0], [-1-sqrt(2), 0], [-1, 0], [1-sqrt(2), 0], [0, 0], [sqrt(2)-1, 0], [1, 0], [sqrt(2)+1, 0], [3, 0]
    ]
    for point in points:
        plt.plot(point[0], point[1], 'ko', markersize=5)


    points2 = [
        [-1-sqrt(2), -1], [-1-sqrt(2), 1], [-1-sqrt(2), 2], [-1-sqrt(2), 3],
        [-1, -1], [-1, 1-sqrt(3)], [-1, 1+sqrt(3)], [-1, 3],
        [1-sqrt(2), -1], [1-sqrt(2), -0.8], [1-sqrt(2), -0.63], [1-sqrt(2), 1], [1-sqrt(2), 2], [1-sqrt(2), 2.5], [1-sqrt(2), 2.63], [1-sqrt(2), 3],
        [0, -1], [0, 1-sqrt(2)], [0, 1+sqrt(2)], [0, 3],
        [sqrt(2)-1, -1], [sqrt(2)-1, -0.8], [sqrt(2)-1, -0.63], [sqrt(2)-1, 1], [sqrt(2)-1, 2], [sqrt(2)-1, 2.5], [sqrt(2)-1, 2.63], [sqrt(2)-1, 3],
        [1, -1], [1, 1-sqrt(3)], [1, 1+sqrt(3)], [1, 3],
        [sqrt(2)+1, -1], [sqrt(2)+1, 1], [sqrt(2)+1, 2], [sqrt(2)+1, 3]
    ]
    # draw hollow p
    for point in points2:
        plt.plot(point[0], point[1], 'ko', markersize=5, markerfacecolor='none')

    # Add notes for the circles
    plt.text(1, 3, '$(x - 1)^2 + (y - 1)^2 = 3$', fontsize=12)
    plt.text(-2.5, 3, '$(x + 1)^2 + (y - 1)^2 = 3$', fontsize=12)

    # Save plot
    plt.savefig('Code/cell4.png', transparent=False)
