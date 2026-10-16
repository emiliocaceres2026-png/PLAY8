import os
import sys
import time
import random
import asyncio
from datetime import datetime, timedelta
from telethon import TelegramClient

# ---------------- CONFIGURACIÓN USERBOT / BOT ----------------
API_ID = 30776682
API_HASH = 'd2e9ad1c3dda250716a24a73d77ae6a6'

# Si tienes un bot token de BotFather, puedes colocarlo aquí para que no pida login interactivo:
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8932126962:AAGB2AuiHVkV6XtLWiTb-Y7msfpsscYNqB8")

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
    {"nombre": "ECUABET", "pais": f"{E_DIAMANTE} ECUADOR {E_DIAMANTE}"},
    {"nombre": "DORADOBET", "pais": f"{E_DIAMANTE} GLOBAL {E_DIAMANTE}"},
    {"nombre": "BETPLAY", "pais": f"{E_DIAMANTE} COLOMBIA {E_DIAMANTE}"},
    {"nombre": "RUSBETH", "pais": f"{E_DIAMANTE} GLOBAL {E_DIAMANTE}"},
    {"nombre": "BETSON", "pais": f"{E_DIAMANTE} GLOBAL {E_DIAMANTE}"},
    {"nombre": "BETMEXICO", "pais": f"{E_DIAMANTE} MÉXICO {E_DIAMANTE}"},
    {"nombre": "1XBET", "pais": f"{E_DIAMANTE} GLOBAL {E_DIAMANTE}"},
    {"nombre": "1WIN", "pais": f"{E_DIAMANTE} GLOBAL {E_DIAMANTE}"}
]

client = TelegramClient('sesion_premium', API_ID, API_HASH)

async def enviar_lote(lote_mensajes):
    for canal_id, texto in lote_mensajes:
        try:
            await client.send_message(canal_id, texto, parse_mode='html', link_preview=False)
            print(f"[{datetime.now().strftime('%H:%M:%S')}] ✅ {canal_id}: Enviado.")
        except Exception as e:
            print(f"[{datetime.now().strftime('%H:%M:%S')}] ❌ Error en {canal_id}: {e}")
        await asyncio.sleep(3)

async def tarea_promo_8_min():
    while True:
        await asyncio.sleep(8 * 60)
        texto_promo = (
            f"{E_ESTRELLA} <b>HOLA</b> {E_ESTRELLA} {E_GAFAS}\n"
            f"{E_PULGAR} <b>MUCHO GUSTO MI NOMBRE ES</b> {E_PULGAR}\n\n"
            f"  {E_FLECHA} <b>WILLIAM ROBERT</b> {E_FLECHA}\n\n"
            f"{E_BOLSA} TE COMENTO CÓMO TRABAJAMOS, {E_COHETE} Y SÍ TE INTERESA ME CONFIRMAS, "
            f"NOSOTROS TRABAJAMOS {E_DIAMANTE} 40% {E_DIAMANTE} {E_DIVISAS} 60% {E_DIVISAS} DE LAS GANANCIAS "
            f"QUE SE OBTENGAN YA QUE TRABAJAMOS CON APLICACIONES PREDICTOR QUE NOS INDICAN CADA SECUENCIA "
            f"Y CADA ALGORITMO QUE ESTEMOS LLEVANDO A CABO YA QUE MANEJAMOS RESULTADOS "
            f"{E_DIAMANTE} 100% {E_DIAMANTE} EFECTIVOS SI TE INTERESA TRABAJAR CON NOSOTROS ME CONFIRMA {E_FLECHA}\n\n\n"
            f"{E_ADN1} <b>PRIEMERO GANAS LUEGO PAGAS MANEJAMOS UN RESULTADO 100% SEGURO Y CONFIABLE</b> {E_ADN1}\n\n\n"
            f"{E_COHETE} <b>AVIATOR</b> {E_COHETE}\n\n"
            f"{E_REGALO} <b>SPACEMAN</b> {E_REGALO}\n\n"
            f"{E_DIAMANTE} <b>LUCKY JET</b> {E_DIAMANTE}\n\n\n"
            f"{E_GAFAS} {E_ESTRELLA} ESCRÍBANME AL PRIVADO SI DESEAN MÁS INFORMACIÓN {E_ESTRELLA} {E_GAFAS}\n\n\n\n"
            f"       {E_ESTRELLA} <a href='{LINK_ADMIN}'><b>ADMIN TELEGRAM</b></a> {E_ESTRELLA}\n\n"
            f"       {E_PULGAR} <a href='{LINK_ADMIN}'><b>CONTACTAR</b></a> {E_PULGAR}"
        )
        lote = [(canal, texto_promo) for canal in CANALES]
        print(f"\n[+] Enviando Info Promocional (Ciclo 8 min)...")
        await enviar_lote(lote)

