import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from math import sqrt

if __name__ == "__main__":
    # draw x = 2*y^2 - 2, x = -2*y^2 + 2
    y = np.arange(-1.5, 1.5, 0.01)
    x1 = 2*y**2 - 2
    x2 = -2*y**2 + 2
    plt.plot(x1, y, 'k')
    plt.plot(x2, y, 'k')


    # Set axis properties
    plt.axis('equal')
    plt.yticks([])
    plt.xticks([])

    ax = plt.gca()
    ax.spines['top'].set_color('none')
    ax.spines['right'].set_color('none')
    ax.spines['left'].set_position(('data', 0))
    ax.spines['bottom'].set_position(('data', 0))

    # Add arrows for axes
    # ax.annotate('', xy=(2.8, 0), xytext=(-2.8, 0), arrowprops=dict(arrowstyle="->", lw=1.5))
    # ax.annotate('', xy=(0, 2), xytext=(0, -2), arrowprops=dict(arrowstyle="->", lw=1.5))

    # Add axis labels
    plt.text(2.9, 0.2, 'x', fontsize=12)
    plt.text(-0.2, 2.4, 'y', fontsize=12)

    # Set plot range
    plt.xlim(-2.4, 2.4)
    plt.ylim(-2.1, 2.1)
    plt.xticks([-3, -2, -1, 0, 1, 2, 3])

    # Save plot
    plt.savefig('Code/cad.png', transparent=False)
