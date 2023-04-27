import numpy as np
import matplotlib.pyplot as plt

# 创建数据
x = np.linspace(0, 2 * np.pi, 1000)
y = np.sin(x)

# 绘制图形
plt.plot(x, y)

# 设置坐标轴标签和标题
plt.xlabel('x')
plt.ylabel('y')
plt.title('Sine Wave')

# 显示图形
plt.show()