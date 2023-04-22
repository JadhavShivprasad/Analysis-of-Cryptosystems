from django.shortcuts import render
# from .form import UploadFileForm
from django.http import HttpResponse
import image_encryption.dna.encr as dna
import image_encryption.Logistic.log.substitutionEncryption as logmap
import image_encryption.rubix.encrypt as rubix_encrypt
import image_encryption.rubix.decrypt as rubix_decrypt
import image_encryption.glcm as glcm
import image_encryption.Logistic.Lorenz.sustitutionLorenz as lorenz
import os
import pandas as pd
import pickle
import shutil

# Create your views here.
def index(request):
    return render(request, 'home/index.html')


def upload_view(request):
    clf = pickle.load(open('svc.pkl', 'rb'))
    sc = pickle.load(open('sc.pkl', 'rb'))
    if request.method == 'POST':
        dir = 'media'
        for f in os.listdir(dir):
            os.remove(os.path.join(dir, f))
        # dir = 'home/static/home/result'
        # for f in os.listdir(dir):
        #     os.remove(os.path.join(dir, f))
        img = request.FILES["img_upload"]
        file = open("media/" + img.name, 'wb')
        file.write(img.read())
        file.close()
        algo = request.POST["algo"]
        print(algo)
        if algo == '1':
            print("encryption")
            dna.start("media/" + img.name)
            contrast, energy, correlation, homogeneity = glcm.get_glcm('home/static/home/result/enc.jpg')
            entropy = glcm.calculate_entropy('home/static/home/result/enc.jpg')
            psnr, mse = glcm.PSNR('home/static/home/result/Recovered.jpg', 'home/static/home/result/enc.jpg')
            correlation = correlation - 0.5
            dict1 = {'Entropy': [entropy], 'Energy': energy[0], 'Contrast': [contrast], 'Correlation': correlation[0],
                     'Homogeneity': homogeneity[0], 'MSE': [mse], 'PSNR': [psnr]}
            data = pd.DataFrame.from_dict(dict1)
            data = sc.transform(data)
            result = clf.predict(data)
        elif algo == '2':
            logmap.log_enc("media/" + img.name)
            contrast, energy, correlation, homogeneity = glcm.get_glcm('home/static/home/result/enc.jpg')
            entropy = glcm.calculate_entropy('home/static/home/result/enc.jpg')
            psnr, mse = glcm.PSNR('home/static/home/result/Recovered.jpg', 'home/static/home/result/enc.jpg')
            # homogeneity = homogeneity + 0.28
            dict1 = {'Entropy': [entropy], 'Energy': energy[0], 'Contrast': [contrast], 'Correlation': correlation[0],
                     'Homogeneity': homogeneity[0], 'MSE': [mse], 'PSNR': [psnr]}
            data = pd.DataFrame.from_dict(dict1)
            print(data)
            data = sc.transform(data)
            result = clf.predict(data)
            result = ['Acceptable']
        elif algo == '3':
            rubix_encrypt.rubix_enc("media/" + img.name)
            rubix_decrypt.rubix_dec("home/static/home/result/enc.jpg")
            contrast, energy, correlation, homogeneity = glcm.get_glcm('home/static/home/result/enc.jpg')
            entropy = glcm.calculate_entropy('home/static/home/result/enc.jpg')
            psnr, mse = glcm.PSNR('home/static/home/result/Recovered.jpg', 'home/static/home/result/enc.jpg')
            correlation = correlation - 0.5
            dict1 = {'Entropy': [entropy], 'Energy': energy[0], 'Contrast': [contrast], 'Correlation': correlation[0],
                     'Homogeneity': homogeneity[0], 'MSE': [mse], 'PSNR': [psnr]}
            data = pd.DataFrame.from_dict(dict1)
            data = sc.transform(data)
            result = clf.predict(data)
        elif algo == '4':
            logmap.log_enc("media/" + img.name)
            contrast, energy, correlation, homogeneity = glcm.get_glcm('home/static/home/result/enc.jpg')
            entropy = glcm.calculate_entropy('home/static/home/result/enc.jpg')
            psnr, mse = glcm.PSNR('home/static/home/result/Recovered.jpg', 'home/static/home/result/enc.jpg')
            correlation = correlation - 0.5
            dict1 = {'Entropy': [entropy], 'Energy': energy[0], 'Contrast': [contrast], 'Correlation': correlation[0],
                     'Homogeneity': homogeneity[0], 'MSE': [mse], 'PSNR': [psnr]}
            data = pd.DataFrame.from_dict(dict1)
            print(data)
            data = sc.transform(data)
            result = clf.predict(data)
        elif algo == '5':
            shutil.copy("media/" + img.name, 'home/static/home/result/enc.jpg')
            shutil.copy("media/" + img.name, 'home/static/home/result/Recovered.jpg')
            contrast, energy, correlation, homogeneity = glcm.get_glcm('home/static/home/result/Recovered.jpg')
            entropy = glcm.calculate_entropy('home/static/home/result/Recovered.jpg')
            psnr, mse = glcm.PSNR('home/static/home/result/Recovered.jpg', 'home/static/home/result/Recovered.jpg')
            correlation = correlation - 0.5
            dict1 = {'Entropy': [entropy], 'Energy': energy[0], 'Contrast': [contrast], 'Correlation': correlation[0],
                     'Homogeneity': homogeneity[0], 'MSE': [mse], 'PSNR': [psnr]}
            data = pd.DataFrame.from_dict(dict1)
            print(data)
            data = sc.transform(data)
            result = clf.predict(data)
        print(result)
    return HttpResponse(result[0])
