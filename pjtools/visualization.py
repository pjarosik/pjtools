import matplotlib.pyplot as plt
import matplotlib.animation as animation


def create_animation(imgs, value_range=None, cmap=None, figsize=None,
                  interval=50, xlabel="OX", ylabel="OY", extent=None):
    """
    Create matpltotlib animation for a given sequence of frames.

    :param imgs: 3D numpy array with shape (frame, x, y)
    """

    fig, ax = plt.subplots()

    def init():
        img.set_data(imgs[0])
        return (img,)

    def animate(frame):
        img.set_data(imgs[frame])
        fig.suptitle(f"frame: {frame}")
        return (img,)

    if figsize is not None:
        fig.set_size_inches(figsize)
    img = ax.imshow(imgs[0], cmap=cmap, extent=extent)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    if value_range is not None:
        img.set_clim(*value_range)
    return animation.FuncAnimation(
        fig, animate, init_func=init, frames=len(imgs),
        interval=interval, blit=True)
