import openpyxl
import string


wb = openpyxl.load_workbook(filename = 'rexistro_libros.xlsx')
wba = wb.active
row_numb = 1
ebook_library = {}
categories = []

def get_row(row:int, init:bool = False):#->str,dict:
    if init:
        for let in string.ascii_uppercase[2:]:
            tag = wba[f'{let}{row_numb}'].value
            if not tag: break
            categories.append((let,wba[f'{let}{row_numb}'].value))
        return None #{cat: [] for cat in categories}
    
    else:
        autor = wba[f'B{row_numb}'].value
        info = {tag: wba[f'{let}{row_numb}'].value for let,tag in categories}
        return autor, info



get_row(row_numb, True)
autor = True
# ebook_library[""] = wba[f'B{row_numb}'].value, wba[f'C{row_numb}'].value
while autor:
    row_numb+=1
    autor,info = get_row(row_numb)
    a=0
    if not ebook_library.get(autor): 
        pass# TBD ebook_library[autor] = [titulo]
    else:
        pass# TBD   ebook_library[autor].append(titulo) 

    

for key in ebook_library:
    print(f'{key}:  {ebook_library[key]}')

