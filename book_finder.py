#USO:
### 1) CREAR CARPETA "..\\Input" CON DIRECTORIOS A ORDENAR
### 2) MIRAR LO DE LOS MODULOS DE CALIBRE (me raia agora memso)
### 3) CORRER SCRIPT:
######  Percorre ..\\Input  dende mais adentor cara a fora
######  Comproba structura (struc_checking.file_cheker) 
######  ..> If consistnecy:   genera directorio ordenado en Output y mueve arhcivos y genera covers
######  ..> If not consistency....

#TBD:
## Comentar bien punto2
## Generar Disorder
## Ver como solventar disorder (probablemente reconvertir con {cmd+calibre})


#serve para correr a primeira vez e para 
import struc_checking
import os
import shutil
import subprocess

main_root = os.path.dirname(__file__)
input_root = f'{main_root}\\Input'
output_root = f'{main_root}\\Output'
disorder_root = f'{main_root}\\Disorder'


input_formats = ["pdf","epub"]      #solo ten que aver un formato de input
output_formats= ["azw3"]      #teñen que cumplirse todos os de saída



# Abre la consola de PowerShell

def env_cmd_pwsh(comando):
    subprocess.run('powershell.exe ' + comando, shell=False,)
 
    # proceso.communicate()


for root, dirs, files in os.walk(input_root, topdown=True):             #primer paseo: mover file a output_root//disorder_root
    for direc in dirs:
        metadata, consistency, target_files= struc_checking.file_checker(files, root, input_formats, output_formats,)

        if consistency:
            aim_route= f'{output_root}\\{metadata["autor"]}\\{metadata["titulo"]}'
            for target in target_files:  
                try:                                                    #si existe el directorio copia aqui     
                    shutil.copy(root+"\\"+target, aim_route+"\\"+target)
                except FileNotFoundError:                               #sino crea el directorio y pega
                    os.makedirs(os.path.dirname( aim_route+"\\"+target), exist_ok=True)
                    if ".ods" in target: shutil.copy(root+"\\"+target,aim_route+"\\"+metadata["titulo"+".ods"])
                    else: shutil.copy(root+"\\"+target,aim_route+"\\"+target)
                    #               output_root+"\\"+"\\".join(root.split("\\")[-2:]))
            cd_command= f"cd '{aim_route}'"
            #para saber mais sobre o seguinte comando:  https://manual.calibre-ebook.com/generated/en/ebook-meta.html
            get_cover_command= f"ebook-meta '{target_files[2]}' --get-cover '{target_files[2].split(".")[0]}.jpg'"         
            env_cmd_pwsh(cd_command+ ";" +get_cover_command)

            a=0

        else:
            None
            

        # movemos a ruta ordenada
                    #   shutil.move(root,
                    #               output_root+"\\"+"\\".join(root.split("\\")[-2:]))




# for root, dirs, files in os.walk(library_root, topdown=True):   #segundo paseo: borrar todo directorio vacio en library_root
#     for dir in dirs:
#         path = os.path.join(root, dir)
#         if not os.listdir(path):
#             os.rmdir(path)






