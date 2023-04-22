import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
import pickle

data = pd.read_csv('dataset.csv')
x = data.iloc[:, 1:-1]
y = data.iloc[:, -1]


x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=5)

print(x)

from sklearn.preprocessing import StandardScaler

st_x = StandardScaler()
x_train = st_x.fit_transform(x_train)
x_test = st_x.transform(x_test)
pickle.dump(st_x, open('sc.pkl', 'wb'))

from sklearn.svm import SVC  # "Support vector classifier"

classifier = SVC(kernel='rbf', random_state=1)
classifier.fit(x_train, y_train)

pickle.dump(classifier, open('svc.pkl', 'wb'))

y_pred = classifier.predict(x_test)

import sklearn.metrics as mt
acc = mt.classification_report(y_true=y_test, y_pred=y_pred)
print(acc)
print(y_pred)
dict1 = {'Entropy':[7.6954], 'Energy':[0.00631481], 'Contrast':[10], 'Correlation':[0.00301259], 'Homotogcneity': [0.01680847], 'MSE': [121], 'PSNR': [10.4]}
df = pd.DataFrame.from_dict(dict1)
y_pred1 = classifier.predict(df)
print(y_pred1)