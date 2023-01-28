from math import sqrt
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

FONT_SIZE = 18
MAX_HEIGHT_INCHES = 3.75

def latexify(fig_width=None, fig_height=None, columns=2):
    """Set up matplotlib's RC params for LaTeX plotting.
    Call this before plotting a figure.

    Parameters
    ----------
    fig_width : float, optional, inches
    fig_height : float,  optional, inches
    columns : {1, 2}
    """

    # code adapted from http://www.scipy.org/Cookbook/Matplotlib/LaTeX_Examples

    # Width and max height in inches for IEEE journals taken from
    # computer.org/cms/Computer.org/Journal%20templates/transactions_art_guide.pdf

    assert(columns in [1,2])

    if fig_width is None:
        fig_width = 3.5 if columns==1 else 7 # width in inches

    if fig_height is None:
        golden_mean = (sqrt(5)-1.0)/2.0    # Aesthetic ratio
        fig_height = fig_width*golden_mean # height in inches

    if fig_height > MAX_HEIGHT_INCHES:
        print("WARNING: fig_height too large: " + str(fig_height) + " so will reduce to " + str(MAX_HEIGHT_INCHES) + " inches.")
        fig_height = MAX_HEIGHT_INCHES

    params = {'backend': 'ps',
              'text.latex.preamble': r'\usepackage{gensymb}',
              'axes.labelsize': FONT_SIZE, # fontsize for x and y labels (was 10)
              'axes.titlesize': FONT_SIZE,
              'font.size': FONT_SIZE, # was 10
              'legend.fontsize': FONT_SIZE, # was 10
              'xtick.labelsize': FONT_SIZE,
              'ytick.labelsize': FONT_SIZE,
              'text.usetex': True,
              'figure.figsize': [fig_width,fig_height],
              'font.family': 'serif'
    }

    plt.rcParams.update(params)


def format_axes(ax):
    SPINE_COLOR = 'black'

    for spine in ['top', 'right']:
        ax.spines[spine].set_visible(False)

    for spine in ['left', 'bottom']:
        ax.spines[spine].set_color(SPINE_COLOR)
        ax.spines[spine].set_linewidth(0.5)
        ax.spines[spine].set_position('zero')

    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')

    for axis in [ax.xaxis, ax.yaxis]:
        axis.set_tick_params(direction='out', color=SPINE_COLOR)
        
    ax.plot((1), (0), ls="", marker=">", ms=10, color=SPINE_COLOR, transform=ax.get_yaxis_transform(), clip_on=False)
    ax.plot((0), (1), ls="", marker="^", ms=10, color=SPINE_COLOR, transform=ax.get_xaxis_transform(), clip_on=False)
    ax.xaxis.get_major_ticks()[1].label1.set_visible(False)
    ax.yaxis.get_major_ticks()[1].label1.set_visible(False)

    return ax
