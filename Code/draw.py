# draw (x - 1)^2 + (y - 1)^2 = 3
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-3, 4, 0.01)
y = np.arange(-1.2, 6, 0.01)
X, Y = np.meshgrid(x, y)
Z = (X - 1.5)**2 + (Y - 1.5)**2 - 1
# draw
plt.contour(X, Y, Z, 0)
plt.axis('equal')
# plt.axis('off')
plt.xlim(-0.2, 2.8)
plt.ylim(-0.2, 2.8)
# axis range (-3, 3)
plt.yticks([0])
plt.xticks([])
ax = plt.gca()
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')
ax.spines['left'].set_position(('data', 0))
ax.spines['bottom'].set_position(('data', 0))
plt.text(3, -0.2, 'x', fontsize=12)
plt.text(-0.2, 3, 'y', fontsize=12)
# draw x = 0.25
plt.plot([0.25, 0.25], [-0.2, 2.8], linestyle='--', color='black')
plt.plot([-0.2, 2.8], [0.25, 0.25], linestyle='--', color='black')
plt.text(0.25, 0.15, '(0.25, 0.25)', fontsize=12)

# draw dashed line y = x, y = 2x, y = 0.5 x
plt.plot([-0.2, 2.8], [-0.2, 2.8], linestyle='--', color='black')
plt.text(0.15, -0.2, 'y = x', fontsize=12)
plt.plot([-0.2, 2.8], [2*(-0.2), 2*(2.8)], linestyle='--', color='black')
plt.text(0.15, 2.6, 'y = 2x', fontsize=12)
plt.plot([-0.2, 2.8], [0.5*(-0.2), 0.5*(2.8)], linestyle='--', color='black')
plt.text(0.15, 1.2, 'y = 0.5 x', fontsize=12)

# plt.savefig('circle2.png', transparent=False)
plt.savefig('Code/pre.png', transparent=True)