async def tarea_publicidad_25_min():
    while True:
        texto_publi = (
            f"{E_ESTRELLA} <b>HOLA</b> {E_ESTRELLA} {E_GAFAS}\n"
            f"{E_PULGAR} <b>MUCHO GUSTO MI NOMBRE ES</b> {E_PULGAR}\n\n"
            f"  {E_FLECHA} <b>WILLIAM ROBERT</b> {E_FLECHA}\n\n"
            f"{E_BOLSA} TE COMENTO CÓMO TRABAJAMOS, {E_COHETE} Y SÍ TE INTERESA ME CONFIRMAS, "
            f"NOSOTROS TRABAJAMOS {E_DIAMANTE} 40% {E_DIAMANTE} {E_DIVISAS} 60% {E_DIVISAS} DE LAS GANANCIAS "
            f"QUE SE OBTENGAN YA QUE TRABAJAMOS CON APLICACIONES PREDICTOR QUE NOS INDICAN CADA SECUENCIA "
            f"Y CADA ALGORITMO QUE ESTEMOS LLEVANDO A CABO YA QUE MANEJAMOS RESULTADOS "
            f"{E_DIAMANTE} 100% {E_DIAMANTE} EFECTIVOS SI TE INTERESA TRABAJAR CON NOSOTROS ME CONFIRMA {E_FLECHA}\n\n\n"
            f"{E_ADN1} <b>PRIEMERO GANAS LUEGO PAGAS MANEJAMOS UN RESULTADO 100% SEGURO Y CONFIABLE</b> {E_ADN1}\n\n\n"
            f"{E_COHETE} <b>AVIATOR</b> {E_COHETE}\n\n"
            f"{E_REGALO} <b>SPACEMAN</b> {E_REGALO}\n\n"
            f"{E_DIAMANTE} <b>LUCKY JET</b> {E_DIAMANTE}\n\n\n"
            f"{E_GAFAS} {E_ESTRELLA} ESCRÍBANME AL PRIVADO SI DESEAN MÁS INFORMACIÓN {E_ESTRELLA} {E_GAFAS}\n\n\n\n"
            f"       {E_ESTRELLA} <b>ADMIN TELEGRAM</b> {E_ESTRELLA}\n\n"
            f"       {E_PULGAR} <a href='{LINK_ADMIN}'><b>CONTACTAR</b></a> {E_PULGAR}"
        )
        lote = [(canal, texto_publi) for canal in CANALES]
        print(f"\n[+] Enviando Publicidad de confirmación (Ciclo 25 min)...")
        await enviar_lote(lote)
        await asyncio.sleep(25 * 60)

async def tarea_senales_15_min():
    while True:
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

        await enviar_lote(mensajes_a_enviar)
        proximo_ciclo = inicio_ciclo + timedelta(minutes=15)
        segundos_espera = max(0, (proximo_ciclo - datetime.now()).total_seconds())
        print(f"⌛ Próxima ronda de señales en {int(segundos_espera)} segundos...")
        await asyncio.sleep(segundos_espera)

async def main():
    if os.path.exists("sesion_premium.session"):
        await client.connect()
    elif BOT_TOKEN:
        print("[+] Iniciando sesion con Token de Bot...")
        await client.start(bot_token=BOT_TOKEN)
    else:
        print("❌ No hay sesion_premium.session ni BOT_TOKEN configurado.")
        sys.exit(1)

    print("🚀 BOT PREMIUM ACTIVO Y CONECTADO A TELEGRAM")

    await asyncio.gather(
        tarea_publicidad_25_min(),
        tarea_promo_8_min(),
        tarea_senales_15_min()
    )

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n🛑 Proceso detenido.")
