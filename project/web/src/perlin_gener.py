from perlin_noise import *

def map_fin(n_of_chunks, length, height):
    noise = PerlinNoise(octaves=10, seed=1)
    xpix, ypix = n_of_chunks*length, n_of_chunks*length

    map = [[noise([i/xpix, j/ypix]) for j in range(xpix)] for i in range(ypix)]
    map_2 = [[noise([i/xpix, j/ypix]) for j in range(xpix)] for i in range(ypix)]
    map_3 = [[noise([i/xpix, j/ypix]) for j in range(xpix)] for i in range(ypix)]
    map_4 = [[noise([i/xpix, j/ypix]) for j in range(xpix)] for i in range(ypix)]
    map_5 = [[noise([i/xpix, j/ypix]) for j in range(xpix)] for i in range(ypix)]

    mapa_fin = [[map[i][j]+map_2[i][j]+map_3[i][j]+map_4[i][j]+map_5[i][j]/5 * height for j in range(xpix)] for i in range(ypix)]

    return mapa_fin