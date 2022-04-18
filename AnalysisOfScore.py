file1 = open("ScoreTotal.txt","r+")
lineas = file1.readlines()
linea = []
for item in lineas:
    linea.append(item.split(','))
#print (linea)
#Tres propuestas de división cuando ScoreTotal=0
#No necesito ordenarlos
#Cuando ScoreTotal= max-min/N
#Necesito ordenarlos
#Cuando Scoretotal los primeros 500
#Necesito ordenarlos
linea.remove(['ID','Score\n'])
for element in linea:
    element[1] =element[1].replace("\n","")
import numpy as np
nplinea = np.asarray(linea)
sorted = nplinea[np.argsort(nplinea[:,1])]
del nplinea
sorted= sorted[::-1]
div5=float(sorted[499][1])
#print(sorted)
del sorted

print(div5)
minimo = float(linea[0][1])
maximo = float(linea[0][1])
N =0
media = 0
for element in linea:
    N=N+1
    if float(element[1]) > maximo:
        maximo = float(element[1])
    if float(element[1]) <  minimo:
        minimo = float(element[1])
    media = float(element[1])+ media
media = media/N
print(maximo,minimo, media)
file1 = open("ScoreTotalResultados00.txt","w+")
file1.writelines(['ID,','Score,', 'Resultado Cero,','Resultado Media,','Resultado 500\n'])
count = 0
for element in linea:
    if float(element[1]) > 0:
        variable = 1
    else:
        variable = 0
    if float(element[1]) > media:
        #print(element[1])
        varm=1
    else:
        varm=0
    if float(element[1]) > div5:
        count = count+1
        var5=1
    else:
        var5=0
    file1.writelines([element[0],',', element[1].replace("\n",""),',', str(variable),",",str(varm),",",str(var5),"\n"])
print(count)