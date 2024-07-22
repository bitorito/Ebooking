
# import methods from book_finder & excel_opener
import os
import shutil

def print_os_structure():
    for root,dirs,files in os.walk(target_path, topdown=False):
        print(f'{"\t"*(len(root.split("\\"))-9)}{root.split("\\")[-1]}' )
        for name in files:
            print(f'{"\t"*(len(root.split("\\"))-8)}{name}' )
        # for name in dirs:
        #     print(f'{"\t"*(len(root.split("\\"))-8)}{name}' )




class TreeLeave:
    """Represents a folder wich contains book files """
    def __init__(self, parent, items):
        self.parent = parent
        self.bookmarks = []
        
        for item in items:
            if ".epub" in item or ".pdf" in item:
                self.name =  item.split(" - ")[0]
                self.source_book = item
            elif ".azw3" in item:
                self.converted_book = item
            elif ".opf" in item:
                self.source_metadata = item
            elif ".sdr" in item:
                self.bookmarks.append(item)
        
        

class TreeBranch:
    """ """
    def __init__(self, parent, item):
        
        self.parent= parent
        self.name = item 
        self.path = os.path.join(parent.path,self.name)
        self.childs = []
        
        for book in os.listdir(self.path):
            self.childs.append(
                TreeLeave(self, os.listdir(os.path.join(self.path,book))))
            


class Treetructure:
    """
    BookStructure is a 3 level book hirecracy:
        _1st: ROOT.     Higher one. It is the folder that contains all authors folders.
        _2nd: BRANCH.   Middle one. It is each author folder, wich contains all of the author's books.
        _3rd: LEAVES.   Lower one.  It is each book folder, wich contains all files related to the book
    """
    def __init__(self):
        self.child = []

    def GenTree_from_files(self, lib_root):
        self.path = lib_root
        for author in os.listdir(target_path):
            if os.path.isfile(  os.path.join(self.path,author)): continue  #skipping files1
            self.child.append(  TreeBranch( self, author)  )
        
                

    def GenTree_from_DB(self, lib_root):     
        pass











target_path = r'C:\Users\rvida\Personal\PROXECTOS\03-Ebooking\ScriptDevel\Input\Biblioteca Gloria'
target_file = r'C:\Users\rvida\Personal\PROXECTOS\03-Ebooking\ScriptDevel\Input\Biblioteca Gloria\Ann Holt\Crepusculo en Oslo (125)\Crepusculo en Oslo - Ann Holt.epub'

tree = Treetructure()
tree.GenTree_from_files(lib_root=target_path)


