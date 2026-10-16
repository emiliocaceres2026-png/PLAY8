import time
import random
import asyncio
import threading
from datetime import datetime, timedelta
from telethon import TelegramClient

# ---------------- CONFIGURACIÓN USERBOT ----------------
API_ID = 30776682
API_HASH = 'd2e9ad1c3dda250716a24a73d77ae6a6'

CANALES = ['@AVIATORPKA', 't.me/+oFnrUl2VKhU1YWJh', 'https://t.me/aviatordo'] 

LINK_ADMIN = 'https://t.me/apkpredictor'
LINK_VIP = 'https://t.me/+oFnrUl2VKhU1YWJh'
LINK_FREE = 'https://www.apkpredictoraviator.com'

# --- EMOJIS PREMIUM ---
E_ESTRELLA = '<tg-emoji emoji-id="5370784581341422520">⭐️</tg-emoji>'
E_GAFAS = '<tg-emoji emoji-id="5235684778727974441">😎</tg-emoji>'
E_PULGAR = '<tg-emoji emoji-id="5393130162311157022">👍</tg-emoji>'
E_FLECHA = '<tg-emoji emoji-id="5429651785352501917">↗️</tg-emoji>'
E_BOLSA = '<tg-emoji emoji-id="5453901475648390219">🛍</tg-emoji>'
E_COHETE = '<tg-emoji emoji-id="5188481279963715781">🚀</tg-emoji>'
E_DIVISAS = '<tg-emoji emoji-id="5377336227533969892">💱</tg-emoji>'
E_ADN1 = '<tg-emoji emoji-id="5215621964286142449">🧬</tg-emoji>'
E_REGALO = '<tg-emoji emoji-id="5215668908278686541">🎁</tg-emoji>'
E_ADN2 = '<tg-emoji emoji-id="5215673679987355184">🧬</tg-emoji>'
E_DIAMANTE = '<tg-emoji emoji-id="6059684519437405439">💎</tg-emoji>'

PLATAFORMAS = [
     {"nombre":"ECUABET", "pais":f"{E_DIAMANTE} ECUADOR {E_DIAMANTE}"},
     {"nombre":"DORADOBET", "pais":f"{E_DIAMANTE} GLOBAL {E_DIAMANTE}"},
     {"nombre":"BETPLAY", "pais":f"{E_DIAMANTE} COLOMBIA {E_DIAMANTE}"},
     {"nombre":"RUSBETH", "pais":f"{E_DIAMANTE} GLOBAL {E_DIAMANTE}"},
     {"nombre":"BETSON", "pais":f"{E_DIAMANTE} GLOBAL {E_DIAMANTE}"},
     {"nombre":"BETMEXICO", "pais":f"{E_DIAMANTE} MÉXICO {E_DIAMANTE}"},
     {"nombre":"1XBET", "pais":f"{E_DIAMANTE} GLOBAL {E_DIAMANTE}"},
     {"nombre":"1WIN", "pais":f"{E_DIAMANTE} GLOBAL {E_DIAMANTE}"}
]

lock_telethon = threading.Lock()

def enviar_mensajes_premium(lote_mensajes):
    with lock_telethon:
        async def _send():
            client = TelegramClient('sesion_premium', API_ID, API_HASH)
            await client.connect()
            for canal_id, texto in lote_mensajes:
                try:
                    await client.send_message(canal_id, texto, parse_mode='html', link_preview=False)
                    print(f"✅ {canal_id}: Mensaje enviado exitosamente.")
                except Exception as e:
                    print(f"❌ Error enviando a {canal_id}: {e}")
                await asyncio.sleep(3)
            await client.disconnect()
        
        asyncio.run(_send())

