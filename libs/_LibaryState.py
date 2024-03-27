import openpyxl
import string



class LibraryState:
    def __init__(self,excelDB_path, folder_path, ):#...)  #TBD
        self.excelDB = openpyxl.load_workbook(filename = excelDB_path)
        self.folder_path = folder_path
       
        self.status_enum =  ('Unchecked', 'New Books', 'All paired', 'Something Wrong')
        self.status = self.status_enum[0]
        
    def get_folder_tree(self):
        pass



wb = openpyxl.load_workbook(filename = 'rexistro_libros.xlsx')
wba = wb.active

ebook_library = {}
categories = []


def get_row(row:int, init:bool = False):#->str,dict:
    if init:
        for let in string.ascii_uppercase[2:]:
            tag = wba[f'{let}{row}'].value
            if not tag: break
            categories.append((let,wba[f'{let}{row}'].value))
        return None #{cat: [] for cat in categories}
    
    else:
        autor = wba[f'B{row}'].value
        info = {tag: [wba[f'{let}{row}'].value] for let,tag in categories}
        return autor, info



def read_library_database(wb):
    ## This function reads, the excel lirary, and build a dictionary
    ## with structured data of excel content
    
    row_numb = 1
    get_row(row_numb, True)
    autor = True

    while autor:
        row_numb+=1
        autor,info = get_row(row_numb)
        if not ebook_library.get(autor): 
            ebook_library[autor] = info
        else:
            for field in info:
                ebook_library[autor][field].append(info[field][0])


    for key in ebook_library:
        print(f'{key}:  {ebook_library[key]}')

    return ebook_library, categories



def write_excel_database(wb, books_register):

    row_numb=1
    for autor in books_register: 
        books_register[autor]   = set(books_register[autor] ) 
        for titulo in books_register[autor]:
            row_numb+=1
            wba[f'B{row_numb}'].value = autor
            wba[f'C{row_numb}'].value = titulo
            a=0
    wb.save(filename = 'rexistro_libros.xlsx')