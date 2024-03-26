#TBD:
# 1)CORRECT TBDS IN FILEs and SUBFILEs

### SECTION: imports
import subprocess
import os

#classes dfined here
import libs._LibaryState
import libs._EbookTarget



### SECTION: GLOBAL DEFS
main_root = os.path.dirname(__file__)
input_root = f'{main_root}\\Input'
output_root = f'{main_root}\\Output'
disorder_root = f'{main_root}\\Disorder'

libre_office_calc_pth = f''
excel_db_pth = f'main_root\\rexistro_libros.xlsx'



def call_excel_db():
    program = libre_office_calc_pth
    file = excel_db_pth
    try:  
        subprocess.call([program, file] )
    
    except:   #tbd select type of error
        raise SystemError('Cant find Libreoffice on this computer')
    state_machine["Fail"]


state_machine = {    "Obetener estado Lib":      (read_excel(), save_prestate()),
                        "Conversion en Masa":       (calibre_convert(), save_prestate()),
                        "Abrir Lib.DB":             (call_excel_db()),  #flux blocked until excel closed
                        "Comparar estados Lib":     (read_excel(), compare_and_get()),
                        "Operar kindle":            (copiar_kindle(), borrar_kindle()),
                        "Fail":                     (close())
}
## main  ##
                                                     

