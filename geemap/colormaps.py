"""Module for commonly used colormaps and palettes for visualizing Earth Engine data.
"""
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from box import Box


def get_palette(cmap_name=None, n_class=None):
    """Get a palette from a matplotlib colormap. See the list of colormaps at https://matplotlib.org/stable/tutorials/colors/colormaps.html.

    Args:
        cmap_name (str, optional): The name of the matplotlib colormap. Defaults to None.
        n_class (int, optional): The number of colors. Defaults to None.

    Returns:
        list: A list of hex colors.
    """
    cmap = plt.cm.get_cmap(cmap_name, n_class)
    colors = [mpl.colors.rgb2hex(cmap(i))[1:] for i in range(cmap.N)]
    return colors


def list_colormaps():
    """List all available colormaps. See a complete lost of colormaps at https://matplotlib.org/stable/tutorials/colors/colormaps.html.

    Returns:
        list: The list of colormap names.
    """
    return plt.colormaps()


def plot_colormap(
    cmap,
    width=8.0,
    height=0.4,
    orientation="horizontal",
    axis_off=True,
    show_name=False,
    font_size=12,
):
    """Plot a colormap.

    Args:
        cmap (str): The name of the colormap.
        width (float, optional): The width of the colormap. Defaults to 8.0.
        height (float, optional): The height of the colormap. Defaults to None.
        orientation (str, optional): The orientation of the colormap. Defaults to "horizontal".
        axis_off (bool, optional): Whether to turn axis off. Defaults to True.
        show_name (bool, optional): Whether to show the colormap name. Defaults to False.
        font_size (int, optional): Font size of the text. Defaults to 12.
    """
    fig, ax = plt.subplots(figsize=(width, height))
    col_map = plt.get_cmap(cmap)

    mpl.colorbar.ColorbarBase(ax, cmap=col_map, orientation=orientation)
    if axis_off:
        ax.set_axis_off()

    if show_name:
        pos = list(ax.get_position().bounds)
        x_text = pos[0] - 0.01
        y_text = pos[1] + pos[3] / 2.0
        fig.text(x_text, y_text, cmap, va="center", ha="right", fontsize=font_size)

    plt.show()


def plot_colormaps(width=8.0, height=0.4):
    """Plot all availabe colormaps.

    Args:
        width (float, optional): Width of the colormap. Defaults to 8.0.
        height (float, optional): Height of the colormap. Defaults to 0.4.
    """
    cmap_list = list_colormaps()
    nrows = len(cmap_list)
    fig, axes = plt.subplots(nrows=nrows, figsize=(width, height * nrows))
    fig.subplots_adjust(top=0.95, bottom=0.01, left=0.2, right=0.99)

    gradient = np.linspace(0, 1, 256)
    gradient = np.vstack((gradient, gradient))

    for ax, name in zip(axes, cmap_list):
        ax.imshow(gradient, aspect="auto", cmap=plt.get_cmap(name))
        ax.set_axis_off()
        pos = list(ax.get_position().bounds)
        x_text = pos[0] - 0.01
        y_text = pos[1] + pos[3] / 2.0
        fig.text(x_text, y_text, name, va="center", ha="right", fontsize=12)

    # Turn off *all* ticks & spines, not just the ones with colormaps.
    for ax in axes:
        ax.set_axis_off()

    plt.show()


__palette_dict = {
    "ndvi": [
        "FFFFFF",
        "CE7E45",
        "DF923D",
        "F1B555",
        "FCD163",
        "99B718",
        "74A901",
        "66A000",
        "529400",
        "3E8601",
        "207401",
        "056201",
        "004C00",
        "023B01",
        "012E01",
        "011D01",
        "011301",
    ],
    "ndwi": [
        "#ece7f2",
        "#d0d1e6",
        "#a6bddb",
        "#74a9cf",
        "#3690c0",
        "#0570b0",
        "#045a8d",
        "#023858",
    ],
    "dem": ["006633", "E5FFCC", "662A00", "D8D8D8", "F5F5F5"],
}

for index, cmap_name in enumerate(list_colormaps()):
    if index < len(list_colormaps()):
        color_dict = {}
        for i in range(3, 13):
            name = "n" + str(i).zfill(2)
            colors = get_palette(cmap_name, i)
            color_dict[name] = colors
        __palette_dict[cmap_name] = color_dict


palettes = Box(__palette_dict, frozen_box=True)