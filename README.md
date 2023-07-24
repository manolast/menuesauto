# menuesauto
Script crea los menues automaticamente a partir de un archivo.csv

Se necesita tener instalado python y pip. Haces "pip install selenium" y "pip install pwinput"

como se usa:

- Empezas a correr el script
- Pide inputs de mail y contraseña para iniciar sesion
- Pide input de que país es la cantina (aca no importa mayúsculas)
- Pide input del nombre de la cantina. Sí importan mayúsculas. No es necesario poner el nombre de la cantina completo. (Ejemplo en la cantina "Colegio nombreColegio" se puede poner solo "nombreColegio" respetando la mayuscula y corre igual)
- Pide input del nombre del archivo csv. En realidad refiere al path al archivo. Si esta en la misma carpeta que el script solo se necesita poner el nombre del archivo sin importar mayúsculas y minúsculas (ejemplo archivocsv.csv)
- Despues de ahí busca la cantina y si encuentra se pone a crear menues con los datos que recibe del .csv
