import numpy as np
import skimage.measure
import cv2
import os
import pandas as pd

dna = "../images/dna/dna_encrypted/"
log = "../images/log/enc/"
lorenz = "../images/lorenz/enc/"
rubix = "../images/rubix/rubix_encrypted/"





def make_dataset(path, name):
    dir1 = os.listdir(path)
    ent = []
    n = []
    for x in dir1:
        ent.append(calculate_entropy(path + x))
        n.append(name)
    dict1 = {'Entropy': ent, 'Algorithm': n}
    return dict1


def make_entropy_dict():
    data = make_dataset(dna, 'dna')
    dic = {'Entropy': data['Entropy'], 'Algorithm': data['Algorithm']}
    data = make_dataset(log, 'log')
    dic['Entropy'] = dic['Entropy'] + data['Entropy']
    dic['Algorithm'] = dic['Algorithm'] + data['Algorithm']
    data = make_dataset(rubix, 'rubix')
    dic['Entropy'] = dic['Entropy'] + data['Entropy']
    dic['Algorithm'] = dic['Algorithm'] + data['Algorithm']
    data = make_dataset(lorenz, 'lorenz')
    dic['Entropy'] = dic['Entropy'] + data['Entropy']
    dic['Algorithm'] = dic['Algorithm'] + data['Algorithm']
    return dic

print(make_entropy_dict())