import numpy as np
import matplotlib.pyplot as plt


# The mandelbrot function takes in a value for n, N_max, and threshold.
# The function will compute the Mandelbrot fractal using a Mandelbrot iteration on each point
def mandelbrot(n, N_max, threshold):
    # x = np.linspace(-2, 1, n)
    # y = np.linspace(-1.5, 1.5, n)

    x = np.linspace(-1.5, 1.5, n)
    y = np.linspace(-2, 1, n)

    # The numpy.meshgrid function returns two 2-Dimensional arrays
    # representing the X and Y coordinates of all the points.
    # nxn grid of points (x,y) in range [−2,1]×[−1.5,1.5]
    y_cords, x_cords = np.meshgrid(x, y)

    # corresponding complex values
    c = x_cords + 1j * y_cords

    z = 0

    # Mandelbrot iteration on each point
    for a in range(N_max):
        z = z ** 2 + c

    mask = (abs(z) < threshold)

    # this will plot the true mask values and will save the figure as a png
    plt.imshow(mask.T, extent=[-2, 1, -1.5, 1.5])
    plt.gray()
    plt.savefig('mandelbrot.png')


# the test n used was 1500 which yields a result similar to that in the original task.
mandelbrot(1500, 50, 50)
