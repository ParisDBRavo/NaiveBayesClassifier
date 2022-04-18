import math
def obtenerN(csvFile1):
    contador = 0
    contador1= 0
    for row in csvFile1:
        contador = contador+1
        x = len(row)
        if row[x-1] == '1':
            contador1= contador1+1    
    return contador-1, contador1

def obtenerValores(csvFile1, indice):
    datos =[]
    for row in csvFile1:
        if row[0]!= "NID":
            if int(row[indice]) not in datos:
                datos.append(int(row[indice]))
    datos =sorted(datos)
    return datos
def obtNVar(csvFile1, numero, indice):
    cont = 0
    cont1 = 0
    for row in csvFile1:
        if row[0]!= "NID":
            if int(row[indice]) == numero:
                cont = cont+1
            if row[len(row)-1] == '1' and int(row[indice]) == numero:
                cont1= cont1+1
    return cont, cont1
    
def obtTitulos(csvFile):
    for element in csvFile:
        if element[0] == "NID":
            titulo = element
    #print(titulo)
    #print(titulo)
    titulobueno = []
    for elements in titulo:
#        if elements.startswith('M'):
#            titulobueno.append(elements)
        if(elements != 'CARAVAN'):
            titulobueno.append(elements)
    titulobueno.remove('NID')
    #print(titulobueno)
    return titulobueno

def scoreTotal(titulo, csvFile, Pc):
    scoret=0
    file1 = open("ScoreTotal.txt","w+")
    file1.writelines(["ID,", "Score", "\n"])
    for row in csvFile:
        if row[0] != 'NID':
            for i in range(1,len(titulo)+1):
                valor = row[i]
                file1 = open(titulo[i-1]+".txt","r+")
                lineas = file1.readlines()
                linea =[]
                for item in lineas:
                    linea.append(item.split(','))
                #print(linea[0])
                for element in linea:
                    #print(element)
                    #print(element[0], valor)
                    if element[1]== valor:
                        scoret = scoret+float(element[9])
                    #print(row[0], scoret)
            #print(row[0], str(scoret))
            file1 = open("ScoreTotal.txt","a")
            file1.writelines([row[0],',',str(scoret+math.log(Pc/(1-Pc))),"\n"])
            scoret = 0

    return scoret