def  get_folder_tree(folder_path):  #tbd fix this functionality
    import os
    tree = {}

    for root,dirs,files in os.walk(folder_path):
        root = root.split('\\')[-1]
        if tree.get(root):
            tree[root].append(*[{dirs: []}, files])
        else:
            tree[root] = [{dir: [] for dir in dirs}, files]
    a=0


def open_excelDB():
    import subprocess
    program = r'C:\Program Files (x86)\LibreOffice\program\scalc.exe'
    file =r'C:\Users\rvida\Personal\PROXECTOS\03-Ebooking\ScriptDevel\rexistro_libros.xlsx'
    subprocess.call([program, file] )


get_folder_tree(r'C:\Users\rvida\Personal\PROXECTOS\03-Ebooking\ScriptDevel\Output')