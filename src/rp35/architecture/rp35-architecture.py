import sys

import config_loader
from diagrams import Cluster, Diagram, Edge
from diagrams.onprem.client import Client
from diagrams.onprem.compute import Server
from diagrams.onprem.database import Oracle

ambiente = sys.argv[1]

# Cargar y obtener la configuración modificada
config = config_loader.cargar_configuracion(ambiente)

# Crear el diagrama y los objetos Cliente, Server y Oracle
with Diagram(name="Ambiente puesto rapipago (" + ambiente.upper() + ")", show=True):
    puesto = Client(label="Puesto 3.5")
    
    with Cluster("Service level1"):
        recargas = Server(config["recargas"])
        transacciones = Server(config["transacciones"])
        puma = Server(config["puma"])

    with Cluster("Rapipago"):
        oracle = Oracle(config["oracle"])

    with Cluster("Service level2"):
        hermes = Server(config["hermes"])
        ws = Server(config["ws"])
        sto = Server(config["sto"])
    
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