import csv
import json

clasificacion = []

with open('listadoRutEmpresa.csv', 'r', newline='') as archivo:
    lectura_csv = csv.DictReader(archivo)
    for fila in lectura_csv :
        
        rut = fila['Rut']
        empresa = fila['Nombre']
        ventas = int(fila['Ventas'])
        clasifica = ""
        
        if ventas < 100000000 :
            clasifica = "Pequenio Contribuyente"
        elif ventas >= 100000001 and ventas < 200000000 :
            clasifica  = "Mediano Contribuyente"
        elif ventas > 200000000 :
            clasifica = "Gran Contribuyente"
        #end if
        
        print(f"La empresa {empresa} de rut {rut} es un {clasifica} ya que sus ventas son de {ventas}")
        
        clasificacion.append({
            'Rut': rut,
            'Nombre Empresa': empresa,
            'Ventas': ventas,
            'Clasificacion Empresa' : clasifica
        })
    #end for
#end open
        
with open('segmentacionEmpresas.json', 'w') as archivo:
    json.dump(clasificacion, archivo, indent=1)
#end open
        