🤖 BOTGP-AUTO - Telegram Pack Transformer
BOTGP-AUTO es un bot de automatización para Telegram desarrollado en Python con la librería Telethon. Permite capturar, procesar y reenviar mensajes de "packs" de juegos entre canales de forma automática.

🚀 Funcionalidades Principales
Monitoreo Automático: Escucha mensajes nuevos en canales específicos.

Extracción con Regex: Identifica IDs, listas de juegos y precios base.

Lógica de Negocio: Calcula automáticamente el precio final (Descuento + Comisión).

Limpieza de Texto: Elimina información irrelevante para un formato más profesional.

🛠️ Configuración del Entorno
1. Variables de Envío (.env)
Para que el bot funcione de forma segura, crea un archivo .env en la raíz del proyecto con esta estructura:

API_ID = tu_id_aqui

API_HASH = tu_hash_aqui

SESSION_NAME = BotGP

[!IMPORTANT]
Nunca subas tu archivo .env a GitHub. Asegúrate de que esté incluido en tu .gitignore.

2. Instalación de Dependencias
Ejecuta este comando en tu terminal:

pip install telethon python-dotenv

🎮 Instrucciones de Uso
Ejecución en Desarrollo
Para correr el script directamente:

python main.py

Creación del Ejecutable (.exe)
Para generar el binario de Windows:

pyinstaller --onefile --console --name "BotGP" main.py

📁 Estructura del Proyecto
main.py: Código fuente principal.

.env: Configuración privada (ignorada por Git).

.gitignore: Filtro de seguridad.

README.md: Esta documentación.

👤 Autor
Jorge Diaz - @JARD1

Institución: Altagracia Informática

Rol: Desarrollador / Estudiante de Computación

Este proyecto fue desarrollado con fines educativos y de automatización personal.
