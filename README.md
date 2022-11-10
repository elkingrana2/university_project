# university_project

Sistema web para administrar una universidad y formulario de contacto, con Django

## Despliegue en tu propio ordenador



Se debe tener instalado django y python

```bash
% pip install python 3.6.8
% pip install Django = 3.2.13
```

Para hacer funcionar el programa en tu propio ordenador:
```bash
% rm db.sqlite3
% python3 manage.py makemigrations
% python3 manage.py migrate
% python3 manage.py runserver
```

## Despliegue en Python Anywhere

Tendrás que haber creado una cuenta en Python Anywhere, y seleccionado
un plan de pago. Para realizar el despliegue de tu práctica, puedes
seleccionar el plan gratuito ("Beginner").

Una vez estés en tu cuenta, busca la pestaña "Dashboard",
abre una nueva consola bash, y en ella, clona el repositorio:

```bash
$ git clone https://github.com/elkingrana2/university_project.git
$ python3 -m venv .virtualenvs/code
$ source ~/.virtualenvs/code/bin/activate
(code) $ pip install Django==3.0.3
```

Ahora, en la pestaña "Web", pulsa sobre "Add a new web app",
selecciona "Manual configuration", y luego "Python 3.7"
(o la versión que corresponda con la que usaste en el
entorno virtual que montaste).

En este punto puedes comprobar que el sitio está arriba,
con la configuración por defecto (un programa "Hello world"
muy simple), cargando en tu navegador la url de tu 
instancia, normalmente http://"nombre".pythonanywhere.com
(siendo `"nombre"` el nombre de tu instancia).

En la pestaña "Web", busca el sitio donde se puede especificar
el directorio con tu código (en la sección "Code"),
y anota en él el directorio
(tal y como has clonado el código en PythonAnywhere) en el que
tienes tu proyecto Django. En nuestro caso,
`/home/elkin09/university_project`,
o el que corresponda a la versión de `django-youtube` que 
quieras que se lance en tu instancia.
Haz lo mismo para el "working directory" (tendrás que especificar
el mismo directorio).

En la pestaña "Web", busca el fichero de configuración WSGI,
normalmente /var/www/"nombre"_pythonanywhere_com_wsgi.py
(siendo `"nombre"` el nombre de tu instancia).
Edítalo (para editarlo, puedes pulsar directamente sobre
su nombre),
haciendo los siguientes cambios
(ten en cuenta que es un fichero Python).

* Comenta la función `application` (que es la función que
produce la página web "Hello World" que has visto en tu
instancia), porque la vamos a sustituir por nuestra aplicación.

* En la sección `DJANGO`, descomenta el código que viene en el
fichero, indicando el camino al proyecto Django
que quieres que sirva tu instancia (variable `path`).
En nuestro caso, `/home/elkin09/university_project`
(o la versión de `django-youtube` que quieras que se lance),
siendo `"nombre"` el nombre de tu instancia.

* En la misma seccion, indica el nombre de tu fichero `settings.py`,
como módulo Python (por ejemplo, si el directorio donde está dentro
de tu prouecto se llama `project`, el módulo será `project.settings`).
Esto lo pondrás en la asignación `os.environ['DJANGO_SETTINGS_MODULE']=`.

Cuando hayas terminado, guarda el fichero (botón "Save", arriba a la derecha).

En la pestaña "Web", busca el sitio donde se puede especificar
el entorno virtual, e indica el camino (path) al que
creaste (en nuestro caso, `/home/"nombre"/.virtualenvs/code`).

En el fichero `settings.py` del proyecto Django que va a servir tu instancia,
añade el nombre de la instancia a `ALOWED_HOSTS`.
Para editarlo, puedes usar la pestaña "Files".
La lista (que normalmente está vacía) te debería quedar así:

```
ALLOWED_HOSTS = ['elkin09.pythonanywhere.com']
```

No olvides pulsar "Save" cuando hayas terminado de editar el fichero.

Por último, antes de lanzar la aplicación, necesitamos crear la
base de datos inicial. En el entorno virtual que creamos antes,
en el directorio del proyecto, ejecuta:

```bash
% python3 manage.py makemigrations
% python3 manage.py migrate
```

No tendrás que ejecutar `manage.py runserver`, porque eso lo hará
PythonAnywhere por ti. Para que lo haga,
en la pestaña "Web", relanza la aplicación de tu instancia
(botón "Reload").

Ahora ya podrás visitar la url de tu instancia, y si todo ha ido bien,
verás tu aplicación funcionando, contenta, en ella.
