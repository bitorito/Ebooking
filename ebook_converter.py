""" convertir epub
		ebook-convert 'La mujer fugitiva - Alicia Gimenez Bartlett.epub' 'La mujer fugitiva - Alicia Gimenez Bartlett.azw3'
 
 sacar portada
		ebook-meta 'La mujer fugitiva - Alicia Gimenez Bartlett.epub' --get-cover 'cover.jpg'
		
 sacar opf
		ebook-meta 'La mujer fugitiva - Alicia Gimenez Bartlett.epub' --to-opf 'metadata.opf'		
	"""