# DaVinci Resolve MCP + Gemini

## ⛔ REGLA OBLIGATORIA: preguntar ANTES de empezar cualquier cosa

Antes de empezar CUALQUIER trabajo —editar, analizar, cortar, renderizar, instalar
o incluso abrir los materiales— preguntar SIEMPRE estas 6 cosas y esperar las respuestas:

1. **MCP de DaVinci Resolve:** ¿Ya está OK el MCP de DaVinci Resolve (instalado, registrado y conectado)?
2. **Formato:** ¿Qué formato necesitas (proporción, resolución, fps y plataforma de destino)?
3. **Encargo:** ¿Qué quieres que se haga (escena, textos, cortes, efectos y duración)?
4. **Materiales:** ¿Dónde está el video o los materiales (ruta exacta)?
5. **DaVinci Resolve:** ¿DaVinci Resolve ya está abierto (con un proyecto disponible)?
6. **API de Gemini:** ¿Ya está OK la API de Gemini para proceder?

Mensaje para copiar al inicio de cada encargo:

> Antes de empezar necesito confirmar:
> 1. ¿Ya está OK el MCP de DaVinci Resolve?
> 2. ¿Qué formato necesitas?
> 3. ¿Qué quieres que se haga?
> 4. ¿Dónde está el video o los materiales?
> 5. ¿DaVinci Resolve ya está abierto?
> 6. ¿Ya está OK la API de Gemini para proceder?

- **No empezar** hasta tener las 6 respuestas. No asumir ninguna respuesta por defecto.
- Si alguna respuesta es «no», resolver primero ese punto (instalar el MCP, abrir Resolve,
  configurar `GEMINI_API_KEY`, conseguir la ruta del material) y volver a confirmar.
- Las respuestas valen para el encargo actual: dentro del mismo encargo no se repiten en
  cada paso; en un encargo o sesión nueva se vuelven a preguntar.
- La confirmación del usuario no sustituye la verificación técnica. No confundir
  «instalado», «registrado en Codex/Claude» y «conectado a Resolve»:

| Pregunta | Verificación técnica antes de usarlo |
|---|---|
| MCP de DaVinci Resolve | `.venv-resolve/Scripts/python.exe scripts/check-resolve-mcp.py` devuelve código 0 |
| DaVinci Resolve abierto | La misma comprobación; código 2 = el MCP arranca pero Resolve no responde a su API |
| API de Gemini | `GEMINI_API_KEY` definida localmente y una llamada de prueba responde sin error |
| Materiales | La ruta indicada existe y el archivo se puede leer |

## MCP incluido

Fuente: [samuelgursky/davinci-resolve-mcp](https://github.com/samuelgursky/davinci-resolve-mcp).
Se incluye como submódulo en `mcp/davinci-resolve`: Git guarda el commit exacto
del servidor original, cuya licencia MIT y documentación se conservan.

```powershell
git clone --recurse-submodules https://github.com/andresvd95/editorVideoAstra.git
cd editorVideoAstra
# Si ya clonaste sin submódulos:
git submodule update --init --recursive
uv venv --python 3.10 .venv-resolve
uv pip install --python .venv-resolve/Scripts/python.exe -r mcp/davinci-resolve/requirements.txt
powershell -NoProfile -ExecutionPolicy Bypass -File scripts/register-resolve-mcp.ps1
```

El registro usa el servidor compuesto oficial y rutas absolutas calculadas localmente.
No sustituye la configuración de otros MCP de Codex. Tras registrarlo puede ser
necesario abrir una nueva sesión de Codex para cargar sus herramientas.

En Resolve Studio, configurar **Preferences > General > External scripting using > Local**.
Para otras ediciones/versiones, consultar `mcp/davinci-resolve/docs/install.md`:
no asumir que abrir Resolve garantiza acceso a su API.

```powershell
.venv-resolve/Scripts/python.exe scripts/check-resolve-mcp.py
```

Esta comprobación abre una sesión MCP, enumera herramientas y consulta el estado
de Resolve sin editar el proyecto. Devuelve código 2 si el servidor arranca pero
Resolve no está disponible. Para comprobar solamente la instalación del servidor:

```powershell
.venv-resolve/Scripts/python.exe scripts/check-resolve-mcp.py --server-only
```

### Estado de la instalación inicial

MCP instalado y registrado en Codex; arranque MCP verificado con 36 herramientas.
La consulta inicial a Resolve devolvió `SCRIPTING_UNAVAILABLE`: la aplicación estaba
abierta, pero no contestaba a su API. Antes de editar, habilitar el acceso correspondiente
a la edición instalada y repetir la comprobación completa. La credencial de Gemini fue
validada; el análisis y la edición del video quedan para una etapa posterior.

## Gemini: comprensión antes de cortar

- La clave se entrega mediante la variable de entorno `GEMINI_API_KEY` o un archivo
  local ignorado por Git. Nunca incluirla en scripts, Markdown, commits o logs.
- Validar la credencial antes de subir el material al servicio autorizado por el usuario.
- Usar la API Files para videos grandes, esperar el estado `ACTIVE` y analizar el
  archivo real; no inventar escenas a partir del nombre o de la descripción.
- Pedir tiempos absolutos de inicio/final, evidencia visual, participantes,
  momentos de impacto y confianza. Distinguir observaciones de interpretaciones.
- Revisar los límites y mantener separados combates distintos. Si hay ambigüedad,
  verificar el tramo o pedir una aclaración puntual antes de decidir el montaje.
- Guardar el análisis localmente y trasladar sus tiempos a marcadores de Resolve.

Referencia: [comprensión de video con Gemini](https://ai.google.dev/gemini-api/docs/video-understanding).

## Montaje y entrega

Crear una timeline del encargo; conservar el video original. Para historias:
1080 × 1920, 9:16, 30 fps, MP4 H.264 con AAC estéreo. Seguir la acción al reencuadrar.
Usar textos llamativos con contorno y profundidad, naranja/dorado en palabras clave,
entradas breves y zoom in/out motivado. Reservar efectos de impacto para acciones
identificadas; no ocultar al jugador, al aliado ni al adversario. Priorizar el audio
del juego y comprobar el resultado exportado, incluido el final de la pelea.

## Encargo WoW confirmado

- Material: `MATERIAL/VIDEO WOW 1/World of Warcraft 2026-03-31 23-52-10.mp4`
  (en la carpeta superior del repositorio).
- Formato: historias 9:16, 1080 × 1920.
- Texto principal: «Cuando están pegándole a tu amigo y llegas a rescatarlo».
- Desde aproximadamente **1:45**, identificar con Gemini al jugador atacando a quien
  estaba pegándole a su amigo y determinar el final real de ese combate.
- Cerca de **2:50** comienza otra pelea: identificarla por separado; no mezclarla
  automáticamente con el primer rescate ni afirmar sus límites sin ver el video.
- Estilo: textos llamativos, zoom in, zoom out y edición dinámica donde ayude a la acción.
- El usuario confirmó Resolve abierto y autorizó Gemini. La comprobación técnica
  y el análisis deben completarse antes de dar por identificada la escena.
