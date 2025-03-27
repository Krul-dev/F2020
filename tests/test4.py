#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: Raul Gomez
Date: 2025-03-27
Description: 
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def animate_growing_wave():
    x = np.linspace(0, 10, 500)  # Full x values
    y = np.sin(x)

    fig, ax = plt.subplots()
    line, = ax.plot([], [], lw=2)

    ax.set_xlim(0, 10)
    ax.set_ylim(-1.5, 1.5)

    def update(frame):
        # Use data up to the current frame
        line.set_data(x[:frame], y[:frame])
        return line,

    ani = FuncAnimation(fig, update, frames=len(x), interval=10, blit=True)
    plt.show()

animate_growing_wave()

