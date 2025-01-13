# pylint: disable=import-outside-toplevel
# pylint: disable=line-too-long
# flake8: noqa
"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""


def pregunta_01():
    """
    La información requerida para este laboratio esta almacenada en el
    archivo "files/input.zip" ubicado en la carpeta raíz.
    Descomprima este archivo.

    Como resultado se creara la carpeta "input" en la raiz del
    repositorio, la cual contiene la siguiente estructura de archivos:


    ```
    train/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    test/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    ```

    A partir de esta informacion escriba el código que permita generar
    dos archivos llamados "train_dataset.csv" y "test_dataset.csv". Estos
    archivos deben estar ubicados en la carpeta "output" ubicada en la raiz
    del repositorio.

    Estos archivos deben tener la siguiente estructura:

    * phrase: Texto de la frase. hay una frase por cada archivo de texto.
    * sentiment: Sentimiento de la frase. Puede ser "positive", "negative"
      o "neutral". Este corresponde al nombre del directorio donde se
      encuentra ubicado el archivo.

    Cada archivo tendria una estructura similar a la siguiente:

    ```
    |    | phrase                                                                                                                                                                 | target   |
    |---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
    |  0 | Cardona slowed her vehicle , turned around and returned to the intersection , where she called 911                                                                     | neutral  |
    |  1 | Market data and analytics are derived from primary and secondary research                                                                                              | neutral  |
    |  2 | Exel is headquartered in Mantyharju in Finland                                                                                                                         | neutral  |
    |  3 | Both operating profit and net sales for the three-month period increased , respectively from EUR16 .0 m and EUR139m , as compared to the corresponding quarter in 2006 | positive |
    |  4 | Tampere Science Parks is a Finnish company that owns , leases and builds office properties and it specialises in facilities for technology-oriented businesses         | neutral  |
    ```


    """



def pregunta_01():

    import zipfile
    import os
    import os
    import pandas as pd
    import os

    zip_path="files/input.zip"
    destino="files/input"

    # Verificar si el archivo zip existe
    if not os.path.exists(zip_path):
        print(f"El archivo {zip_path} no existe.")


    # Descomprimir el archivo zip
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(destino)

    print(f"El archivo se ha descomprimido en la carpeta: {destino}")





    # Ruta base del directorio de entrada
    ruta_directorio = "files/input/input"

    # Listas para almacenar la información
    frases = []
    sentimientos = []
    conjuntos = []

    # Verificar si la ruta base existe
    if not os.path.exists(ruta_directorio):
        print(f"La ruta '{ruta_directorio}' no existe. Asegúrate de descomprimir el archivo ZIP correctamente.")
    else:
        # Recorrer las carpetas `train` y `test`
        for conjunto in ['train', 'test']:
            for sentimiento in ['negative', 'positive', 'neutral']:
                carpeta = f"{ruta_directorio}/{conjunto}/{sentimiento}"  # Usar '/' para las rutas

                if os.path.exists(carpeta):
                    print(f"Procesando carpeta: {carpeta}")
                    # Leer todos los archivos de la carpeta
                    for archivo in os.listdir(carpeta):
                        if archivo.endswith('.txt'):
                            ruta_archivo = f"{carpeta}/{archivo}"  # Usar '/' para las rutas
                            print(f"Leyendo archivo: {ruta_archivo}")

                            # Leer el contenido del archivo
                            with open(ruta_archivo, 'r', encoding='utf-8') as file:
                                frase = file.read().strip()
                            
                            # Agregar los datos a las listas
                            frases.append(frase)
                            sentimientos.append(sentimiento)
                            conjuntos.append(conjunto)
                else:
                    print(f"La carpeta '{carpeta}' no existe.")

        # Crear un DataFrame con los datos recolectados
        df = pd.DataFrame({
            'phrase': frases,
            'target': sentimientos,
            'dataset': conjuntos
        })

        # Imprimir el DataFrame para verificar los resultados
        print("Primeras filas del DataFrame:")
        print(df.head(5))




    # Crear la carpeta de salida si no existe
    output_dir = "files/output"
    os.makedirs(output_dir, exist_ok=True)

    # Filtrar los datos del DataFrame según el conjunto (train o test)
    df_train = df[df['dataset'] == 'train'].drop(columns=['dataset'])
    df_test = df[df['dataset'] == 'test'].drop(columns=['dataset'])

    # Rutas de los archivos CSV
    ruta_train_csv = os.path.join(output_dir, 'train_dataset.csv')
    ruta_test_csv = os.path.join(output_dir, 'test_dataset.csv')

    # Guardar los DataFrames en archivos CSV
    df_train.to_csv(ruta_train_csv, index=False, encoding='utf-8')
    df_test.to_csv(ruta_test_csv, index=False, encoding='utf-8')

    print(f"Archivos CSV guardados exitosamente en la carpeta '{output_dir}':")
    print(f" - {ruta_train_csv}")
    print(f" - {ruta_test_csv}")


