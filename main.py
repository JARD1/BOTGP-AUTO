import os
import asyncio
import re
from dotenv import load_dotenv
from telethon import TelegramClient, events

# ==========================================
# CONFIGURACIÓN Y CARGA DE CREDENCIALES
# ==========================================
# Cargamos las variables desde el archivo .env para mantener la seguridad
load_dotenv()

API_ID = int(os.getenv('API_ID'))
API_HASH = os.getenv('API_HASH')
SESION_NAME = os.getenv('SESSION_NAME')

# Canales de origen y destino (puedes moverlos al .env si lo prefieres)
CHAT_FUENTE = '@swichtaccount' 
CHAT_DESTINO = '@GameOverPack_bot' 

# Inicialización del cliente de Telethon con las credenciales cargadas
client = TelegramClient(SESION_NAME, API_ID, API_HASH)

# ==========================================
# LÓGICA DE PROCESAMIENTO
# ==========================================

def transformar_mensaje_pack(mensaje_capturado):
    """
    Analiza el texto del mensaje original, extrae los datos clave
    mediante expresiones regulares (Regex) y aplica la lógica de precios.
    """
    
    # 1. Extracción del ID (Busca 'ID:' y captura letras/números siguientes)
    match_id = re.search(r'ID:\s*([A-Za-z0-9]+)', mensaje_capturado)
    
    # 2. Extracción del Precio (Busca el número antes del símbolo €)
    match_precio = re.search(r'Precio:\s*(\d+)€', mensaje_capturado)
    
    # Validación: Si no encuentra ID o Precio, cancela el proceso
    if not match_id or not match_precio:
        print("❌ Error: No se pudo extraer el ID o el Precio. Formato no reconocido.")
        return None

    pack_id = match_id.group(1)
    try:
        precio_base = int(match_precio.group(1))
    except ValueError:
        return None

    # 3. Extracción y Limpieza de Juegos
    # Delimita el texto entre "Juegos incluidos:" y "Tamaño total:"
    match_juegos = re.search(
        r'Juegos incluidos:(.*?)Tamaño total:', 
        mensaje_capturado, 
        re.DOTALL | re.IGNORECASE
    )
    
    juegos_formato = ""
    if match_juegos:
        juegos_brutos = match_juegos.group(1).strip()
        juegos_lista = juegos_brutos.split('\n')
        
        for juego in juegos_lista:
            juego_limpio = juego.strip()
            if not juego_limpio: continue
            
            # Limpieza: Elimina el tamaño del archivo (ej: "(5.8 gb)") para estética
            juego_limpio = re.sub(r'\s*\([\d\.]+\s*gb\)', '', juego_limpio).strip()
            
            if juego_limpio:
                juegos_formato += f"🎮 {juego_limpio}\n"

    # 4. Cálculo del Nuevo Precio
    # Lógica: Descuento variable según el precio base + comisión de 10€
    descuento = 2 if precio_base >= 20 else 1
    precio_final = precio_base - descuento + 10
    
    # 5. Construcción del Mensaje Final (Plantilla de salida)
    mensaje_final = (
        "💜🎮 GAMEOVER PACK 🎮💜\n"
        f"ID: {pack_id}\n\n"
        f"{juegos_formato}\n"
        f"Precio: {precio_final}€"
    )
    
    return mensaje_final

# ==========================================
# CONTROLADOR DE EVENTOS
# ==========================================

@client.on(events.NewMessage(chats=CHAT_FUENTE))
async def capturar_y_responder(event):
    """
    Se activa cada vez que el CHAT_FUENTE publica un mensaje.
    Transforma el contenido y lo reenvía al CHAT_DESTINO.
    """
    mensaje_capturado = event.message.message
    mensaje_final = transformar_mensaje_pack(mensaje_capturado)
    
    print("-" * 40)
    print(f"📩 Mensaje detectado en {CHAT_FUENTE}")
    
    if mensaje_final:
        # Envío del mensaje procesado al destino
        await client.send_message(CHAT_DESTINO, mensaje_final)
        print("✅ Pack procesado y enviado con éxito.")
        print(f"💰 Precio final calculado: {mensaje_final.split('Precio: ')[-1]}")
    else:
        print("⚠️ El mensaje no cumplía con el formato de 'Pack'. Ignorado.")
    
    print("-" * 40)

# ==========================================
# EJECUCIÓN PRINCIPAL
# ==========================================

async def main():
    # Inicia la sesión del cliente (pide login si es la primera vez)
    await client.start()
    print(f"🚀 BotGP en línea. Escuchando {CHAT_FUENTE}...")
    # Mantiene el script corriendo permanentemente
    await client.run_until_disconnected()

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n🛑 BotGP detenido manualmente por el usuario.")