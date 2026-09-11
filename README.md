# EditorVideoAstra

## ⛔ Protocolo obligatorio antes de editar

En el primer encargo del cliente, comprobar o crear primero `ESTILO_CLIENTE_LOCAL.md`
mediante la entrevista de marca explicada más abajo. Después, en cada encargo audiovisual,
preguntar estas seis cosas y esperar las respuestas:

1. **MCP de DaVinci Resolve:** ¿Ya está OK el MCP de DaVinci Resolve?
2. **Formato:** ¿Qué formato necesitas?
3. **Encargo:** ¿Qué quieres que se haga?
4. **Materiales:** ¿Dónde está el video o los materiales?
5. **DaVinci Resolve:** ¿DaVinci Resolve ya está abierto?
6. **API de Gemini:** ¿Ya está OK la API de Gemini para proceder?

No empezar sin las 6 respuestas ni asumirlas por defecto. Detalle y verificación
técnica en [MCP_DAVINCI_GEMINI.md](MCP_DAVINCI_GEMINI.md).

El repositorio incluye el MCP oficial como submódulo en `mcp/davinci-resolve`,
su registro para Codex y el protocolo de análisis con Gemini.
Instalación y flujo: [MCP_DAVINCI_GEMINI.md](MCP_DAVINCI_GEMINI.md).
Clonar con `git clone --recurse-submodules` para descargar también el MCP.

Sistema general para producir videos verticales con una edición moderna, clara,
dinámica y adaptable a la identidad de cada cliente.

Este repositorio documenta las reglas visuales, narrativas y técnicas que deben seguirse al editar piezas corporativas, promocionales e informativas. El objetivo es que diferentes editores —humanos o asistidos por IA— puedan obtener resultados consistentes.

## Primera vez con un cliente

Antes de editar, el asistente debe buscar `ESTILO_CLIENTE_LOCAL.md` en el proyecto de
trabajo.

1. Si no existe, pregunta al cliente por **colores, logos, tipo de edición, tipografía,
   lenguaje gráfico, subtítulos, audio, formatos y restricciones**.
2. Espera las respuestas y copia
   [`ESTILO_CLIENTE_LOCAL.example.md`](./ESTILO_CLIENTE_LOCAL.example.md) como
   `ESTILO_CLIENTE_LOCAL.md`.
3. Completa el perfil, lo resume al cliente y marca `Estado: CONFIRMADO`.
4. En los siguientes encargos carga el perfil automáticamente y no repite la entrevista,
   salvo que falte información o la marca haya cambiado.

El perfil real queda excluido de Git. Sus reglas de marca sobrescriben el estilo general,
pero no una instrucción explícita más reciente del cliente ni requisitos de seguridad,
legibilidad, licencias o conservación del material.

### Orden de prioridad

1. Instrucción del cliente para el encargo actual.
2. `ESTILO_CLIENTE_LOCAL.md` confirmado.
3. Brief o guion del proyecto.
4. Sistema general de este repositorio.

## Documento principal

La especificación completa está en:

➡️ [ESTILO_EDICION_VERTICAL_REPLICABLE.md](./ESTILO_EDICION_VERTICAL_REPLICABLE.md)

Incluye:

- Formato vertical, resolución y zonas seguras.
- Paleta de color y jerarquía visual.
- Tipografías, subtítulos y títulos con relieve 2.5D.
- Diseño y animación de la tarjeta inicial.
- Animación de iconos y recursos gráficos.
- Zoom in, zoom out, punch-in y reencuadres.
- Transiciones y efectos básicos de video.
- Colorización y diseño sonoro.
- Organización recomendada de pistas en DaVinci Resolve.
- Parámetros reutilizables y lista de control final.

## Principios esenciales

1. **La narración manda:** cada recurso debe reforzar una frase, gesto o acción.
2. **El rostro es prioritario:** ningún título, icono o gráfico debe cubrirlo.
3. **Una idea por escena:** evitar competir por la atención del espectador.
4. **Dinamismo con intención:** usar movimiento cuando mejore el ritmo o la comprensión.
5. **Consistencia de marca:** respetar la paleta, tipografía y jerarquía definidas.
6. **Edición segura:** conservar una copia antes de modificar un montaje aprobado.

