import time
import psutil
import matplotlib.pyplot as plt


get_ipython().run_line_magic('matplotlib', 'notebook')
plt.rcParams['animation.html'] = 'jshtml'



fig = plt.figure()
ax = fig.add_subplot(111)
fig.show()



i = 0
x,y = [], []

while True:
    x.append(i)
    y.append(psutil.cpu_percent())
    
    ax.plot(x, y, color='b')
    
    fig.canvas.draw()
    
    timesleep(0.1)
    i += 1

