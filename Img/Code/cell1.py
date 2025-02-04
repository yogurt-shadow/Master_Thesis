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
    ax.annotate('', xy=(3, 0), xytext=(-3, 0), arrowprops=dict(arrowstyle="->", lw=1.5))
    ax.annotate('', xy=(0, 3.3), xytext=(0, -0.8), arrowprops=dict(arrowstyle="->", lw=1.5))

    # Add axis labels
    plt.text(2.9, -0.2, 'x', fontsize=12)
    plt.text(-0.2, 2.9, 'y', fontsize=12)

    inter_x = np.arange(1 - sqrt(3), -1 + sqrt(3), 0.01)
    # inter_y1 should be empty np
    inter_y1 = np.zeros(len(inter_x))
    inter_y2 = np.zeros(len(inter_x))

    for i in range(len(inter_x)):
        curr_y = [sqrt(3 - (inter_x[i] - 1)**2) + 1, -sqrt(3 - (inter_x[i] - 1)**2) + 1, sqrt(3 - (inter_x[i] + 1)**2) + 1, -sqrt(3 - (inter_x[i] + 1)**2) + 1]
        curr_y.sort()
        inter_y1[i] = curr_y[1]
        inter_y2[i] = curr_y[2]

    plt.fill_between(inter_x, inter_y1, inter_y2, hatch='//', alpha=0.5)

    # Set plot range
    plt.xlim(-3.2, 3.2)
    plt.ylim(-1, 3.2)

    # Add notes for the circles
    plt.text(1, 3, '$(x - 1)^2 + (y - 1)^2 = 3$', fontsize=12)
    plt.text(-2.5, 3, '$(x + 1)^2 + (y - 1)^2 = 3$', fontsize=12)

    # Save plot
    plt.savefig('Code/cell1.png', transparent=False)
