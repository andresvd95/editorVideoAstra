# ⛔ REGLA OBLIGATORIA: perfil de cliente antes de editar

Antes del primer encargo audiovisual de un cliente, comprobar si existe
`ESTILO_CLIENTE_LOCAL.md` con `Estado: CONFIRMADO`.

- Si no existe o está incompleto, realizar primero la entrevista de marca descrita en
  `ESTILO_EDICION_VERTICAL_REPLICABLE.md`: colores, logos, tipo de edición, tipografía,
  lenguaje gráfico, subtítulos, audio, formato y restricciones.
- Esperar las respuestas, completar el archivo local desde
  `ESTILO_CLIENTE_LOCAL.example.md` y resumirlo al cliente antes de editar.
- En trabajos posteriores, cargar ese perfil automáticamente y preguntar solo por
  cambios o datos faltantes.
- El perfil local sobrescribe el estilo visual general, pero no una instrucción explícita
  más reciente, requisitos de seguridad, legibilidad, licencias o conservación del
  original.
- No preguntar por la marca al realizar únicamente mantenimiento documental o técnico
  del repositorio.

# ⛔ REGLA OBLIGATORIA: preguntar ANTES de empezar un encargo audiovisual

Antes de empezar CUALQUIER encargo audiovisual —editar, analizar, cortar, renderizar, instalar
o incluso abrir los materiales— preguntar SIEMPRE estas 6 cosas y esperar las respuestas:

1. **MCP de DaVinci Resolve:** ¿Ya está OK el MCP de DaVinci Resolve (instalado, registrado y conectado)?
2. **Formato:** ¿Qué formato necesitas (proporción, resolución, fps y plataforma de destino)?
3. **Encargo:** ¿Qué quieres que se haga (escena, textos, cortes, efectos y duración)?
4. **Materiales:** ¿Dónde está el video o los materiales (ruta exacta)?
5. **DaVinci Resolve:** ¿DaVinci Resolve ya está abierto (con un proyecto disponible)?
6. **API de Gemini:** ¿Ya está OK la API de Gemini para proceder?

- **No empezar** hasta tener las 6 respuestas. No asumir ninguna respuesta por defecto.
- Si alguna respuesta es «no», resolver primero ese punto y volver a confirmar.
- Las respuestas valen para el encargo actual: dentro del mismo encargo no se repiten en
  cada paso; en un encargo o sesión nueva se vuelven a preguntar.
- Confirmación del usuario y verificación técnica son estados distintos: comprobar la
  conexión real del MCP (`scripts/check-resolve-mcp.py`) y la respuesta de Gemini.
  Detalle en `MCP_DAVINCI_GEMINI.md`.

Para instalar el MCP desde cero, una respuesta «todavía no está instalado, instálalo»
autoriza la instalación; verificar la conexión antes de editar en Resolve.

Leer primero `ESTILO_CLIENTE_LOCAL.md` cuando exista y después
`ESTILO_EDICION_VERTICAL_REPLICABLE.md` y `MCP_DAVINCI_GEMINI.md`.
Usar Gemini para comprender el video y marcar tiempos verificables. Un minuto
aproximado del usuario es una pista, nunca un límite de corte ya confirmado.
Realizar el montaje en DaVinci Resolve mediante su MCP. Conservar el original y
crear una timeline propia para el montaje. No presentar un plan como video terminado.

Nunca guardar claves API, tokens, videos privados o entornos Python en Git.
Publicar documentación/configuración y el submódulo del MCP cuando se solicite.

