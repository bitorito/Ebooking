
from xml.etree import ElementTree as ET
import unicodedata


def file_checker(files: list[str], dir: str,
                input_formats: list[str], output_formats: list[str],):
    ''' 
    file_checker comproba que a estrutura é solida:

        1) metadata.opf Existe   --> extraemos titulo  
        2) existe un ficheiro que compre input_formats   --> file_flags[inputOK] = True
        3) existe un ficheiro que compre output_formats   --> file_flags[inputOK] = True
    '''

    def eliminar_tildes(s):
        return ''.join(c for c in unicodedata.normalize('NFD', s)
                    if unicodedata.category(c) != 'Mn')

    #file checker evalua que se dan as condicións de arquivos correctos
    file_flags = {condition:False for condition in ["inputOK","outputOK"]}    #engadimos condicion de arquivo de saída presentes
    output_files = []

    metadata = None
    for element in files:  #buscar o metadata primeiro
        
        if element.find("opf") != -1:
            target =f'{dir}\\{element}'
            tree = ET.parse(target)  # Parsea el archivo metadata.opf

            # Crea una estructura para almacenar la información
            metadata = {'titulo':eliminar_tildes(tree.find(".//{http://purl.org/dc/elements/1.1/}title").text),
                        'autor':eliminar_tildes(tree.find(".//{http://purl.org/dc/elements/1.1/}creator").text,)}
            output_files.append(eliminar_tildes(element))
            # print(metadata)
    if metadata==None: 
        return None, False, None #Se non hai metadata, paramos


    for element in files:  #para cada elemento
        for checker in input_formats: #percorremos os formatos de entrada e vereficamos que existe entrada
            if element.find(checker)!=-1 and element.find(eliminar_tildes(metadata['titulo']))!=-1: 
                file_flags['inputOK']= True 
                output_files.append(eliminar_tildes(element))
        
        for checker in output_formats: #percorremos os formatos de saida e vereficamos cada un deles
            if element.find(checker)!=-1 and element.find(eliminar_tildes(metadata['titulo']))!=-1: 
                file_flags['outputOK']= True
                output_files.append(eliminar_tildes(element))

    
    # print(file_flags)
    # print(dir)

    if all(list(file_flags.values())):
        return metadata, True, output_files
    else:
        return None,False,None
    