# ----------------- HILO PROMOCIONAL (CADA 8 MINUTOS) -----------------
def hilo_info_8_minutos():
    while True:
        time.sleep(8 * 60)
        
        texto_promo = (
            f"{E_ESTRELLA} <b>HOLA</b> {E_ESTRELLA} {E_GAFAS}\n"
            f"{E_PULGAR} <b>MUCHO GUSTO MI NOMBRE ES</b> {E_PULGAR}\n\n"
            f"  {E_FLECHA} <b>WILLIAM ROBERT</b> {E_FLECHA}\n\n"
            f"{E_BOLSA} TE COMENTO CÓMO TRABAJAMOS, {E_COHETE} Y SÍ TE INTERESA ME CONFIRMAS, NOSOTROS TRABAJAMOS {E_DIAMANTE} 40% {E_DIAMANTE} {E_DIVISAS} 60% {E_DIVISAS} DE LAS GANANCIAS QUE SE OBTENGAN YA QUE TRABAJAMOS CON APLICACIONES PREDICTOR QUE NOS INDICAN CADA SECUENCIA Y CADA ALGORITMO QUE ESTEMOS LLEVANDO A CABO YA QUE  MANEJAMOS RESULTADOS {E_DIAMANTE} 100% {E_DIAMANTE} EFECTIVOS SI TE INTERESA TRABAJAR CON NOSOTROS ME CONFIRMA {E_FLECHA}\n\n\n"
            f"{E_ADN1} <b>PRIEMERO GANAS LUEGO PAGAS MANEJAMOS UN RESULTADO 100% SEGURO Y CONFIABLE</b> {E_ADN1}\n\n\n"
            f"{E_COHETE} <b>AVIATOR</b> {E_COHETE}\n\n"
            f"{E_REGALO} <b>SPACEMAN</b> {E_REGALO}\n\n"
            f"{E_DIAMANTE} <b>LUCKY JET</b> {E_DIAMANTE}\n\n\n"
            f"{E_GAFAS} {E_ESTRELLA} ESCRÍBANME AL PRIVADO SI DESEAN MÁS INFORMACIÓN {E_ESTRELLA} {E_GAFAS}\n\n\n\n"
            f"       {E_ESTRELLA} <a href='{LINK_ADMIN}'><b>ADMIN TELEGRAM</b></a> {E_ESTRELLA}\n\n"
            f"       {E_PULGAR} <a href='{LINK_ADMIN}'><b>CONTACTAR</b></a> {E_PULGAR}"
        )
        
        lote_promo = [(canal, texto_promo) for canal in CANALES]
        print("\n[+] Enviando Info Promocional (Ciclo 8 min)...")
        enviar_mensajes_premium(lote_promo)

# ----------------- HILO PUBLICIDAD (ENVÍA AL INICIO Y LUEGO CADA 25 MIN) -----------------
def hilo_publicidad_25_minutos():
    while True:
        texto_publi = (
            f"{E_ESTRELLA} <b>HOLA</b> {E_ESTRELLA} {E_GAFAS}\n"
            f"{E_PULGAR} <b>MUCHO GUSTO MI NOMBRE ES</b> {E_PULGAR}\n\n"
            f"  {E_FLECHA} <b>WILLIAM ROBERT</b> {E_FLECHA}\n\n"
            f"{E_BOLSA} TE COMENTO CÓMO TRABAJAMOS, {E_COHETE} Y SÍ TE INTERESA ME CONFIRMAS, NOSOTROS TRABAJAMOS {E_DIAMANTE} 40% {E_DIAMANTE} {E_DIVISAS} 60% {E_DIVISAS} DE LAS GANANCIAS QUE SE OBTENGAN YA QUE TRABAJAMOS CON APLICACIONES PREDICTOR QUE NOS INDICAN CADA SECUENCIA Y CADA ALGORITMO QUE ESTEMOS LLEVANDO A CABO YA QUE  MANEJAMOS RESULTADOS {E_DIAMANTE} 100% {E_DIAMANTE} EFECTIVOS SI TE INTERESA TRABAJAR CON NOSOTROS ME CONFIRMA {E_FLECHA}\n\n\n"
            f"{E_ADN1} <b>PRIEMERO GANAS LUEGO PAGAS MANEJAMOS UN RESULTADO 100% SEGURO Y CONFIABLE</b> {E_ADN1}\n\n\n"
            f"{E_COHETE} <b>AVIATOR</b> {E_COHETE}\n\n"
            f"{E_REGALO} <b>SPACEMAN</b> {E_REGALO}\n\n"
            f"{E_DIAMANTE} <b>LUCKY JET</b> {E_DIAMANTE}\n\n\n"
            f"{E_GAFAS} {E_ESTRELLA} ESCRÍBANME AL PRIVADO SI DESEAN MÁS INFORMACIÓN {E_ESTRELLA} {E_GAFAS}\n\n\n\n"
            f"       {E_ESTRELLA} <b>ADMIN TELEGRAM</b> {E_ESTRELLA}\n\n"
            f"       {E_PULGAR} <a href='{LINK_ADMIN}'><b>CONTACTAR</b></a> {E_PULGAR}"
        )
        
        lote_publi = [(canal, texto_publi) for canal in CANALES]
        print("\n[+] Enviando Publicidad de confirmación...")
        enviar_mensajes_premium(lote_publi)
        
        time.sleep(25 * 60)

