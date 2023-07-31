import json

def cargar_configuracion(ambiente):
    archivo_configuracion = "rp35-config-" + ambiente + ".json"
    with open(archivo_configuracion, "r") as file:
        config = json.load(file)

    for key, value in config.items():
        config[key] = value.replace(";", "\n")

    return config



