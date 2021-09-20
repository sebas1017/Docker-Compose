# Docker-Compose

el dockerfile de la raiz es para los puntos desarrollados ejecutando una imagen de ubuntu y el comando figlet con un mensaje 


en el directorio store tenemos un servicio en la carpeta fruits con su respectivo docker file
en el directorio web tenemos el servicio web de apache que renderiza datos provenientes del servicio fruits-service el cual es una api construida en flask que retorna
un json de frutas


estos dos servicios integrados son desplegados utilizando docker-compose up

por lo tanto para ejecutar el proyecto en cualquier maquina clonar este repositorio e ir al directorio store 
una vez ahi ejecutar docker-compose up 

y luego de que este comando se lleve a cabo tendran 2 contenedores corriendo el servicio de apache con php en el puerto 5000 y el servicio fruits-service osea la api en FLASK
en el puerto 5001

por lo tanto podrian ir al navegador en las direcciones

http://localhost:5000
y
http://localhost:5001

y podran ver en ejecucion los 2 servicios 
en el caso de ejecutar esto en la maquin AWS localhost debe ser reemplazado por la direccion ip publica del servidor
