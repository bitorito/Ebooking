## CHANGELOG

------------------------------------------------------------------------------------------------------------------
## [20240326] Victor
## Engadido
	- __main__.py  --> main file with StateMachine and all calls integrated
	- \libs
		- _EbookTarget.py  --> definicion de clase ebooktarget 		/copiar,renombrar,etc...
		- _LibraryState.py  --> definicion de clase librarystate	/compara,busca regex, cerciora integegridad...
		\old
			-ebook_converter.py, excel_opener.py, struct_chkecing.py, book_finder.py

## Modificado
    - FLOWCHAR.ODG   --> engadidas clases, estrutura de main definida

## TBD 
	- Documentar clases
		- Definir entradas
		- Definir saídas
		- Explicativos metodos
			
	- Complete program structure
	- Get a functional version
	- Prepare Tests

------------------------------------------------------------------------------------------------------------------
## [20240317] Victor
## Engadido
	- rexistro_libros.xlsx  --> excel que sirve como DB
	- excel_opener.py  --> permite operaciones automatizadas sobre {rexistro_libros.xlsx}
	- FLOWCHART.odg  --> esquemas asociados o funcionamento

## Modificado
	
## TBD 
	- {FLOWCHART.odg}
		- perfilar arquivos.py:  
			- IN-OUTS e trafico entre eles
			- xerarquizar arquivos --> ordenar secuencias
			
		- secuenciar operacións a realizar
		- decidir dende onde automatizamos a chamda do script: 
			python como macro de excel
			abrir excel dende python
		
	- {excel_opener.py}:
		- definir escritura de excel
		
	- {struct_checking.py}:
		-aplicar en directorio o arbol de rutas definido por {rexistro_libros.xlsx}
	

------------------------------------------------------------------------------------------------------------------
## [20240223] Victor
## Engadido
	- book_finder.py --> ordena e convirte
    - struc_checking.py --> comproba consistency en función de arquivos in-out e metadata.title
    - ebook_converter.py --> almacena certos comnados de CMD-calibre

## Modificado
    - book_finder.py --> comentarios basicos
