#TBD:
# 1)CORRECT TBDS IN FILEs and SUBFILEs

### SECTION: imports
import subprocess
import os
import shutil

#classes dfined here
import libs.ExcelDB
import libs.OSoperationst



### SECTION: GLOBAL DEFS
main_root = os.path.dirname(__file__)
input_root = f'{main_root}\\Input\\Biblioteca Gloria'
output_root = f'{main_root}\\Output'
# disorder_root = f'{main_root}\\Disorder'

libre_office_calc_pth = f''
excel_db_pth = f'main_root\\rexistro_libros.xlsx'

                                
            


libs.OSoperationst.collect_epubs(input_root, output_root)