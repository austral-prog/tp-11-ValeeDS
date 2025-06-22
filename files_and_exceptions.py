def read_file_to_dict(filename):
    """Lee un archivo de ventas donde cada venta es producto:valor_de_venta;... y agrupa los valores por producto en una lista.

    :param filename: str - nombre del archivo a leer.
    :return: dict - diccionario con listas de montos por producto.
    :raises: FileNotFoundError - si el archivo no existe.
    """
    import csv

    csv_data = []

    try:
        with open(filename, "r") as f:
            csv_reader = csv.reader(f, delimiter=';')
            for row in csv_reader:
                csv_data = row

    except FileNotFoundError:
        raise FileNotFoundError("Error: The file does not exist.")

    ventas = dict()

    for reg in csv_data:
        info = ( reg[ : reg.find(":") ] , reg[ reg.find(":")+1 : ] )
        if info[0] in ventas.keys() and info[0] != '':
            ventas[info[0]].append(float(info[1]))
        elif info[0] != '':
            ventas[info[0]] = [float(info[1])]

    return ventas


def process_dict(data):
    """Para cada producto, imprime el total de ventas y el promedio, en el orden natural del diccionario.

    :param data: dict - diccionario a procesar.
    :return: None
    """
    for prod, ventas in data.items():
        tot = sum(ventas)
        prom = tot / len(ventas)

        print(f"{prod}: ventas totales ${tot:.2f}, promedio ${prom:.2f}")