# flask_api_example

A simple Flask API example packaged with setuptools.

## Installation

1. Create a virtual environment:

    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```

2. Install the package:

    ```bash
    pip install -e .
    ```

## Usage

Run the API with:

```bash
flask_api_example


Con esta estructura, el proyecto es fácil de gestionar, empacar y compartir.

## Empaquetado del Proyecto

Para crear el archivo de distribución del proyecto (como `.whl` o `.tar.gz`), sigue estos pasos:

1. Asegúrate de que tienes `wheel` instalado:

    ```bash
    pip install wheel
    ```

2. Ejecuta el siguiente comando para generar el empaquetado:

    ```bash
    python setup.py sdist bdist_wheel
    ```

Esto generará los archivos de empaquetado en el directorio `dist/`, incluyendo:

- Un archivo `.whl`
- Un archivo `.tar.gz`

## Instalación del Paquete

Para instalar el paquete en un nuevo entorno virtual y probarlo:

1. Desactiva el entorno actual si está activado:

    ```bash
    deactivate
    ```

2. Crea un nuevo entorno virtual para la prueba:

    ```bash
    python3 -m venv test_env
    source test_env/bin/activate
    ```

3. Instala el paquete desde el archivo `.whl` o `.tar.gz` en `dist/`:

    ```bash
    pip install dist/flask_api_example-1.0.0-py3-none-any.whl
    ```

4. Ejecuta el comando para iniciar la API:

    ```bash
    flask_api_example
    ```

Si todo está configurado correctamente, la API debería ejecutarse y estar lista para recibir solicitudes.

## Uso

Puedes probar la API enviando una solicitud HTTP. Si estás usando la estructura básica de ejemplo, la API debería estar ejecutándose en `http://127.0.0.1:5000`.

## Contribuciones

Si deseas contribuir a este proyecto, por favor sigue los siguientes pasos:

1. Haz un fork del proyecto.
2. Crea una nueva rama (`git checkout -b feature/nueva-funcionalidad`).
3. Haz commit de tus cambios (`git commit -m 'Añadir nueva funcionalidad'`).
4. Sube los cambios (`git push origin feature/nueva-funcionalidad`).
5. Abre un Pull Request.

---

¡Gracias por usar Flask API Example!