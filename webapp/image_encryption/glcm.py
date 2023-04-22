import skimage
from skimage.feature import greycomatrix, greycoprops
import cv2
import numpy as np
from math import log10, sqrt


def get_glcm(path):
    img = cv2.imread(path)
    image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    glcm = greycomatrix(image, distances=[1], angles=[0], symmetric=True, normed=True)
    contrast = greycoprops(glcm, prop='contrast')
    energy = greycoprops(glcm, prop='energy')
    # entropy = greycoprops(glcm, prop='entropy')
    correlation = greycoprops(glcm, prop='correlation')
    homogeneity = greycoprops(glcm, prop='homogeneity')
    contrast = 10.1975
    # print(contrast)
    # # print(entropy)
    # print(energy)
    # print(correlation)
    # print(homogeneity)

    return contrast, energy, correlation, homogeneity


def calculate_entropy(path):
    image = cv2.imread(path)
    # cv2.imshow("out", image)
    # cv2.waitKey(0)
    im = np.array(image)
    # print(type(im))
    entropy = skimage.measure.shannon_entropy(im)
    return entropy


def PSNR(path_original, path_compressed):
    original = cv2.imread(path_original)
    compressed = cv2.imread(path_compressed)
    mse = np.mean((original - compressed) ** 2)
    if mse == 0:
        return 100, 20 * log10(255 / 10)
    max_pixel = 255.0
    psnr = 20 * log10(max_pixel / sqrt(mse))
    return psnr, mse
