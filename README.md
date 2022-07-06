# All-Cripto
Portal de noticias del mundo cripto, con tutoriales bien pensados para aquellos que estén iniciandose en este mundo
## Instalación
Primero es importante crear la carpeta base o directorio principal donde se van a almacenar tanto el proyecto de scrapy como los archivos de django, que los dos se encuentren en el mismo nivel

Esto se hace con mkdir (nombre de la carpeta) o  dentro de la carpeta a usar si ya la tienes creada

1. Luego ejecutar en consola:

En Windows: py -m venv venv

En Linux: sudo pip3 install virtualenv

2. Activar el entorno virtual con:

En Windows: venv\Scripts\activate

En Linux: source /venv/bin/activate

3. Asegurate de tener activado el entorno virtual, en tu consola aparecerá la palabra venv o env al lado del directorio actual

Descargar con pip las dependencias:

pip install Django

pip install scrapy

pip install scrapy-djangoitem. Esta extensión de los items de scrapy la veremos a profundidad más adelante

pip install beautifulsoup4

pip install django-extensions

4. Una vez instaladas las dependencias en el directorio principal ejecutar en consola

scrapy startproject (nombre de tu proyecto)

django-admin startproject (nombre de tu proyecto)

