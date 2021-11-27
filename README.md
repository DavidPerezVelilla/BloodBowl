#Descripción:

Web dedicada a este divertido juego de mesa. En ella podras consultar su reglamento, tiendas donde poder comprarte un equipo e incluso jugar. 
Tambien cuenta con un apartado donde podras crear tu propio equipo, consultarlo (junto con muchos otros) y ver los jugadores que lo componen.

Para crear este gestor, he creado 3 modelos: 
 - Equipo: nombre, raza (clave ajena en refenrecia a Razas), descripcion, imagen e icono.
 - Razas: nombre
 - Jugadores: nombre, equipo (clave ajena en refenrecia a Equipo), coste, movimiento, fuerza, agilidad, pase, armadura y habilidades.
 
#Instalación:

- En la consola* nos posicionaremos en la carpeta donde queramos descargar el proyecto
- Una vez alli ejecutaremos el comando git clone con el enlace del codigo (git clone https://github.com/DavidPerezVelilla/BloodBowl.git)
- Nos tendremos que dirigir a la carpeta del proyecto y alli instalaremos Django (py -m pip install Django) y debugtoolbar (pip install django-debug-toolbar)
- Ejecutaremos el servidor (py manage.py runserver)
- Acederemos entonces a la direccion http://localhost:8000/ (o el número que nos indicaran al ejecutar el servidor)
- Para parar el servidor: Ctrl + c en la consola

*Si trabajamos en Windows deberemos usar "GitBash".
