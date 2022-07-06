import matplotlib.pyplot as plt
from grid import Grid
import time

DIM = 6

images = [
        plt.imread("images/0.png"),
        plt.imread("images/1.png"),
        plt.imread("images/2.png"),
        plt.imread("images/3.png"),
        plt.imread("images/4.png")
    ]

f, axes = plt.subplots(DIM,DIM, figsize=(DIM, DIM))
plt.subplots_adjust(wspace=0, hspace=0, left=0, right=1, bottom=0, top=1)

def showImages(g:Grid) :
    grid = g.getGridOrientation()
    for i in range(DIM) :
        for j in range(DIM):
            axes[i, j].axis("off")
            if grid[i][j] is None :
                continue
            axes[i, j].imshow(images[grid[i][j]])
    plt.pause(0.2)
    plt.draw()

g = Grid(DIM)
finish = 1
while finish :
    finish = g.runStep()
    showImages(g)
time.sleep(1)

# im1 = plt.imread("images/1.png")
# im2 = plt.imread("images/2.png")
# im3 = plt.imread("images/3.png")
# im4 = plt.imread("images/4.png")

# f, axes = plt.subplots(DIM,DIM, figsize=(DIM, DIM))

# axes[0, 0].imshow(im4)
# axes[0, 1].imshow(im2)
# axes[1, 0].imshow(im3)
# axes[1, 1].imshow(im1)

# axes[0, 0].axis('off')
# axes[0, 1].axis('off')
# axes[1, 0].axis('off')
# axes[1, 1].axis('off')

# plt.subplots_adjust(wspace=0, hspace=0, left=0, right=1, bottom=0, top=1)
# plt.show()