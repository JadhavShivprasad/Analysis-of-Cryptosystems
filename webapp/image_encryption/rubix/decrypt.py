import cv2
from random import randint
import numpy
import sys
from image_encryption.rubix.helper import *

def rubix_dec(path):
    pix = cv2.imread(path)

    # Obtaining the RGB matrices
    r = []
    g = []
    b = []
    for i in range(pix.shape[0]):
        r.append([])
        g.append([])
        b.append([])
        for j in range(pix.shape[1]):
            rgbPerPixel = pix[i, j]
            r[i].append(rgbPerPixel[0])
            g[i].append(rgbPerPixel[1])
            b[i].append(rgbPerPixel[2])

    m = pix.shape[0]
    n = pix.shape[1]

    Kr = []
    Kc = []

    print('Enter value of Kr')
    kc = open('kc.txt', 'r')
    kr = open('kr.txt', 'r')
    Kr_lines = kr.readlines()
    Kc_lines = kc.readlines()

    for x in Kr_lines:
        Kr.append(int(x.replace('\n', '')))

    for x in Kc_lines:
        Kc.append(int(x.replace('\n', '')))

    print(kc)
    print(kr)
    print('Enter value of ITER_MAX')
    ITER_MAX = 1

    for iterations in range(ITER_MAX):
        # For each column
        for j in range(n):
            for i in range(m):
                if j % 2 == 0:
                    r[i][j] = r[i][j] ^ Kr[i]
                    g[i][j] = g[i][j] ^ Kr[i]
                    b[i][j] = b[i][j] ^ Kr[i]
                else:
                    r[i][j] = r[i][j] ^ rotate180(Kr[i])
                    g[i][j] = g[i][j] ^ rotate180(Kr[i])
                    b[i][j] = b[i][j] ^ rotate180(Kr[i])
        # For each row
        for i in range(m):
            for j in range(n):
                if i % 2 == 1:
                    r[i][j] = r[i][j] ^ Kc[j]
                    g[i][j] = g[i][j] ^ Kc[j]
                    b[i][j] = b[i][j] ^ Kc[j]
                else:
                    r[i][j] = r[i][j] ^ rotate180(Kc[j])
                    g[i][j] = g[i][j] ^ rotate180(Kc[j])
                    b[i][j] = b[i][j] ^ rotate180(Kc[j])
        # For each column
        for i in range(n):
            rTotalSum = 0
            gTotalSum = 0
            bTotalSum = 0
            for j in range(m):
                rTotalSum += r[j][i]
                gTotalSum += g[j][i]
                bTotalSum += b[j][i]
            rModulus = rTotalSum % 2
            gModulus = gTotalSum % 2
            bModulus = bTotalSum % 2
            if rModulus == 0:
                downshift(r, i, Kc[i])
            else:
                upshift(r, i, Kc[i])
            if gModulus == 0:
                downshift(g, i, Kc[i])
            else:
                upshift(g, i, Kc[i])
            if bModulus == 0:
                downshift(b, i, Kc[i])
            else:
                upshift(b, i, Kc[i])

        # For each row
        for i in range(m):
            rTotalSum = sum(r[i])
            gTotalSum = sum(g[i])
            bTotalSum = sum(b[i])
            rModulus = rTotalSum % 2
            gModulus = gTotalSum % 2
            bModulus = bTotalSum % 2
            if rModulus == 0:
                r[i] = numpy.roll(r[i], -Kr[i])
            else:
                r[i] = numpy.roll(r[i], Kr[i])
            if gModulus == 0:
                g[i] = numpy.roll(g[i], -Kr[i])
            else:
                g[i] = numpy.roll(g[i], Kr[i])
            if bModulus == 0:
                b[i] = numpy.roll(b[i], -Kr[i])
            else:
                b[i] = numpy.roll(b[i], Kr[i])

    for i in range(m):
        for j in range(n):
            pix[i, j] = (r[i][j], g[i][j], b[i][j])

    cv2.imwrite("home/static/home/result/Recovered.jpg", pix)
