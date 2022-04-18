#Saco más datos de la matriz de confusion
import csv
import numpy as np
csvFile= csv.reader(open('tic_test.csv', "r"), delimiter = ",")
#print(len(next(csvFile)))
#87x5823
file1 = open("ScoreTotalResultados00.txt","r")
lineas = file1.readlines()
Y_pred= np.array([])
Y_test= np.array([])
linea=[]
for item in lineas:
    linea =item.split(',')
    if linea[2]!= 'Resultado Cero':
        Y_pred = np.append(Y_pred,int(linea[4].replace("\n","")))
for row in csvFile:
    if row[0] != 'NID':
        Y_test= np.append(Y_test, int(row[86]))
#Y_pred= arr
#Y_test= np.array([])
print(Y_pred,Y_test)
print(Y_pred.shape,Y_test.shape)
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt
classes_= np.array([0,1])
cm = confusion_matrix(Y_test, Y_pred, labels=classes_)
print(cm)
disp = ConfusionMatrixDisplay(confusion_matrix=cm,display_labels=classes_)
disp.plot()
plt.show()  
from sklearn.metrics import accuracy_score
print ('Accuracy:')
ACC=accuracy_score(Y_test, Y_pred)
print(ACC)
from sklearn.metrics import classification_report
target_names = ['No Caravan', 'Caravan']
print(classification_report(Y_test, Y_pred, target_names=target_names))