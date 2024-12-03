# Tarea_3_Sistema_Distribuidos

Este proyecto implementa un sistema para recopilar, procesar y almacenar datos de tráfico en tiempo real utilizando un ecosistema de tecnologías basadas en contenedores Docker.

## Requisitos previos

Antes de ejecutar el sistema, asegúrese de tener instalados los siguientes programas:

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

## Configuración inicial

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/tu-usuario/tu-repositorio.git
   cd tu-repositorio
Construir y levantar los contenedores
Desde la raíz del proyecto, ejecute el siguiente comando:
```bash
docker-compose up --build
``````
Este comando hará lo siguiente:

Construirá las imágenes Docker para cada servicio definido.
Iniciará los contenedores de forma concurrente.
Configurará las redes y dependencias entre servicios.
2. **Verificar los servicios**
Una vez que los contenedores estén en ejecución, puede verificar cada servicio accediendo a sus interfaces:
```bash
Spark Master UI: http://localhost:8080
Elasticsearch: http://localhost:9200
Kibana: http://localhost:5601
``````

3. Enviar datos de prueba al sistema
El scrapper comenzará a recopilar datos automáticamente al iniciarse. Estos datos se enviarán a Kafka y pasarán por el flujo de procesamiento configurado.

4. Detener los contenedores
Para detener y eliminar todos los contenedores asociados al proyecto, use:

```bash
docker-compose down
``````
5. Reiniciar en caso de errores
Si encuentra algún problema, reinicie los servicios con:

```bash
docker-compose down
docker-compose up --build
``````

Notas adicionales
Asegúrese de ajustar las configuraciones en los archivos de configuración dentro de las carpetas específicas de cada servicio (por ejemplo, scrapper/requirements.txt, kafka/server.properties, etc.) según sus necesidades.
En caso de querer ampliar la capacidad de los servicios (por ejemplo, aumentar el número de trabajadores Spark o nodos Cassandra), edite el archivo docker-compose.yml.
