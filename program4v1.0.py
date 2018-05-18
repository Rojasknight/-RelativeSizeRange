# !/usr/bin/python 
# -*- coding: UTF-8 -*-
#################################################################################
# Nombre del programa:  program4_v1.0                                           #  
# Correo Electronico:   afarable-1997@hotmail.com                               #
# Fecha:                14/05/2018                                              #
# Descripción:          Programa encargado de realizar calcular la tabla de     #
#                       tamaños relativos                                       #
#################################################################################

__author__ = 'Danny Rojas Reyes'
__version__ = 'program4_v1.0.py'

from math import log, pow, sqrt, exp
import os


""" Descripción de la clase
#Nombre: Operation                                                                                       
#Descripción: se ejecutaran las distintas operaciones para llevar a 
#             cabo  tabla de tamaños relativos de una tabla de proxy   
#Constructor: Operation()
#Parámetros del constructor:  null

#Metodos: 3(xDivY, logLnXi, average, variance )
"""

class Operation:

    array_aux = list() 

    def xDivY(self, x, y):
        return round((x / float(y)), 4)   
        
    def logLnXi(self, data):
        return round(log(float(data)), 4)

    def average(self, array):
        return round(sum(array) / len(array), 4);
    
    def variance(self, lnXi, avg):
        for item in lnXi:
            self.array_aux.append(round(pow(item - avg, 2), 4))
        return round(sum(self.array_aux) / float((len(lnXi)) - 1), 4)



""" Descripción de la clase                                                              
#Nombre: InputData                                                                                       
#Descripción: se ejecutaran en primera instancia para instanciar la clase Operation      
#Constructor: InputData()
#Parámetros del constructor:  null

#Metodos: 1(main)
"""

class InputData():
    def main():

        operations = Operation();
        option = 0;
        avg = 0;

        srcX = list()
        srcY = list()
        const_xDivY = list()
        const_ln = list()

        print "**********Digita una opcion**********"
        print "1. Calcular la tabla de tamanos relativos de la tabla de Proxy"
        print "2. Calcular la tabla de tamanos relativos del libro"
        option = int(raw_input('#>'))
        

        if(option == 1):
            srcX = [18,18,25,31,37,82,82,87,89,230,85,87,558]
            srcY = [3,3,3,3,3,5,4,4,4,10,3,3,10]
            
        elif option == 2:
            srcY = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
            srcX = [7,12,10,12,10,12,12,12,12,8,8,8,20,14,18,12]
        else:
            print "[x] Opcion no valida, intenta de nuevo..."
        

        for item in range(len(srcX)):
            const_xDivY.append(operations.xDivY(srcX[item], srcY[item]))
        
        for item in range(len(srcX)):
            const_ln.append(operations.logLnXi(const_xDivY[item]))

        avg = operations.average(const_ln)
        print "Media: " + str(avg);
        variance = operations.variance(const_ln, avg);
        print "Variance: " + str(variance);
        standar_dev = sqrt(variance)
        print "Dev Standar" + str(round(standar_dev, 4))
        print "--------------------------------"
        print "ln(VS) => " + str(round(exp(avg - (2 * standar_dev)), 4)) 
        print "ln(S) => "  + str(round(exp(avg - standar_dev), 4))
        print "ln(M) => "  + str(round(exp(avg), 4))
        print "ln(L) => "  + str(round(exp(avg + standar_dev), 4))
        print "ln(VL) =>" + str(round(exp(avg + (2 * standar_dev)), 4)) 

    if __name__ == '__main__':
        os.system('cls')
        main()