## CHANGELOG
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
