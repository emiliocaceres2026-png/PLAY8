import time
import random
import asyncio
import os
import json
from datetime import datetime, timedelta
from telethon import TelegramClient

API_ID = 30370336
API_HASH = '3997f17c527e08b887ea3a0679c9c121'

# --- EMOJIS PREMIUM OFICIALES DEL PROYECTO ---
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

path = os.path.expanduser("~/Desktop/asistente_premium")
os.makedirs(path, exist_ok=True)
ARCHIVO_REGISTRO_CLIENTES = os.path.join(path, "clientes_atendidos.json")

# Rutas exactas de tus carpetas de audios
CARPETA_AUDIO_DUDA = r"C:\Users\carls\Desktop\AUDIO DUDA"

if os.path.exists(ARCHIVO_REGISTRO_CLIENTES):
    with open(ARCHIVO_REGISTRO_CLIENTES, "r", encoding="utf-8") as f:
        try:
            clientes_atendidos = json.load(f)
        except:
            clientes_atendidos = {}
else:
    clientes_atendidos = {}

def guardar_registro_clientes():
    with open(ARCHIVO_REGISTRO_CLIENTES, "w", encoding="utf-8") as f:
        json.dump(clientes_atendidos, f, indent=4, ensure_ascii=False)

client = TelegramClient(os.path.join(path, "sesion_nueva_prueba"), API_ID, API_HASH)

