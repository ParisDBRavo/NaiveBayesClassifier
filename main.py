import csv
import math
from FuncionesDeObtener import obtenerValores
from FuncionesDeObtener import obtenerN
from FuncionesDeObtener import obtNVar
from FuncionesDeObtener import obtTitulos
from FuncionesDeObtener import scoreTotal
#-----------------------------------------------------------------------------------------------------
#Abro el archivo y calculo N y Ncaravan en el cual como N es constante para los calculos y ahora solo 
#nos enfocamos en carvan van a ser variables globales
#-----------------------------------------------------------------------------------------------------
csvFile= csv.reader(open('tic_training.csv', "r"), delimiter = ",")
N, NCaravan =obtenerN(csvFile)
#-----------------------------------------------------------------------------------------------------
#Vuelvo a abrir el archivo por alguna razón python no guardaba csvFile una vez usado en alguna función
#Por lo que hay lineas repetidas de csvFile
#También en la varibale titulos pongo el head del archivo que me servirá para guardar los txt
#-----------------------------------------------------------------------------------------------------
csvFile= csv.reader(open('tic_training.csv', "r"), delimiter = ",")
titulos = obtTitulos(csvFile)
#-----------------------------------------------------------------------------------------------------
#Creo Todos donde voy a guardar todos los resultados y pongo su header
#-----------------------------------------------------------------------------------------------------
file = open("Todos.txt", "w+")
file.writelines(["Variable,","Valor,","Nx,","Ncx,","Nc,","N,", "P(C),", "P(C|X),","Epsilon,", "Score\n"])
#-----------------------------------------------------------------------------------------------------
#Itero sobre los titulos para obtener los datos de las varibales que empiezan con M ya que son las que se 
#utilizarán para los calculos
#-----------------------------------------------------------------------------------------------------
for i in range(1, len(titulos)+1):
#-----------------------------------------------------------------------------------------------------
#En lista obtengo una lista de todos los valores de un tipo por ejemplo de MOSTTYPE después a su vez 
#guardo los resultados de cada categoria en su propio archivo aparte de guardarlos en el total
#-----------------------------------------------------------------------------------------------------
    csvFile= csv.reader(open('tic_training.csv', "r"), delimiter = ",")
    lista =obtenerValores(csvFile,i)
    #csvFile= csv.reader(open('tic_training.csv', "r"), delimiter = ",")
    file1 = open(titulos[i-1]+".txt","w+")
    file1.writelines(["Variable,","Valor,","Nx,","Ncx,","Nc,","N,", "P(C),", "P(C|X),","Epsilon,", "Score\n"])
    #scoreTotal = 0.0

    for element in lista:
#-----------------------------------------------------------------------------------------------------
#Para cada categoria y su respectivo tipo calculo el número total que hay en el archivo grande y 
#También el numero dado Caravan y la categoría lo calculo. Con estos valores ya obtengo 
#-----------------------------------------------------------------------------------------------------
        csvFile= csv.reader(open('tic_training.csv', "r"), delimiter = ",")
        NVar , NVarCar = obtNVar(csvFile, element, i)
    #print(NVar,NVarCar)
        epsilon = NVar*(NVarCar/NVar- NCaravan/N)/(math.sqrt(NVar*(NCaravan/N*(1-NCaravan/N))))
#-----------------------------------------------------------------------------------------------------
#Escribí esta condición para cuando NvarCar fuera igual a 0 ya que comprometía el resultado del log
#Hablando con mi compañera podría usarse mejores técnicas como darle un NAN
#-----------------------------------------------------------------------------------------------------
        if NVarCar != 0:
            score = math.log((NVarCar/NCaravan)/((NVar-NVarCar)/(N-NCaravan)))
        else: 
            score = math.log(((NVarCar+0.5)/(NCaravan+0.5*2))/((NVar-NVarCar)/(N-NCaravan)))
        file1.writelines([titulos[i-1] ,",",str(element),",",str(NVar) ,",",str(NVarCar),",", str(NCaravan), ",",\
            str(N),",",str(NCaravan/N),"," ,str(NVarCar/NVar),",",str(epsilon) ,",",str(score),"\n"])

        file.writelines([titulos[i-1] ,",",str(element),",",str(NVar) ,",",str(NVarCar),",", str(NCaravan), ",",\
            str(N),",",str(NCaravan/N),"," ,str(NVarCar/NVar),",",str(epsilon) ,",",str(score),"\n"])
    file1.close()
    with open(titulos[i-1]+".txt", 'r') as f:
        data = f.read()
        with open(titulos[i-1]+".txt", 'w') as w:
            w.write(data[:-1])
file.close()
#-----------------------------------------------------------------------------------------------------
#Calculo el ScoreTotal
#-----------------------------------------------------------------------------------------------------
csvFile= csv.reader(open('tic_test.csv', "r"), delimiter = ",")
scoreTotal(titulos,csvFile, NCaravan/N)

    #if(row[0]=='NID'):
        #print(row)
