import matplotlib.pyplot as plt
from matplotlib import style

style.use('ggplot')
x = [1,2,3]
y = [4,5,6]
x1 = [1,2,3]
y1 = [2,4,6]
x2 = [1,2,3]
y2 = [4,5,6]

plt.plot(x,y,'c',linewidth=5,label = 'first line')

plt.title('Lets see')
plt.plot(x1,y1,'g',linewidth=8,label = 'second line')
plt.legend()
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.xlabel('x1-axis')
plt.ylabel('y1-axis')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.grid(True,color='k')
#plt.legend()
plt.show()
plt.plot(x1,y1)
