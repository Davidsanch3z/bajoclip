# README

# Proyecto de Descarga de Videos desde Redes Sociales (BajaClip)

## Descripción
**BajaClip** es una aplicación web desarrollada con Flask y yt-dlp que permite descargar videos de redes sociales como Facebook, Instagram y Twitter. Los usuarios pueden proporcionar la URL del video y la aplicación lo descargará en formato MP4 para su posterior visualización o almacenamiento.

Este proyecto fue creado para demostrar habilidades en desarrollo web utilizando tecnologías como Python, Flask, y herramientas de descarga como yt-dlp.

## Tecnologías Utilizadas

- **Flask**: Framework ligero de Python para el desarrollo de aplicaciones web.
- **yt-dlp**: Herramienta de descarga de videos que soporta múltiples plataformas de redes sociales, como YouTube, Facebook, Instagram y Twitter.
- **HTML/CSS**: Para el diseño y maquetación de la interfaz de usuario.
- **JavaScript**: Para mejorar la interactividad en el lado del cliente.
- **FFmpeg**: Utilizado para convertir los videos descargados a formato MP4, si es necesario.
- **Bootstrap**: Para proporcionar un diseño responsivo y limpio en la interfaz de usuario.

## Instalación

### 1. Clonar el repositorio

Clona este repositorio en tu máquina local:

git clone https://github.com/tu_usuario/bajaclip.git
2. Instalar dependencias
Crea un entorno virtual y activa el entorno. Luego, instala las dependencias necesarias:

bash
Copiar código
# Crear entorno virtual (si no lo tienes)
python -m venv venv

# Activar entorno virtual
# En Windows
venv\Scripts\activate
# En macOS/Linux
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt
3. Instalar FFmpeg
Para que el proyecto funcione correctamente con la conversión de videos a formato MP4, necesitas tener FFmpeg instalado en tu sistema.

Windows: Descargar FFmpeg
macOS/Linux: Puedes instalar FFmpeg usando Homebrew (macOS) o apt (Linux):
bash
Copiar código
brew install ffmpeg # macOS
sudo apt install ffmpeg # Linux
4. Ejecutar la aplicación
Una vez que hayas instalado todas las dependencias, puedes ejecutar la aplicación con el siguiente comando:

bash
Copiar código
python app.py
Accede a la aplicación desde tu navegador visitando http://127.0.0.1:5000/.

Uso
Ingresa la URL de un video de redes sociales en el campo correspondiente de la página de inicio.
Haz clic en el botón "Descargar" para iniciar la descarga del video.
El video será descargado en formato MP4.
Estructura de Archivos
graphql
Copiar código
bajaclip/
│
├── app.py                # Código principal de la aplicación Flask
├── downloads/            # Carpeta donde se guardan los videos descargados
├── static/
│   ├── css/
│   │   └── styles.css    # Archivos CSS para el diseño
│   └── js/
│       └── script.js     # Archivos JavaScript (si es necesario)
├── templates/
│   └── index.html        # Plantilla HTML principal
└── requirements.txt      # Dependencias del proyecto
Contribuciones
Si deseas contribuir al proyecto, sigue estos pasos:

Haz un fork del repositorio.
Crea una nueva rama (git checkout -b feature/nueva-funcionalidad).
Realiza tus cambios y confirma los cambios (git commit -am 'Añadir nueva funcionalidad').
Haz un push a la rama (git push origin feature/nueva-funcionalidad).
Crea un Pull Request.
Licencia
Este proyecto está bajo la licencia MIT. Consulta el archivo LICENSE para más detalles.



Este archivo README ahora incluye:

- Descripción general del proyecto.
- Tecnologías utilizadas.
- Instrucciones para la instalación y uso.
- Estructura de archivos.
- Cómo contribuir al proyecto.
- El código fuente de la aplicación Flask (`app.py`).
