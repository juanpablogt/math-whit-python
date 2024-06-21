from matplotlib import pyplot as plt
from matplotlib.patches import Circle

def draw_square(ax):
    square = plt.Polygon([(1, 1), (5, 1), (5, 5), (1, 5)], closed=True)
    ax.add_patch(square)

def draw_circles(ax):
    draw_square(ax)
    y = 1.5
    while y < 5:
        x = 1.5
        while x < 5:
            c = Circle((x, y), 0.5, zorder=3, color='red') # Color rojo para los círculos
            ax.add_patch(c)
            x += 1.0
        y += 1.0
    plt.show()

if __name__ == '__main__':
    ax = plt.axes(xlim=(0, 6), ylim=(0, 6))
    draw_circles(ax)