async def tarea_escanear_mensajes_privados():
    print("🤖 Escáner activo de chats privados con palabras clave de bienvenida iniciado...")

    palabras_inicio = ["hola", "hola me interesa", "hola quiero ganar", "estoy interesado", "deseo informacion", "informacion"]
    palabras_duda = ["duda", "miedo", "inconfiable", "no puedo", "no", "como así", "como asi", "desconfio", "inseguro", "inseguridad", "estafa", "falso", "datos", "contra", "contraseña", "por que", "por qué", "como se", "cómo se"]
    dominios_correo = ["@gmail", "@hotmail", "@outlook", "@yahoo", "@icloud"]

    while True:
        try:
            async for dialog in client.iter_dialogs(limit=25):
                if dialog.is_user:
                    remitente = dialog.entity
                    user_id_str = str(remitente.id)
                    username = f"@{remitente.username}" if remitente.username else ""
                    
                    estado_usuario = clientes_atendidos.get(user_id_str, {"fase": 0})
                    fase_actual = estado_usuario.get("fase", 0)
                    es_cuenta_de_prueba = (username.lower() in ["@aviatordoi", "@pedritorca"])

                    if not es_cuenta_de_prueba:
                        total_mensajes_chat = 0
                        async for _ in client.iter_messages(dialog.entity, limit=5):
                            total_mensajes_chat += 1

                        if total_mensajes_chat > 3:
                            continue

                    # ==========================================
                    # FASE 0: Detectar palabras de inicio ➡️ Enviar texto de bienvenida oficial con emojis 100% premium
                    # ==========================================
                    if fase_actual == 0:
                        async for message in client.iter_messages(dialog.entity, limit=1):
                            if message and message.text and not message.out:
                                texto_cliente = message.text.lower().strip()
                                coincide_inicio = any(p in texto_cliente for p in palabras_inicio)

                                if coincide_inicio:
                                    clientes_atendidos[user_id_str] = {
                                        "fase": 1,
                                        "fecha": time.strftime("%Y-%m-%d %H:%M:%S")
                                    }
                                    guardar_registro_clientes()

                                    print(f"📩 Palabra de inicio detectada de ({username or user_id_str}). Enviando mensaje de bienvenida oficial...")
                                    
                                    texto_bienvenida = (
                                        f"{E_ESTRELLA}<b>HOLA</b>{E_ESTRELLA}\n"
                                        f"{E_ESTRELLA}<b>MUCHO GUSTO MI NOMBRE ES</b>{E_ESTRELLA}\n\n"
                                        f"<b>WILLIAM ROBERT</b>\n\n"
                                        f"{E_REGALO}<b>TE COMENTO CÓMO TRABAJAMOS,</b> {E_COHETE}<b>Y SÍ TE INTERESA ME CONFIRMAS, NOSOTROS TRABAJAMOS</b> {E_DIAMANTE}{E_DIAMANTE}<b>40%</b> {E_DIAMANTE}{E_DIAMANTE}<b>60%</b> {E_DIAMANTE}<b>DE LAS GANANCIAS QUE SE OBTENGAN YA QUE TRABAJAMOS CON APLICACIONES PREDICTOR QUE NOS INDICAN CADA SECUENCIA Y CADA ALGORITMO QUE ESTEMOS LLEVANDO A CABO YA QUE MANEJAMOS RESULTADOS</b> {E_DIAMANTE}<b>100%</b>{E_DIAMANTE}<b>EFECTIVOS SI TE INTERESA TRABAJAR CON NOSOTROS ME CONFIRMA</b>{E_ESTRELLA}\n\n\n"
                                        f"{E_DIVISAS}<b>PRIMERO GANAS LUEGO PAGAS MANEJAMOS UN RESULTADO 100% SEGURO Y CONFIABLE</b>{E_DIVISAS}\n\n\n"
                                        f"{E_ESTRELLA}<b>AVIATOR</b> {E_ESTRELLA}\n\n\n"
                                        f"{E_ESTRELLA}<b>SPACEMAN</b> {E_ESTRELLA}\n\n\n"
                                        f"{E_ESTRELLA}<b>LUCKY JET</b> {E_ESTRELLA}"
                                    )
                                    await client.send_message(dialog.entity, texto_bienvenida, parse_mode='html')
                                    print(f"✨ Mensaje de bienvenida oficial enviado a: {username or user_id_str}")
                                break

                    # ==========================================
                    # FASE 1: Tras el texto de bienvenida ➡️ Enviar texto pidiendo audio de presentación
                    # ==========================================
                    elif fase_actual == 1:
                        async for message in client.iter_messages(dialog.entity, limit=1):
                            if message and message.text and not message.out:
                                clientes_atendidos[user_id_str]["fase"] = 2
                                guardar_registro_clientes()

                                texto_obligatorio = (
                                    f"{E_ESTRELLA} <b>HOLA QUE TAL</b> {E_ESTRELLA}\n\n"
                                    f"{E_ESTRELLA} <b>PRIMERO QUE TODO, PARA PROCEDER ATENDERTE</b> {E_ESTRELLA}\n\n"
                                    f"{E_COHETE} <b>PROCESO OBLIGATORIO</b> {E_COHETE}\n\n"
                                    f"{E_ESTRELLA} <b>ENVIAR UN AUDIO</b> {E_ESTRELLA}\n\n"
                                    f"{E_ESTRELLA} <b>PRESENTÁNDOTE</b> {E_ESTRELLA}\n"
                                    f"{E_ESTRELLA} <b>CON TU NOMBRE,</b> {E_ESTRELLA} {E_COHETE}\n"
                                    f"{E_ESTRELLA} <b>TU APELLIDO,</b> {E_ESTRELLA}\n\n"
                                    f"Y\n\n"
                                    f"{E_ESTRELLA} <b>EN QUE PLATAFORMA JUEGAS</b> {E_ESTRELLA}\n\n"
                                    f"{E_ESTRELLA} <b>PARA QUE UNO DE NUESTROS ASESORES PROCEDA ATENDERTE EN UN MOMENTO</b> {E_ESTRELLA}"
                                )
                                await client.send_message(dialog.entity, texto_obligatorio, parse_mode='html')
                                print(f"✨ Solicitud de audio de presentación enviada a: {username or user_id_str}")
                                break

                    # ==========================================
                    # FASE 2: Esperando audio de presentación ➡️ Instrucciones de recarga
                    # ==========================================
                    elif fase_actual == 2:
                        async for message in client.iter_messages(dialog.entity, limit=1):
                            if message and message.voice and not message.out:
                                clientes_atendidos[user_id_str]["fase"] = 3
                                guardar_registro_clientes()

                                texto_recarga = (
                                    f"{E_REGALO} <b>OK PERFECTO MUY BIEN…</b> {E_REGALO} {E_DIVISAS} <b>PROCEDE A RECARGAR TU CUENTA</b> {E_ADN1} <b>DE JUEGO, CON LA INVERSIÓN QUE</b> {E_DIAMANTE} <b>DESEA HACER CUANDO</b> {E_FLECHA} <b>RECARGUES TU CUENTA DE JUEGO</b> {E_ESTRELLA} <b>ME CONFIRMAS PARA NOTIFICARTE</b> {E_BOLSA} <b>LOS SIGUIENTES PASOS A SEGUIR.</b> {E_COHETE} <b>QUEDO ATENTO. MUCHAS GRACIAS</b> {E_REGALO}"
                                )
                                await client.send_message(dialog.entity, texto_recarga, parse_mode='html')
                                print(f"✨ Instrucciones de recarga enviadas a: {username or user_id_str}")
                                break

                    # ==========================================
                    # FASE 3: Tras confirmar recarga ➡️ Términos y Condiciones
                    # ==========================================
                    elif fase_actual == 3:
                        async for message in client.iter_messages(dialog.entity, limit=1):
                            if message and message.text and not message.out:
                                clientes_atendidos[user_id_str]["fase"] = 4
                                guardar_registro_clientes()

                                texto_terminos = (
                                    f"{E_BOLSA} <b>OK, COMÉNTAME SI ESTÁS</b> {E_REGALO} "
                                    f"<b>TOTALMENTE DE ACUERDO CON LOS</b> {E_FLECHA} <b>TÉRMINOS Y CONDICIONES, ES</b> {E_ADN1} "
                                    f"<b>DECIR 40% DE LAS GANANCIAS</b> {E_ESTRELLA} <b>PARA TI 60% PARA NOSOTROS SI</b> {E_FLECHA} "
                                    f"<b>ESTÁS TOTALMENTE DE ACUERDO</b> {E_BOLSA} <b>POR FAVOR ME CONFIRMAS. GRACIAS</b> {E_REGALO}"
                                )
                                await client.send_message(dialog.entity, texto_terminos, parse_mode='html')
                                print(f"✨ Mensaje de términos y condiciones enviado a: {username or user_id_str}")
                                break

                    # ==========================================
                    # FASE 4: Tras aceptar términos ➡️ Pedir Usuario y Contraseña
                    # ==========================================
                    elif fase_actual == 4:
                        async for message in client.iter_messages(dialog.entity, limit=1):
                            if message and message.text and not message.out:
                                clientes_atendidos[user_id_str]["fase"] = 5
                                guardar_registro_clientes()

                                texto_conexion = (
                                    f"{E_BOLSA} <b>OK PERFECTO MUY BIEN, POR</b> {E_BOLSA} "
                                    f"<b>FAVOR ENVÍAME USUARIO Y</b> {E_BOLSA} "
                                    f"<b>CONTRASEÑA PARA PROCEDER A</b> {E_COHETE}{E_DIAMANTE} <b>CONECTAR TU CUENTA</b> {E_BOLSA} "
                                    f"<b>DIRECTAMENTE AL SERVIDOR Y</b> {E_ADN1} "
                                    f"<b>ASIMISMO PODER COMENZAR A</b> {E_BOLSA} "
                                    f"<b>INCREMENTAR TUS GANANCIAS POR FAVOR QUEDO ATENTO</b> {E_ADN2}"
                                )
                                await client.send_message(dialog.entity, texto_conexion, parse_mode='html')
                                print(f"✨ Solicitud de usuario y contraseña enviada a: {username or user_id_str}")
                                break

                    # ==========================================
                    # FASE 5: Bifurcación (Datos vs Audio de Dudas de AUDIO DUDA)
                    # ==========================================
                    elif fase_actual == 5:
                        async for message in client.iter_messages(dialog.entity, limit=1):
                            if message and message.text and not message.out:
                                texto_cliente = message.text.lower()

                                tiene_duda = any(palabra in texto_cliente for palabra in palabras_duda)

                                if tiene_duda:
                                    print(f"⚠️ Duda o negativa detectada en ({username or user_id_str}). Enviando nota de voz desde AUDIO DUDA...")
                                    audio_duda_enviado = False
                                    if os.path.exists(CARPETA_AUDIO_DUDA):
                                        for archivo in os.listdir(CARPETA_AUDIO_DUDA):
                                            if archivo.lower().endswith(('.ogg', '.mp3', '.m4a', '.wav', '.oga')):
                                                ruta_completa = os.path.join(CARPETA_AUDIO_DUDA, archivo)
                                                await client.send_file(dialog.entity, ruta_completa, voice_note=True)
                                                print(f"🎤 Nota de voz de duda ({archivo}) enviada con éxito.")
                                                audio_duda_enviado = True
                                                break
                                    if not audio_duda_enviado:
                                        print(f"⚠️ [Aviso] No se encontró audio en '{CARPETA_AUDIO_DUDA}'.")
                                    break

                                es_correo = any(dominio in texto_cliente for dominio in dominios_correo)
                                parece_credenciales = len(texto_cliente.split()) >= 2 or es_correo or len(texto_cliente) > 6

                                if parece_credenciales:
                                    clientes_atendidos[user_id_str]["fase"] = 6
                                    guardar_registro_clientes()

                                    texto_saldo = (
                                        f"{E_ADN1} <b>PERFECTO, EN EL MOMENTO QUE</b> {E_BOLSA} "
                                        f"<b>NOSOTROS NOS ENCONTRAMOS INCREMENTADOS DE SALDO DE UNA</b> {E_ADN1} "
                                        f"<b>MANERA SEGURA Y CONFIABLE NECESITO QUE MANTENGAS TU CUENTA DESCONECTADA Y NO INICIA</b> {E_ESTRELLA} "
                                        f"<b>SESIÓN PARA NO PRESENTAR INCONVENIENTES CON</b> {E_ADN1} "
                                        f"<b>EL SERVIDOR A</b> {E_COHETE} "
                                        f"<b>MEDIDA DE ESTAR INCREMENTANDO TU SALDO TE VAMOS A ESTAR ENVIANDO FOTO Y VIDEO DE LAS</b> {E_REGALO} "
                                        f"<b>GANANCIAS</b> {E_BOLSA} <b>QUE ESTEMOS INCREMENTANDO. GRACIAS ASÍ QUE POR FAVOR CUANDO DESCONECTES TU CUENTA ME CONFIRMAS PARA PODER COMENZAR.</b> {E_BOLSA}"
                                    )
                                    await client.send_message(dialog.entity, texto_saldo, parse_mode='html')
                                    print(f"✨ Instrucciones de cuenta desconectada enviadas a: {username or user_id_str}")
                                    break
        except Exception as e:
            print(f"⚠️ Error en el escáner privado: {e}")
        
        await asyncio.sleep(4)

async def main():
    await client.start()
    print("🚀 ASISTENTE PRIVADO ACTIVO - BIENVENIDA PREMIUM SIN EMOJIS NORMALES")
    await asyncio.gather(
        tarea_escanear_mensajes_privados()
    )

if __name__ == '__main__':
    while True:
        try:
            with client:
                client.loop.run_until_complete(main())
        except Exception as e:
            print(f"⚠️ [AVISO DE RECONEXIÓN] Ocurrió un error general: {e}. Reiniciando en 5 segundos...")
            time.sleep(5)
