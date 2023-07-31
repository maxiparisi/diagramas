# Parámetros para generar Diagramas de arquitectura RP3.5

- dev ---> diagrama de arquitectura ambiente de desarrollo
- test ---> diagrama de arquitectura ambiente de testing
- homo ---> diagrama de arquitectura ambiente de homologación
- prod ---> diagrama de arquitectura ambiente de producción

Ejemplo para generar el diagrama para desa: 
~~~
python .\rp35-architecture.py dev
~~~

# Para generar png a partir del archivo dot

ir a carptea del archivo que se genera con python y correr algo por el estilo:

~~~

dot -Tpng -o ambiente_desa_puesto_rapipago.png ambiente_desa_puesto_rapipago

~~~
