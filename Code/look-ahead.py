import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-3, 4, 0.01)
y = np.arange(-1.2, 6, 0.01)
X, Y = np.meshgrid(x, y)
Z = (X - 2)**2 + (Y - 2)**2 - 1
# draw
plt.contour(X, Y, Z, 0)
plt.axis('equal')
# plt.axis('off')
plt.xlim(-0.2, 2.8)
plt.ylim(-0.2, 4)
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
# plt.plot([0.25, 0.25], [-0.2, 2.8], linestyle='--', color='black')
# plt.plot([-0.2, 2.8], [0.25, 0.25], linestyle='--', color='black')
# plt.text(1.5, -0.25, '(1.5, 0)', fontsize=12)
# plt.text(0, 1.25, '(0, 1.5)', fontsize=12)

# plt.text(0.7, 0.8, '(0.7, 0.7)', fontsize=12)
plt.scatter(0.7, 0.7, color='black', s=10)

# plt.text(0.8, 0.5, 'lk(l, x)', fontsize=12)
# plt.text(1.5, 1.2, 'lk(l, y)', fontsize=12)

plt.plot([0.7, 1.4], [0.7, 0.7], linestyle='--', color='black')
plt.plot([1.4, 1.4], [0.7, 3], linestyle='--', color='black')

# draw dashed line y = x, y = 2x, y = 0.5 x
# plt.plot([-0.2, 2.8], [-0.2, 2.8], linestyle='--', color='black')
# plt.text(1.5, 2, 'y = x', fontsize=12)
# plt.plot([-0.2, 2.8], [2*(-0.2), 2*(2.8)], linestyle='--', color='black')
# plt.text(0.8, 2.6, 'y = 2x', fontsize=12)
# plt.plot([-0.2, 2.8], [0.5*(-0.2), 0.5*(2.8)], linestyle='--', color='black')
# plt.text(2, 1.2, 'y = 0.5 x', fontsize=12)

plt.savefig('Code/img/look-ahead.png', transparent=True)