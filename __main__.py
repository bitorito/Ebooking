
MaquinaDeEstados = {    "Obetener estado Lib":      (read_excel(), save_prestate()),
                        "Conversion en Masa":       (calibre_convert(), save_prestate()),
                        "Abrir Lib.DB":             (open_lib_db()),  #flux blocked until excel closed
                        "Comparar estados Lib":     (read_excel(), compare_and_get()),
                        "Operar kindle":            (copiar_kindle(), borrar_kindle()



## main  ##

