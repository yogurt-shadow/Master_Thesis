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

    plt.text(2, 1.5, '$x = 2y^2 - 2$', fontsize=12)
    plt.text(-2, 1.5, '$x = -2y^2 + 2$', fontsize=12)

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

    # draw dashed lines
    plt.plot([-2, -2], [-2, 2], 'k--')
    plt.plot([2, 2], [-2, 2], 'k--')
    # denote symbols
    plt.text(-2.4, 1.7, '$C_1$', fontsize=15)
    plt.text(-2.4, 0, '$C_2$', fontsize=15)
    plt.text(-2.4, -1.7, '$C_3$', fontsize=15)
    plt.text(-1, 1.7, '$C_4$', fontsize=15)
    plt.text(-1, 0.9, '$C_5$', fontsize=15)
    plt.text(-1, 0, '$C_6$', fontsize=15)
    plt.text(-1, -1, '$C_7$', fontsize=15)
    plt.text(-1, -1.7, '$C_8$', fontsize=15)
    plt.text(1, 1.7, '$C_9$', fontsize=15)
    plt.text(1, 0.9, '$C_{10}$', fontsize=15)
    plt.text(1, 0, '$C_{11}$', fontsize=15)
    plt.text(1, -1, '$C_{12}$', fontsize=15)
    plt.text(1, -1.7, '$C_{13}$', fontsize=15)
    plt.text(2.4, 1.7, '$C_{14}$', fontsize=15)
    plt.text(2.4, 0, '$C_{15}$', fontsize=15)
    plt.text(2.4, -1.7, '$C_{16}$', fontsize=15)

    # Save plot
    plt.savefig('Code/img/cad.png', transparent=False)