## Referencia rápida

| Elemento | Regla base |
|---|---|
| Formato | 9:16, 1080 × 1920 px, 30 fps |
| Tarjetas completas | Solo una, al inicio |
| Títulos | Cortos, en mayúsculas y fuera del rostro |
| Fuente principal | La definida en el perfil local |
| Fuente secundaria | La definida en el perfil local |
| Colores de marca | Los definidos en el perfil local |
| Color de énfasis | El definido en el perfil local |
| Zoom progresivo | 100 % a 103–106 % |
| Punch-in | 100 % a 104–108 % |
| Transición predeterminada | Disolución de 6–10 fotogramas |
| Música | Baja, aproximadamente −30 a −34 LUFS |
| Voz | Prioritaria, objetivo aproximado de −16 LUFS |

## Cómo utilizar el sistema

### 1. Preparar el material

- Reunir videos, voz, música, efectos, imágenes y logos.
- Identificar la duración y calidad de cada archivo.
- Transcribir la voz y marcar frases, pausas, fechas y palabras clave.
- Revisar los gestos y el espacio disponible alrededor de la persona.

### 2. Construir el montaje

- Editar primero la voz y la historia.
- Seleccionar las tomas por significado, expresión y gesto.
- Mantener pausas naturales y retirar silencios accidentales.
- Guardar una copia antes de realizar cambios estructurales.

### 3. Aplicar el diseño

- Crear una sola tarjeta inicial.
- Mostrar palabras clave como títulos flotantes.
- Ubicar iconos en relación con los gestos de la persona.
- Incorporar subtítulos durante toda la voz.
- Respetar las zonas seguras y evitar cubrir el rostro.

### 4. Añadir dinamismo

- Usar zoom in para enfatizar beneficios o frases importantes.
- Usar zoom out para revelar contexto o liberar espacio.
- Aplicar punch-in únicamente en palabras clave.
- Animar títulos, iconos y gráficos con entradas y salidas suaves.
- Reservar las transiciones llamativas para cambios reales de bloque.

### 5. Finalizar

- Igualar color y proteger los tonos de piel.
- Mantener la música detrás de la voz.
- Sincronizar efectos con apariciones y cortes.
- Revisar el video completo después de exportarlo.
- Confirmar que el archivo final contiene los últimos cambios manuales.

## Estructura recomendada en DaVinci Resolve

```text
V4  Máscaras o recursos extraordinarios
V3  Títulos, subtítulos, iconos y gráficos
V2  Transiciones y recursos de apoyo
V1  Montaje principal

A5  Efectos adicionales
A4  Efectos de aparición
A3  Música
A2  Voz / canal adicional
A1  Voz principal
```

## Antes de entregar

- [ ] El formato es vertical 9:16.
- [ ] Ningún elemento cubre el rostro.
- [ ] Los subtítulos son legibles y están sincronizados.
- [ ] Los zooms no cortan cabeza, manos u objetos relevantes.
- [ ] Los iconos aparecen sincronizados con la voz o el gesto.
- [ ] La música no compite con la voz.
- [ ] Los efectos coinciden con los cortes y apariciones.
- [ ] El color es consistente entre escenas.
- [ ] Se conservaron los cambios manuales aprobados.
- [ ] Se revisó la exportación completa.

## Alcance actual

El repositorio contiene la documentación, la plantilla pública del perfil de cliente, el
MCP de DaVinci Resolve como submódulo y scripts de instalación/verificación. No incluye
perfiles reales de clientes, videos, audios, credenciales, material privado ni archivos
temporales de DaVinci Resolve.

## Licencia y uso

Antes de reutilizar públicamente activos, logos, fuentes, música o efectos, verifica que cuentas con los permisos y licencias correspondientes. Este repositorio define el estilo de edición; no concede derechos sobre recursos de terceros.

