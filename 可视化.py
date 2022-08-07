# 数据可视化 图表
from matplotlib import pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = Axes3D(fig)
x = np.arange(-4, 4, 0.25)
Y = np.arange(-4, 4, 0.25)
x, Y = np.meshgrid(x, Y)
R = np.sqrt(x ** 2 + Y ** 2)
z = np.sin(R)
# 具体函数方法可用help(function）查看，如: help(ax.plot_surface)ax.plot_surface(X, Y，z,rstride=1, cstride=1, cmap='rainbow')
plt.show()
