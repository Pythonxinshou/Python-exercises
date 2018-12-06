import matplotlib.pyplot as plt


squares1 = list(range(1, 6))
squares2 = list(range(1, 5001))
x_squares1 = [x**3 for x in squares1]
x_squares2 = [i**3 for i in squares2]
plt.scatter(squares1, x_squares1, c='c', s=1)
plt.scatter(squares2, x_squares2, c='g', edgecolor='none', s=1)

# 设置图表标题并给坐标轴设置标签
plt.title("Square Number", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# 设置刻度标记大小
plt.tick_params(axis='both', which='major', labelsize=14)

plt.show()
