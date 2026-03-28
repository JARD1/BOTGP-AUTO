# 🤖 BOTGP-AUTO - Telegram Pack Transformer

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Telegram](https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)

**BOTGP-AUTO** es un bot de automatización para Telegram desarrollado en **Python** con la librería **Telethon**. Permite capturar, procesar y reenviar mensajes de "packs" de juegos entre canales de forma automática.

---

## 🚀 Funcionalidades Principales

* **Monitoreo Automático:** Escucha mensajes nuevos en canales específicos.
* **Extracción con Regex:** Identifica IDs, listas de juegos y precios base.
* **Lógica de Negocio:** Calcula automáticamente el precio final (Descuento + Comisión).
* **Limpieza de Texto:** Elimina información irrelevante (como tamaños de archivo) para un formato más limpio.

---

## 🛠️ Configuración del Entorno

### 1. Variables de Entorno (`.env`)
Para que el bot funcione de forma segura, crea un archivo `.env` en la raíz del proyecto:

```env
API_ID=tu_api_id_real
API_HASH=tu_api_hash_real
SESSION_NAME=BotGP
```

> [!IMPORTANT]
> **Nunca** subas tu archivo `.env` a GitHub. Asegúrate de que esté incluido en tu `.gitignore`.

### 2. Instalación de Dependencias
```bash
pip install telethon python-dotenv
```

---

## 🎮 Instrucciones de Uso

### Ejecución en Desarrollo
Para correr el script directamente:
```bash
python main.py
```

### Creación del Ejecutable (.exe)
Si deseas usar el bot en una computadora sin Python instalado, genera el binario con:
```bash
pyinstaller --onefile --console --name "BotGP" main.py
```

---

## 📁 Estructura del Proyecto

* `main.py`: Código fuente principal del bot.
* `.env`: Archivo de configuración privada (no incluido en el repo).
* `.gitignore`: Filtro de seguridad para archivos sensibles.
* `README.md`: Documentación del proyecto.

---

## 👤 Autor

* **Jorge Diaz** - [@JARD1](https://github.com/JARD1)
* **Institución:** UNEXCA
* **Rol:** Desarrollador / Estudiante de Informática

---
*Este proyecto fue desarrollado con fines educativos y de automatización personal.*
