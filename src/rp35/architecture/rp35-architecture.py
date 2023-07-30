from diagrams import Cluster, Diagram, Edge
from diagrams.onprem.compute import Server
from diagrams.onprem.client import Client
from diagrams.onprem.database import Oracle

# Leer el archivo de propiedades y guardar los pares clave-valor en un diccionario
namePropiedades = "rp35.properties"
with open(namePropiedades) as file:
    propiedades = {}
    for line in file:
        clave, valor = line.strip().split("=", 1)
        propiedades[clave] = valor.replace(";", "\n")

# Crear el diagrama y los objetos Cliente, Server y Oracle
with Diagram(name="Ambiente DESA puesto rapipago", show=True):
    puesto = Client(label="Puesto 3.5")
    
    with Cluster("Service level1"):
        recargas = Server(propiedades["recargas"])
        transacciones = Server(propiedades["transacciones"])
        puma = Server(propiedades["puma"])

    with Cluster("Rapipago"):
        oracle = Oracle(propiedades["oracle"])

    with Cluster("Service level2"):
        hermes = Server(propiedades["hermes"])
        ws = Server(propiedades["ws"])
        sto = Server(propiedades["sto"])
    
    # Conectar los objetos utilizando las relaciones definidas en el código original
    puesto >> Edge(color="darkgreen") << puma
    puesto >> Edge(color="darkgreen") << transacciones
    puesto >> Edge(color="darkgreen") << recargas
    recargas >> Edge(color="darkgreen") << hermes
    transacciones >> Edge(color="darkgreen") << ws
    transacciones >> Edge(color="darkgreen") << sto
    hermes >> Edge(color="darkgreen") << oracle
    transacciones >> Edge(color="darkgreen") << oracle
    sto >> Edge(color="darkgreen") << oracle
    ws >> Edge(color="darkgreen") << oracle