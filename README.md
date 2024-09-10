
![Logo](https://raw.githubusercontent.com/kedro-org/kedro-brand-identity/main/horizontal/color/kedro-horizontal-color-on-light.svg)

Para poder entrar y ejecutar este proyecto Kedro, se mostrarán las instrucciones o pasos a seguir para configurar el entorno y correr los pipelines.

Instrucciones de instalación
=======================================

## Windows

**Descargar el archivo :** 
Clona o descarga este repositorio en tu máquina local.

( Tambien puedes clonar este repositorio directamente ) 
```http
  git clone https://github.com/Andresilvampuero/machinwow.git
```

**Abrir el proyecto en un editor de código :** Utiliza tu editor de código preferido (VS Code, PyCharm, etc.).

**Crear un entorno virtual :** Usar un entorno virutal es recomendable para no corromper otros proyectos dentro de un sistema
```http
  python -m venv [nombre_entorno]
```

**Activar el entorno virtual :** Hacer funcionar el entorno virtual
```http
  .\.venv\Scripts\activate
```

**Entra a tu entorno virtual :** 
```http
  cd [nombre_entorno]
```
**Instalar Kedro :**
```http
  pip install kedro
```

***(Opcional) Instalar Jupyter Notebook :*** Para visualizar mejor los notebook
```http
  pip install jupyter
```

**Cargar el proyecto en el entorno virtual:** Si no se prefiere clonar el repositorio cargamos manualmente el proyecto

**Entrar al proyecto raiz:** 
```http
  cd machinwow
```
**Entrar al proyecto kedro:** 
```http
  cd wow
```

**Dependencias:** Se instalarán las dependecias necesarias para correr este proyecto
los notebook
```http
  pip install -r requirements.txt
```

**Correr los pipelines del proyecto:**
los notebook
```http
  kedro run
```

***(Opcional) Visualizar el notebook en localhost:*** Si deseas trabajar con notebooks en Jupyter, ejecuta el siguiente comando:
```http
  kedro jupyter notebook
```
## MacOS

**Descargar el archivo :** 
Clona o descarga este repositorio en tu máquina local.

*( Tambien puedes clonar este repositorio directamente )*
```http
  git clone https://github.com/Andresilvampuero/machinwow.git
```

**Abrir el proyecto en un editor de código :** Utiliza tu editor de código preferido (VS Code, PyCharm, etc.).

**Crear un entorno virtual :** Usar un entorno virutal es recomendable para no corromper otros proyectos dentro de un sistema
```http
  python3 -m venv [nombre_entorno]
```

**Activar el entorno virtual :** Hacer funcionar el entorno virtual
```http
  source [nombre_entorno]/bin/activate
```

**Entra a tu entorno virtual :** 
```http
  cd [nombre_entorno]
```
**Instalar Kedro :**
```http
  pip install kedro
```

***(Opcional) Instalar Jupyter Notebook :*** Para visualizar mejor los notebook
```http
  pip install jupyter
```

**Cargar el proyecto en el entorno virtual:** Si no se prefiere clonar el repositorio cargamos manualmente el proyecto

**Entrar al proyecto raiz:** 
```http
  cd machinwow
```

**Entrar al proyecto kedro:** 
```http
  cd wow
```

**Dependencias:** Se instalarán las dependecias necesarias para correr este proyecto
los notebook
```http
  pip install -r requirements.txt
```
**Correr los pipelines del proyecto:**
los notebook
```http
  kedro run
```

***(Opcional) Visualizar el notebook en localhost:*** Si deseas trabajar con notebooks en Jupyter, ejecuta el siguiente comando:
```http
  kedro jupyter notebook
```




#
 


## Posibles Errores

- Verificar si está instalado python
```http
  python --version
```
- Verificar si está instalado kedro
```http
  kedro info
```
- Problemas de privacidad :
Ingresar al PowerShell o algun interfaz de consola con permisos de administrador
```http
  set-executionpolicy unrestricted
```


