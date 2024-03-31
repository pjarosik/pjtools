import matplotlib.pyplot as plt
import matplotlib.animation as animation

def create_animation(imgs, value_range=None, cmap=None, figsize=None,
                  interval=50, xlabel="OX", ylabel="OY", extent=None, aspect=None,
                  titles=None
):
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
        if titles is not None:
            fig.suptitle(titles[frame])
        else:
            fig.suptitle(f"frame: {frame}")
        return (img,)

    if figsize is not None:
        fig.set_size_inches(figsize)
    img = ax.imshow(imgs[0], cmap=cmap, extent=extent)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    if aspect is not None:
      ax.set_aspect(aspect)
    if value_range is not None:
        img.set_clim(*value_range)
    return animation.FuncAnimation(
        fig, animate, init_func=init, frames=len(imgs),
        interval=interval, blit=True)


def create_animation_1d(lines, value_range=None, cmap=None, figsize=None,
                        interval=50, xlabel="OX", ylabel="OY",
                        aspect=None):
    """
    Create matpltotlib animation for a given sequence of lines.

    :param imgs: 2D numpy array with shape (frame, y)
    """

    fig, ax = plt.subplots()
    
    t = np.arange(len(lines[0]))

    def init():
        l.set_data(t, lines[0])
        return l, 

    def animate(frame):
        l.set_data(t, lines[frame])
        fig.suptitle(f"sample: {frame}")
        return l, 

    if figsize is not None:
        fig.set_size_inches(figsize)
    l,  = ax.plot(t, lines[0])
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    if aspect is not None:
        ax.set_aspect(aspect)
    return animation.FuncAnimation(
        fig, animate, init_func=init, frames=len(lines),
        interval=interval, blit=True)
