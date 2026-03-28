# 🤖 BOTGP-AUTO - Telegram Pack Transformer

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Telegram](https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)

**BOTGP-AUTO** es un bot de automatización para Telegram. Permite capturar, procesar y reenviar mensajes de "packs" de juegos entre canales de forma automática, aplicando lógicas de precios y limpieza de texto.

---

## ⚡ Uso Rápido (Sin instalar Python)

Si solo quieres usar el bot y ya tienes el archivo ejecutable (`BotGP.exe`), sigue estos pasos:

1. Coloca el archivo `BotGP.exe` en una carpeta vacía.
2. En esa misma carpeta, crea un archivo de texto llamado **exactamente** `.env` y ábrelo con el Bloc de notas.
3. Pega tus credenciales de Telegram dentro del archivo `.env` con este formato:
   ```env
   API_ID=tu_api_id_real
   API_HASH=tu_api_hash_real
   SESSION_NAME=BotGP
   ```
4. Haz doble clic en `BotGP.exe`. La primera vez te pedirá tu número de teléfono y código de Telegram para iniciar sesión.

> [!IMPORTANT]
> **Nunca** compartas tu archivo `.env` ni el archivo `BotGP.session` que se genera automáticamente. Quien los tenga, tendrá acceso a tu cuenta.

---

## 💻 Para Desarrolladores (Código Fuente)

Si deseas modificar el código o compilarlo tú mismo, necesitarás [Python 3.8+](https://www.python.org/downloads/).

### 1. Instalación de Dependencias
Abre tu terminal en la carpeta del proyecto y ejecuta:
```bash
pip install telethon python-dotenv
```

### 2. Ejecución en Desarrollo
Para correr el script directamente desde el código:
```bash
python main.py
```

### 3. Creación del Ejecutable (.exe)
Si haces cambios y quieres generar un nuevo binario `.exe`, utiliza PyInstaller:
```bash
pip install pyinstaller
pyinstaller --onefile --console --name "BotGP" main.py
```
*El nuevo ejecutable se guardará dentro de la carpeta `/dist`.*

---

## 🚀 Funcionalidades Principales

* **Monitoreo Automático:** Escucha mensajes nuevos en canales específicos.
* **Extracción con Regex:** Identifica IDs, listas de juegos y precios base.
* **Lógica de Negocio:** Calcula automáticamente el precio final (Descuento + Comisión).
* **Limpieza de Texto:** Elimina información irrelevante para un formato más limpio.

---

## 👤 Autor

* **Jorge Diaz** - [@JARD1](https://github.com/JARD1)
* **Institución:** UNEXCA
* **Rol:** Desarrollador / Estudiante de Informática

---
*Este proyecto fue desarrollado con fines educativos y de automatización personal.*
