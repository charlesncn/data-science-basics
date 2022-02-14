import matplotlib.pyplot as plt
import numpy as np
fig, axis = plt.subplots(2)
rng = np.random.RandomState(42)
x =10 * rng.rand(40)
y= 2*x-1+rng.randn(40)

axis[0].set_title('X Values')
axis[0].hist(x, rwidth=0.7)

plt.subplots_adjust(top=3)
axis[1].set_title('Y Values')
axis[1].hist(y, rwidth=0.6)

# axis[2].bar(x,y)
