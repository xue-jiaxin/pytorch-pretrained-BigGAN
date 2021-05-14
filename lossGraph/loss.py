from matplotlib import pyplot as plt
import matplotlib.patches as mpatches

import numpy as np


def extarct_data():
    gan = 'G_GAN: '
    gl1 = 'G_L1: '
    dreal = 'D_real: '
    dfake = 'D_fake: '
    f = open('loss_log1.txt')
    gan_list = [0]
    gl1_list = [0]
    dreal_list = [0]
    dfake_list = [0]
    for line in f:
        gan_pos = line.find(gan) + len(gan)
        gl1_pos = line.find(gl1) + len(gl1)
        dreal_pos = line.find(dreal) + len(dreal)
        dfake_pos = line.find(dfake) + len(dfake)
        if gan in line:
            gan_list.append(float(line[gan_pos:gan_pos + 5]))
        if gl1 in line:
            gl1_list.append(float(line[gl1_pos:gl1_pos + 5]))
        if dreal in line:
            dreal_list.append(float(line[dreal_pos:dreal_pos + 5]))
        if dfake in line:
            dfake_list.append(float(line[dfake_pos:]))
    return gan_list, gl1_list, dreal_list, dfake_list


gan, gl1, deal, dfake = extarct_data()


def plot_loss():
    gan, gl1, dreal, dfake = extarct_data()
    gan_moy = [sum(gan[i:i + 50]) / 50 for i in range(0, len(gan) - 50, 50)]
    gl1_moy = [sum(gl1[i:i + 50]) / 50 for i in range(0, len(gl1) - 50, 50)]
    dfake_moy = [sum(dfake[i:i + 50]) / 50 for i in range(0, len(dfake) - 50, 50)]
    dreal_moy = [sum(dreal[i:i + 50]) / 50 for i in range(0, len(dreal) - 50, 50)]
    return gan_moy, gl1_moy, dfake_moy, dreal_moy


gan, gl1, dreal, dfake = plot_loss()

linegan, = plt.plot(gan, label="G_GAN", linewidth=0.9)
linedfake, = plt.plot(dfake, label="D_fake", linewidth=0.9)
linedreal, = plt.plot(dreal, label="D_real", linewidth=0.9)
plt.legend(loc="center right")

plt.show()
