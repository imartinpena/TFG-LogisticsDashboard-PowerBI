### Manual de Usuario para el Script de Conversión de CSV a Excel

#### Requisitos Previos:
1. Tener instalado Python.
2. Asegurarse de que la biblioteca `pandas` esté instalada. Si no, se puede instalar usando el comando `pip install pandas`.

#### Instrucciones de Uso:
1. Abrir una terminal o línea de comandos.
2. Navegar al directorio donde se encuentra el script `CSVtoEXCEL.py`.
3. Ejecutar el script utilizando el comando:
   ```
   python CSVtoEXCEL.py ruta_al_archivo_CSV ruta_de_salida_para_el_archivo_Excel
   ```
   Donde:
   - `ruta_al_archivo_CSV`: es la ruta completa donde se encuentra el archivo `.csv` que deseas convertir.
   - `ruta_de_salida_para_el_archivo_Excel`: es la ruta del directorio donde deseas guardar el archivo `.xlsx` resultante.

#### Ejemplo de Uso:
Supongamos que tienes un archivo llamado `FY18CW00.csv` en tu escritorio y deseas guardar el Excel convertido en una carpeta llamada `Output` también en el escritorio. El comando sería:
```
python CSVtoEXCEL.py C:\Users\TuUsuario\Desktop\FY18CW00.csv C:\Users\TuUsuario\Desktop\Output
```

#### Salida Esperada:
Después de ejecutar el script, deberías ver un mensaje en la terminal que indica que el archivo se ha convertido y guardado exitosamente, proporcionando la ruta del archivo. Si ocurre algún error, se mostrará un mensaje con la descripción del error para ayudarte a resolverlo.

Este manual facilita la comprensión y uso del script para cualquier usuario, incluso sin conocimientos avanzados en programación, permitiendo la conversión eficiente de datos de formatos `.csv` a `.xlsx`.