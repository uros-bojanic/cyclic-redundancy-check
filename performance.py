# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Created By  : Uros Bojanic
# Created Date: 2022/03/16
# ---------------------------------------------------------------------------

# Python program to analyze and plot CRC benchmark results
import numpy as np
import pandas as pd
import imageio
import matplotlib.pyplot as plt


# Driver code
if __name__ == "__main__":
    # Load benchmark data
    df = pd.read_csv('benchmark.csv')

    # Preview benchmark data
    df.head(1000)

    # Algorithm name (generator)
    xs = df['Name'].unique()
    xd = dict()
    for index, name in enumerate(xs):
        xd[index] = name
    x = np.array(list(range(0, len(xs))))

    # Sequence length (information)
    y = df['SequenceLength'].unique()

    # 3D execution time data
    X, Y = np.meshgrid(x, y)
    Z = X.copy()
    for i in range(0, len(X)):
        for j in range(0, len(X[0])):
            Z[i][j] = df.loc[(df.Name == xd[X[i][j]]) & (df.SequenceLength == Y[i][j])]['ExecutionTime'].values[0]

    # 3D plot using matplotlib
    fig = plt.figure()
    fig.set_dpi(200)
    ax = fig.add_subplot(111, projection='3d')
    ax.contour3D(X, Y, Z, 50)
    ax.set(xticks=range(len(xs)), xticklabels=xs)

    axis_ticks_fontsize = 5
    axis_label_fontsize = 7
    axis_label_color = 'red'
    axis_label_backgroundcolor = 'white'

    ax.set_xlabel('CRC algorithm (complexity)')
    ax.xaxis.label.set_color(axis_label_color)
    ax.xaxis.label.set_fontsize(axis_label_fontsize)
    ax.xaxis.label.set_backgroundcolor(axis_label_backgroundcolor)
    ax.xaxis.set_tick_params(labelsize=axis_ticks_fontsize)
    ax.xaxis.labelpad = 20

    ax.set_ylabel('Length of encoded sequence (bits)')
    ax.yaxis.label.set_color(axis_label_color)
    ax.yaxis.label.set_fontsize(axis_label_fontsize)
    ax.yaxis.label.set_backgroundcolor(axis_label_backgroundcolor)
    ax.yaxis.set_tick_params(labelsize=axis_ticks_fontsize)

    ax.set_zlabel('Execution time (ms)')
    ax.zaxis.label.set_color(axis_label_color)
    ax.zaxis.label.set_fontsize(axis_label_fontsize)
    ax.zaxis.label.set_backgroundcolor(axis_label_backgroundcolor)
    ax.zaxis.set_tick_params(labelsize=axis_ticks_fontsize)

    # Rotate the axes and update
    iteration = 0
    filenames = []
    for angle in range(0, 180):
        # Save frame
        filename = 'benchmark_plot/benchmark_plot_{}.png'.format(iteration)
        fig.savefig(filename, dpi=200)
        filenames.append(filename)
        iteration += 1
        # Rotate plot
        ax.view_init(30, 180+angle)
        plt.draw()
        plt.pause(.0001)

    # Build GIF from frames
    with imageio.get_writer('performance.gif', mode='I') as writer:
        for filename in filenames:
            image = imageio.imread(filename)
            writer.append_data(image)
