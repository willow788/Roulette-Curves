import colorsys
import math
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main() -> None:
    # Parameters (tune these to match a specific reference)
    a = 5
    b = 4
    phase_sweep = 2 * math.pi  # total phase range swept across layers
    layers = 320
    steps = 12000

    # Visual style
    line_width = 0.6
    alpha = 0.025
    hue = 0.14  # golden/yellow
    output_path = Path(__file__).with_name("lissajous.png")

    t = np.linspace(0.0, 2 * math.pi, steps, endpoint=True)

    fig, ax = plt.subplots(figsize=(8, 8), facecolor="black")
    ax.set_facecolor("black")
    ax.set_aspect("equal", adjustable="box")
    ax.axis("off")

    for k in range(layers):
        phase = (k / layers) * phase_sweep
        value = 0.20 + 0.80 * (k / layers)
        r, g, b_ = colorsys.hsv_to_rgb(hue, 1.0, value)

        x = np.sin(a * t + phase)
        y = np.sin(b * t)

        ax.plot(x, y, color=(r, g, b_, alpha), linewidth=line_width)

    # Tight framing
    ax.set_xlim(-1.05, 1.05)
    ax.set_ylim(-1.05, 1.05)
    plt.margins(0)

    fig.savefig(output_path, dpi=300, facecolor=fig.get_facecolor(), bbox_inches="tight", pad_inches=0)
    plt.show()


if __name__ == "__main__":
    main()
