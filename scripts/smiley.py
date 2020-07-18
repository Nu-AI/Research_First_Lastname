import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize = (8,8))
ax = fig.add_subplot(1,1,1,aspect = 1)
ax.scatter([.5], [.5], c = 'yellow', edgecolor = 'gold', linewidth = 15, s = 210000)
ax.scatter([.35], [.62], c = 'darkgoldenrod', s = 1700)
x = np.linspace(.35,.65, 100)
y = 4 * (x-.5)**2 + 0.3

ax.plot(x,y,c = 'darkgoldenrod', linewidth = 20)

a = np.linspace(.6,.7, 100)
b = -1.75*(a-.7)**2 + 0.6

c = np.linspace(.63, .75, 100)
d = -1.25*(a-.6)**1.5 + 0.7

e = np.linspace(.25,.35, 100)
f = -2*(a-.8)**2 + 0.77

ax.plot(a,b,c='darkgoldenrod', linewidth = 11)
ax.plot(c,d,c='darkgoldenrod', linewidth = 9)
ax.plot(e,f,c='darkgoldenrod', linewidth = 9)

plt.grid(False)
plt.show()