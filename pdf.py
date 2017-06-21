"""
This is a demo of creating a pdf file with several pages,
as well as adding metadata and annotations to pdf files.
"""
import os
import datetime
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt
from modelos import *
# Create the PdfPages object to which we will save the pages:
# The with statement makes sure that the PdfPages object is closed properly at
# the end of the block, even if an Exception occurs.

class GeneradorPdf:

    def __init__(self, estadisticas = None):
        self.promedios = estadisticas.get('promedios_totales')

    def getPdf(self):
        assert self.promedios
        with PdfPages('simulacion.pdf') as pdf:

            """plt.figure(figsize=(3, 3))
            plt.hist([1,2,3,2,2,4,2,1,2])
            plt.title('Demandas Instatisfechas')
            pdf.savefig()  # saves the current figure into a pdf page
            plt.close()"""
            p = self.promedios
            labels = 'Demandas Satisfechas', 'Demandas Insatisfechas'

            demoras_empl = p.get('cant_demandas_sin_atender_por_demoras_empl')
            demoras_stock = p.get('cant_demandas_sin_atender_por_falta_stock')
            demandas_insatisfechas = demoras_empl + demoras_stock
            total_demandas = p.get('promedio_total_demandas')
            demandas_satisfechas = total_demandas -demandas_insatisfechas
            
            colors = ['white', 'red', 'lightcoral', 'gold']

            texto = "Total de Demandas: %d \n Insatisfechas %d \n Satisfechas %d"%(total_demandas,demandas_insatisfechas, demandas_satisfechas)
            sizes = [demandas_satisfechas, demandas_insatisfechas]
            explode = (0, 0.2)  # only "explode" the 2nd slice (i.e. 'Hogs')
            fig1, ax1 = plt.subplots()
            ax1.set_title('Analisis de Demandas', bbox={'facecolor':'0.9', 'pad':5})  
            plt.text( 0.7,0.8, texto)
            ax1.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=115)
            ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
            plt.gca().set_aspect('1')

            resumen = "[ Configuracion ] \nAnios Simulados: %d \nDias Simulados: %d \nMeses Simulados: %d \nHoras Prod.xDia: %d \nDias Prod.xMes: %d \nCant.Empleados: %d \nTiempo Atencion 1: %d \nTiempo Atencion 2: %d" %(2,5,4,7,8,6,4,3) 
            plt.text( -1.5,-1.3, resumen, horizontalalignment='left', bbox={'facecolor':'red', 'alpha':0.4, 'pad':25})
           


            pdf.savefig()  # saves the current figure into a pdf page
            plt.close()

            texto = "Total Dem. Insatis: %d \n Por Empleados %d \n Por Stock %d"%(demandas_insatisfechas, demoras_empl, demoras_stock)
            labels = 'Demoras Por Empleados', 'Demoras Por Stock'
            sizes = [demoras_empl,demoras_stock]
            explode = (0, 0.2)  # only "explode" the 2nd slice (i.e. 'Hogs')
            fig1, ax1 = plt.subplots()
            ax1.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=112)
            ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
            ax1.set_title('Dem Insatisfechas', bbox={'facecolor':'0.9', 'pad':5})  
            plt.text( 0.7,0.8, texto)
            pdf.savefig()  # saves the current figure into a pdf page
            plt.close()

            d = pdf.infodict()
            d['Title'] = 'Simulacion MyS2017'
            d['Author'] = u'Nicoc'
            d['Subject'] = 'Simulacion de fabrica de autopartes'
            d['Keywords'] = 'PdfPages multipage keywords author title subject'
            d['CreationDate'] = datetime.datetime(2009, 11, 13)
            d['ModDate'] = datetime.datetime.today()
            
            os.spawnv(os.P_NOWAIT, '/usr/bin/atril', ['atril', 'simulacion.pdf'])


if __name__ == '__main__':
    result = Simulacion(default=True).iniciar()
    estadisticas = Estadisticas().getEstadisticas(result)
    g = GeneradorPdf(estadisticas).getPdf()
