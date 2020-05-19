#importando bibliotecas
import PySimpleGUI as sg
from PIL import Image
from PIL.ExifTags import TAGS
import sys

sg.theme('DarkTeal1') #Tema da interface

#Função principal
def main():
    #Configurando interface
    layout = [[sg.Text('Selecione a imagem ou video')],
            [sg.In(), sg.FileBrowse()],
            [sg.Button('Extrair'), sg.Button('Sair')]]

    window = sg.Window('Lookmetadata', layout)

    while True:  #Loop de eventos
        event, values = window.read()
        if event in (None, 'Sair'):
            break
        if event == "Extrair":
            result = []
            fname = values[0]
            #Lendo imagem com PIL
            image = Image.open(fname)

            #Extrair EXIF
            exifdata = image.getexif()

            #Interagindo com cada EXIF
            for tag_id in exifdata:
                #Pegando tags
                tag = TAGS.get(tag_id, tag_id)
                data = exifdata.get(tag_id)
                #Decodificando dados
                if isinstance(data, bytes):
                    data = data.decode()
                #Adicionando dados ao resultado
                result.append(f"{tag:25}: {data}")
                
            break
            

    window.close()
    if event == "Extrair": #Ativando evento
        resultado(result)


#Interface de resultado
def resultado(result):
    #Configurando interface
    layout1 = [ [sg.Text('Resultado')],
                [sg.Listbox(values=result, size=(40, 20), key='-LIST-', enable_events=True)],
                [sg.Button('Voltar')]]

    window1 = sg.Window('Lookmetadata', layout1)

    while True:  #Loop de evntos
        event, values = window1.read()
        if event in (None, 'Voltar'):
            break

    window1.close() 
    if event == "Voltar":
        main()  

#Começando aplicação
main()     
  