# ----------------- HILO DE SEÑALES (CICLO EXACTO DE 15 MIN) -----------------
def ejecutar_ciclo_canales():
    inicio_ciclo = datetime.now()
    plataformas_ronda = random.sample(PLATAFORMAS, len(CANALES))

    print(f"\n--- INICIANDO RONDA DE SEÑALES ({inicio_ciclo.strftime('%H:%M:%S')}) ---")

    mensajes_a_enviar = []

    for i, canal_id in enumerate(CANALES):
        seleccion = plataformas_ronda[i]
        
        t1 = inicio_ciclo + timedelta(minutes=random.randint(3, 5))
        t2 = t1 + timedelta(minutes=random.randint(5, 7))

        h1 = t1.strftime('%I:%M %p')
        h2 = t2.strftime('%I:%M %p')
        x1 = round(random.uniform(1.65, 2.15), 2)
        x2 = round(random.uniform(1.65, 2.15), 2)

        texto = (
            f"<b>{seleccion['pais']}</b>\n\n"
            f"{E_ESTRELLA} ATENCIÓN {E_ESTRELLA}      {E_COHETE} SEÑALES {E_COHETE}\n\n"
            f"            {E_BOLSA} <b>{seleccion['nombre']}</b> {E_BOLSA}\n\n"
            f"                {E_FLECHA} <b>{x1}x</b> {E_FLECHA}\n"
            f"            {E_ADN1} <b>{h1}</b> {E_ADN1}\n\n"
            f"                {E_FLECHA} <b>{x2}x</b> {E_FLECHA}\n"
            f"            {E_ADN1} <b>{h2}</b> {E_ADN1}\n\n"
            f"        {E_REGALO} BUENA SUERTE {E_REGALO}\n"
            f"{E_DIAMANTE}{E_ESTRELLA}{E_COHETE}{E_PULGAR}{E_DIVISAS}{E_ADN2}{E_DIAMANTE}{E_ESTRELLA}{E_COHETE}{E_PULGAR}\n\n"
            f"              {E_GAFAS} <a href='{LINK_ADMIN}'><b>ADMIN</b></a> {E_GAFAS}\n\n"
            f"          {E_DIAMANTE} <a href='{LINK_VIP}'><b>GRUPO VIP</b></a> {E_DIAMANTE}\n\n"
            f"        {E_REGALO} <a href='{LINK_FREE}'><b>AVIATOR FREE</b></a> {E_REGALO}"
        )
        
        mensajes_a_enviar.append((canal_id, texto))

    enviar_mensajes_premium(mensajes_a_enviar)
    
    proximo_ciclo = inicio_ciclo + timedelta(minutes=15)
    return proximo_ciclo

# ----------------- INICIO DEL SISTEMA -----------------
client_test = TelegramClient('sesion_premium', API_ID, API_HASH)
client_test.start()
client_test.disconnect()

print("🚀 BOT PREMIUM ACTIVO (SEÑALES AL INSTANTE + PUBLICIDAD DE ARRANQUE)")

threading.Thread(target=hilo_publicidad_25_minutos, daemon=True).start()
threading.Thread(target=hilo_info_8_minutos, daemon=True).start()

while True:
    try:
        hora_proximo_ciclo = ejecutar_ciclo_canales()
        print(f"⌛ Ciclo de Señales enviado. El próximo arranca EXACTAMENTE a las ({hora_proximo_ciclo.strftime('%H:%M:%S')})...")
        
        while datetime.now() < hora_proximo_ciclo:
            time.sleep(10) 
            
    except KeyboardInterrupt:
        print("\n🛑 Detenido por el usuario.")
        break
    except Exception as e:
        print(f"⚠️ Error global: {e}")
        time.sleep(30)
