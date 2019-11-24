import matplotlib.pyplot as plt
import numpy as np


FIGURE_SIZE = (4.5, 3.5)
FIGURE_DPI = 72

COLOR_PALETTE = ["xkcd:soft green", "xkcd:pastel red"]

PLOT_XMAX = 1
PLOT_SAMPLES = 1000
PLOT_XMARGIN = 0.05
PLOT_YMARGIN = 0.05

LINE_WIDTH = 1.5
XKCD_SCALE = 0.3

OUTPUT_BASEDIR = "_static/img"


def harmonic_potential(r, *, k):
    return 0.5 * k * r ** 2


def spring_potential(r, *, k, b):
    return 0.5 * k * (r - b) ** 2


def semispring_potential(r, *, k, b):
    return 0.5 * k * np.maximum(0, r - b) ** 2


def lennard_jones_potential(r, *, epsilon, sigma):
    r = np.maximum(r, 1e-6)
    return epsilon * ((sigma / r) ** 12 - 2 * (sigma / r) ** 6)


def softcore_potential(r, *, epsilon, sigma, p, q):
    return epsilon * np.maximum(0, 1 - (r / sigma) ** p) ** q


def softwell_potential(r, *, epsilon, sigma, p):
    return -epsilon / (1 + (r / sigma) ** p)


def main():
    make(
        harmonic_potential,
        [
            dict(k=1),
        ],
        xticks={
            "values": [0.0, 0.3, 0.6, 0.9],
            "labels": ["0", "", "", ""],
        },
        yticks={
            "values": [0.0, 0.2, 0.4],
            "labels": ["0", "", ""],
        },
    )

    make(
        spring_potential,
        [
            dict(k=10, b=0.3),
        ],
        xticks={
            "values": [0.0, 0.3, 0.6, 0.9],
            "labels": ["0", "b", "", ""],
        },
        yticks={
            "values": [0.0, 1.0, 2.0],
            "labels": ["0", "", ""],
        },
    )

    make(
        semispring_potential,
        [
            dict(k=10, b=0.3),
        ],
        xticks={
            "values": [0.0, 0.3, 0.6, 0.9],
            "labels": ["0", "b", "", ""],
        },
        yticks={
            "values": [0.0, 1.0, 2.0],
            "labels": ["0", "", ""],
        },
    )

    make(
        lennard_jones_potential,
        [
            dict(epsilon=1, sigma=0.3),
        ],
        xticks={
            "values": [0.0, 0.3, 0.6, 0.9],
            "labels": ["0", "sigma", "", ""],
        },
        yticks={
            "values": [-1.0, 0.0, 1.0, 2.0],
            "labels": ["-epsilon", "0", "", ""],
        },
        ymin=-1.1,
        ymax=2.1,
    )

    make(
        softcore_potential,
        [
            dict(epsilon=2, sigma=0.6, p=2, q=3, label="<2, 3>"),
            dict(epsilon=2, sigma=0.6, p=8, q=3, label="<8, 3>"),
        ],
        xticks={
            "values": [0.0, 0.3, 0.6, 0.9],
            "labels": ["0", "", "sigma", ""],
        },
        yticks={
            "values": [0.0, 1.0, 2.0],
            "labels": ["0", "", "epsilon"],
        },
    )

    make(
        softwell_potential,
        [
            dict(epsilon=2, sigma=0.3, p=4, label="< 4 >"),
            dict(epsilon=2, sigma=0.3, p=12, label="< 12 >"),
        ],
        xticks={
            "values": [0.0, 0.3, 0.6, 0.9],
            "labels": ["0", "sigma", "", ""],
        },
        yticks={
            "values": [-2.0, -1.0, 0.0],
            "labels": ["-epsilon", "", "0"],
        },
        ymax=1.2,
    )


def make(func, specs, *, xticks, yticks, **kwargs):
    name = func.__name__
    plots = []

    for spec in specs:
        args = spec.copy()
        label = args.pop("label", None)
        x = np.linspace(0, PLOT_XMAX, num=PLOT_SAMPLES)
        y = func(x, **args)
        plots.append({"x": x, "y": y, "label": label})

    with plt.xkcd(scale=XKCD_SCALE):
        fig = make_graph(plots, xticks=xticks, yticks=yticks, title=name, **kwargs)
        fig.savefig(f"{OUTPUT_BASEDIR}/{name}.png")


def make_graph(
    plots, *, xticks, yticks, title, xmin=None, xmax=None, ymin=None, ymax=None
):
    fig, ax = plt.subplots(figsize=FIGURE_SIZE, dpi=FIGURE_DPI, constrained_layout=True)

    ax.spines["top"].set_color("none")
    ax.spines["right"].set_color("none")

    for plot, color in zip(plots, COLOR_PALETTE):
        ax.plot(plot["x"], plot["y"], lw=LINE_WIDTH, color=color, label=plot["label"])

    ax.set_xlabel("r")
    ax.set_title(title)

    ax.set_xticks(xticks["values"])
    ax.set_yticks(yticks["values"])
    ax.set_xticklabels(xticks["labels"])
    ax.set_yticklabels(yticks["labels"])

    xmin = xmin or ax.get_xlim()[0]
    xmax = xmax or ax.get_xlim()[1]
    ymin = ymin or ax.get_ylim()[0]
    ymax = ymax or ax.get_ylim()[1]
    ax.set_xlim(xmin, xmax)
    ax.set_ylim(ymin, ymax)

    ax.grid(True, lw=1, ls=":")
    if len(plots) > 1:
        ax.legend(framealpha=1, facecolor="white", edgecolor="none")

    return fig


if __name__ == "__main__":
    main()
