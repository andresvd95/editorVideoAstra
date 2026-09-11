# SISTEMA REPLICABLE DE EDICIÓN VERTICAL — VELONET

## 0. ⛔ REGLA OBLIGATORIA: preguntar ANTES de empezar cualquier cosa

Antes de empezar CUALQUIER trabajo, preguntar SIEMPRE estas 6 cosas y esperar las respuestas:

1. **MCP de DaVinci Resolve:** ¿Ya está OK el MCP de DaVinci Resolve (instalado, registrado y conectado)?
2. **Formato:** ¿Qué formato necesitas (proporción, resolución, fps y plataforma de destino)?
3. **Encargo:** ¿Qué quieres que se haga (escena, textos, cortes, efectos y duración)?
4. **Materiales:** ¿Dónde está el video o los materiales (ruta exacta)?
5. **DaVinci Resolve:** ¿DaVinci Resolve ya está abierto (con un proyecto disponible)?
6. **API de Gemini:** ¿Ya está OK la API de Gemini para proceder?

No empezar sin las 6 respuestas ni asumirlas por defecto. Dentro del mismo encargo no se
repiten en cada paso; en un encargo nuevo se vuelven a preguntar. Verificar la conexión
real del MCP y de Gemini antes de usarlos.
Si se solicita instalar el MCP, completar primero esa instalación y comprobarla antes
de editar. El procedimiento reproducible está en [MCP_DAVINCI_GEMINI.md](MCP_DAVINCI_GEMINI.md).

Gemini debe comprender el video real y proponer tiempos verificables antes de recortar.
DaVinci Resolve y su MCP realizan el montaje. En clips de videojuegos, adaptar esta guía
a la acción: textos llamativos, zoom in/out y efectos de impacto puntuales, sin tapar
personajes ni perder el desenlace. Mantener separados combates diferentes.

Las claves API se configuran localmente y nunca se suben a GitHub.

## 1. Propósito

Este documento define un sistema estable para editar videos verticales corporativos de Velonet con un acabado moderno, dinámico y profesional.

Debe aplicarse a campañas, promociones, anuncios informativos, tutoriales breves, novedades de servicio y llamados a la acción.

El resultado debe sentirse:

- Claro y fácil de seguir.
- Dinámico, pero no sobrecargado.
- Coherente con la identidad de Velonet.
- Cercano, tecnológico y confiable.
- Diseñado alrededor de la narración y de la persona en cámara.

> **Regla central:** cada movimiento, texto, icono, transición o efecto debe reforzar una idea concreta. No se agregan efectos únicamente para llenar la pantalla.

---

## 2. Formato maestro

| Propiedad | Valor recomendado |
|---|---:|
| Relación de aspecto | 9:16 vertical |
| Resolución de edición | 1080 × 1920 px |
| Resolución mínima | 720 × 1280 px |
| Fotogramas por segundo | 30 fps |
| Espacio de color | Rec.709 Gamma 2.4 |
| Audio | 48 kHz estéreo |
| Duración ideal | 15–45 segundos |
| Exportación | H.264, MP4, audio AAC |

### Zonas seguras

- Dejar al menos **7 % del ancho** libre en cada lateral.
- Evitar títulos dentro del **10 % superior**, donde algunas plataformas muestran elementos de interfaz.
- Mantener subtítulos por encima del **15 % inferior**.
- No colocar texto, iconos o gráficos sobre ojos, boca o gestos importantes.
- Antes de diseñar, identificar el espacio negativo real de cada plano.

---

## 3. Jerarquía visual

La edición debe seguir esta prioridad:

1. Rostro y expresión de la persona.
2. Acción o gesto que explica el mensaje.
3. Palabra clave o beneficio principal.
4. Icono o recurso gráfico que completa la idea.
5. Subtítulos.
6. Elementos decorativos.

Si dos elementos compiten, se elimina o reduce el de menor prioridad.

### Densidad máxima

- Una idea principal visible por escena.
- Un título destacado a la vez.
- Un icono principal a la vez, salvo que la narración compare explícitamente dos elementos.
- Máximo dos líneas de subtítulos.
- Evitar repetir en pantalla la oración completa si ya está subtitulada: el título solo debe mostrar la palabra o concepto clave.

---

## 4. Paleta de color

### Colores principales

| Uso | Color |
|---|---|
| Morado corporativo | `#5D2D91` |
| Morado oscuro | `#211331` |
| Morado de profundidad | `#482247` |
| Naranja de énfasis | `#FFAA3D` |
| Dorado luminoso | `#FFF0C5` |
| Blanco principal | `#FFFFFF` |
| Blanco secundario | `#EEE8F6` |
| Negro de contorno | `#140C20` |

### Reglas de uso

- Morado: base de marca, sombras y paneles.
- Naranja/dorado: beneficios, fechas, verbos de acción y palabras clave.
- Blanco: información principal y subtítulos.
- No introducir colores ajenos a la paleta salvo que pertenezcan a un activo oficial.
- Los degradados deben ser suaves y utilizar tonos de la misma familia.

---

## 5. Tipografía

### Fuentes

- **Títulos principales:** Gobold Regular.
- **Alternativa de títulos:** Montserrat ExtraBold o Black.
- **Subtítulos y textos auxiliares:** Montserrat SemiBold.
- **Texto secundario:** Montserrat Medium.

### Tratamiento de títulos principales

- Usar mayúsculas.
- Aplicar una cara con degradado blanco–dorado o blanco–naranja.
- Añadir contorno fino claro y contorno exterior oscuro.
- Crear relieve 2.5D mediante entre **5 y 9 capas desplazadas** hacia abajo y a la derecha.
- Añadir una sombra suave y corta; evitar sombras negras grandes.
- Mantener alta legibilidad incluso en pantallas pequeñas.

### Tratamiento de subtítulos

- Montserrat SemiBold.
- Blanco con contorno oscuro de 2–4 px, según resolución.
- Sombra discreta únicamente si el fondo lo requiere.
- Una o dos líneas, centradas.
- Mostrar bloques cortos siguiendo la cadencia de la voz.
- Resaltar en naranja o dorado solamente una palabra importante cuando sea útil.
- No utilizar una caja morada permanente detrás de los subtítulos.

---

## 6. Tarjeta inicial

Solo se permite una tarjeta completa al comienzo del video.

### Diseño

- Panel de vidrio oscuro y semitransparente.
- Esquinas redondeadas amplias.
- Borde fino blanco o dorado con baja opacidad.
- Una barra o detalle naranja pequeño, no dominante.
- Kicker breve, título principal y una línea secundaria.
- El premio, beneficio o pregunta debe ser el elemento de mayor tamaño.

### Animación

- Duración de entrada: **9–12 fotogramas**.
- Escala inicial: **88–92 %**.
- Escala final: **100 %**.
- Desplazamiento vertical inicial: **20–40 px**.
- Opacidad: 0–100 %.
- Curva: Ease Out suave, sin rebote agresivo.
- Salida: 6–8 fotogramas con opacidad y desplazamiento corto.
- Se puede agregar un brillo diagonal muy sutil, una sola vez.

### Prohibición

No repetir tarjetas pesadas durante el resto del video. Después del inicio se utilizan títulos flotantes, iconos y subtítulos.

---

## 7. Títulos y palabras clave

Los textos principales deben aparecer en el espacio negativo, preferiblemente arriba de la persona o en el lado hacia el que está señalando.

### Comportamiento

- Duración habitual: **1.2–2.8 segundos**.
- Entrada: escala 90–100 %, desplazamiento de 15–30 px y opacidad.
- Salida: opacidad y desplazamiento de 10–20 px.
- Aplicar Ease Out al entrar y Ease In al salir.
- Se permite una inclinación máxima de 1–2° si ayuda a la energía del plano.
- Evitar movimientos continuos de gran amplitud.

### Animación tipográfica principal

Para palabras especialmente importantes se puede utilizar:

1. Aparición por palabra o por bloque semántico.
2. Escala rápida de 92 % a 103 % y asentamiento a 100 %.
3. Revelado mediante máscara horizontal o vertical.
4. Extrusión 2.5D animada durante la entrada.
5. Barrido de luz breve sobre la cara de la tipografía.

No usar más de dos técnicas simultáneas.

---

## 8. Iconos y aplicaciones gráficas

Los iconos deben responder a lo que la persona dice o señala. No deben flotar sin relación con la acción.

### Preparación

- Recortar márgenes transparentes innecesarios.
- Conservar la proporción original.
- Aplicar sombra difusa pequeña para separarlos del fondo.
- No alterar logotipos ni activos corporativos oficiales.
- Mantener una escala coherente entre iconos equivalentes.

### Animación de entrada

- Duración: **8–12 fotogramas**.
- Escala: 75–90 % a 100 %.
- Opacidad: 0–100 %.
- Desplazamiento: 15–35 px desde la dirección del gesto.
- Rotación opcional: máximo 4°.
- Ease Out o Back muy leve; evitar rebotes caricaturescos.

### Movimiento en pantalla

- Flotación máxima: 2–5 px.
- Ciclo: 1.2–2 segundos.
- Puede añadirse un brillo o pulso único al aparecer.
- Si el icono representa una acción, se permite una microanimación interna breve.

### Salida

- Duración: 5–8 fotogramas.
- Opacidad a cero y escala a 96–98 %.
- Retirar el icono antes de que comience una nueva idea.

### Sincronización sonora

- Usar un efecto mágico, campana o destello suave al aparecer un elemento importante.
- El pico del sonido debe coincidir con el momento en que el icono alcanza aproximadamente el 100 % de escala.
- El efecto debe permanecer por debajo de la voz y no repetirse de forma mecánica.

---

## 9. Movimiento de cámara y efectos dinámicos

En escenas donde el encuadre y la resolución lo permitan, aplicar movimiento digital para evitar planos estáticos.

### Zoom in progresivo

Usar cuando:

- La frase aumenta en importancia.
- Se presenta un beneficio.
- La persona mira directamente a cámara.
- Se necesita dirigir la atención al rostro o a un objeto.

Valores recomendados:

- Inicio: 100 %.
- Final: 103–106 %.
- Duración: 0.8–2 segundos.
- Curva: Ease In/Out.
- Reencuadrar para que los ojos no cambien bruscamente de posición.

### Zoom out progresivo

Usar cuando:

- Se revela el contexto o una interfaz.
- Se cierra una explicación.
- Entra un título o icono que necesita más espacio.
- Se prepara una transición.

Valores recomendados:

- Inicio: 104–107 %.
- Final: 100 %.
- Duración: 0.8–2 segundos.
- Curva: Ease In/Out.

### Punch-in de énfasis

- Escala: 100 % a 104–108 %.
- Entrada: 5–8 fotogramas.
- Mantener durante la palabra clave.
- Salida opcional: 6–10 fotogramas.
- Usar como máximo una vez por frase o idea.

### Movimiento lateral y reencuadre

- Se permite un desplazamiento horizontal de 1–3 % para seguir un gesto o liberar espacio para gráficos.
- El movimiento debe ser lento y continuo.
- No cortar manos, cabeza o elementos relevantes durante el recorrido.

### Efectos básicos permitidos

- Zoom in y zoom out.
- Punch-in suave.
- Reencuadre lateral.
- Desenfoque direccional breve durante una transición motivada.
- Destello o glow sutil sobre un gráfico.
- Ligero motion blur en elementos animados.
- Congelado muy corto solo si enfatiza un dato o permite una composición gráfica.
- Velocidad variable suave únicamente cuando la acción original lo soporte.

### Límites

- No superar 108 % de escala salvo material de alta resolución y justificación clara.
- No encadenar zooms en cada oración.
- No aplicar shake, glitch, RGB split o distorsiones fuertes en piezas corporativas informativas.
- No degradar nitidez ni revelar bordes por el reencuadre.
- Si el rostro ya ocupa gran parte del plano, priorizar movimiento de texto antes que zoom.

---

## 10. Transiciones

### Transición predeterminada

- Disolución suave de **6–10 fotogramas**.
- Debe mantener intacta la narración.
- No debe generar cuadros negros ni saltos de exposición.

### Transición con movimiento

Se permite cuando dos planos comparten dirección o energía:

- Whip pan corto.
- Desenfoque direccional.
- Zoom through discreto.
- Match cut por gesto, objeto, forma o color.

### Sonido de transición

- Añadir woosh solamente en cambios claros de bloque o localización.
- Hacer coincidir el golpe principal con el punto de corte.
- Ajustar el inicio del archivo para que la cola del efecto continúe después del cambio.
- Evitar woosh en cada corte.

---

## 11. Ritmo de edición

- Cortar por intención, respiración, gesto o cambio de idea.
- Mantener las pausas que ayudan a comprender.
- Evitar silencios accidentales.
- Priorizar continuidad de voz sobre una transición visual llamativa.
- Alternar momentos de energía con momentos de lectura.
- Introducir un cambio visual significativo cada 2–4 segundos cuando el contenido lo permita: corte, título, icono, zoom o cambio de composición.
- No activar simultáneamente un zoom fuerte, un título grande, un icono y una transición.

---

## 12. Colorización

### Objetivo

Mejorar consistencia, piel y contraste sin producir un aspecto artificial.

### Orden de trabajo

1. Balance de blancos.
2. Exposición.
3. Contraste.
4. Saturación.
5. Piel.
6. Coherencia entre planos.
7. Viñeta o ajuste local, solo si es necesario.

### Criterios

- Mantener tonos de piel naturales.
- Proteger morados y naranjas corporativos de sobresaturación.
- Aplicar contraste moderado.
- Levantar ligeramente un rostro oscuro antes de aclarar todo el plano.
- Evitar negros empastados y blancos recortados.
- Usar nitidez suave; no amplificar compresión ni ruido.

---

## 13. Diseño sonoro

### Voz

- Es el elemento prioritario.
- Objetivo orientativo: **−16 LUFS integrados**.
- Pico máximo orientativo: **−1.5 dBTP**.
- Aplicar reducción de ruido y ecualización solamente cuando sea necesario.

### Música de fondo

- Debe sentirse más que escucharse.
- Objetivo inicial recomendado: aproximadamente **−30 a −34 LUFS** antes de mezclar con la voz.
- Aplicar ducking adicional de 2–4 dB durante las frases.
- Fundidos de entrada y salida suaves.
- Evitar melodías que compitan con la dicción.

### Efectos

- Iconos destacados: magia, destello o campana suave.
- Cambios de bloque: woosh corto.
- Títulos principales: impacto suave opcional.
- Mantener los efectos normalmente entre **−22 y −16 dBFS de pico**, según densidad de la mezcla.
- Verificar la mezcla en audífonos y en el altavoz de un teléfono.

---

## 14. Flujo de trabajo replicable

### Etapa A — Comprensión

1. Inventariar videos, audios, imágenes, logos y documentos.
2. Transcribir toda la voz.
3. Identificar inicio y final real de cada frase.
4. Registrar gestos, miradas, manos, objetos y espacios negativos.
5. Crear un mapa de escenas y palabras clave.

Si se utiliza una herramienta de análisis multimodal, sus tiempos deben verificarse contra el audio real. Nunca guardar claves API dentro de archivos del proyecto.

### Etapa B — Montaje base

1. Construir el relato con la voz.
2. Elegir las mejores tomas por significado y gesto.
3. Retirar pausas accidentales sin afectar naturalidad.
4. Conservar una copia del montaje antes de cambios estructurales.

### Etapa C — Diseño

1. Diseñar la única tarjeta inicial.
2. Crear palabras clave flotantes.
3. Integrar iconos siguiendo los gestos.
4. Añadir subtítulos completos.
5. Comprobar que ningún elemento cubra el rostro.

### Etapa D — Dinamismo

1. Marcar planos demasiado estáticos.
2. Elegir entre zoom in, zoom out, punch-in o reencuadre.
3. Animar títulos principales.
4. Animar iconos y gráficos.
5. Añadir transiciones solo donde exista cambio de bloque.

### Etapa E — Acabado

1. Igualar color.
2. Limpiar y nivelar voz.
3. Añadir música y efectos en pistas separadas.
4. Revisar sincronización audiovisual.
5. Exportar un archivo de revisión.
6. Corregir y generar el archivo final.

---

## 15. Estructura recomendada de pistas en DaVinci Resolve

### Video

- **V1:** montaje principal.
- **V2:** transiciones, parches y recursos de apoyo.
- **V3:** títulos, subtítulos, iconos y gráficos.
- **V4:** recursos extraordinarios o máscaras, solo cuando sean necesarios.

### Audio

- **A1–A2:** voz principal o canales originales.
- **A3:** música.
- **A4:** efectos de aparición.
- **A5:** transiciones y efectos adicionales.

Mantener nombres descriptivos y evitar mezclar voz, música y efectos en un mismo archivo cuando el proyecto requiera ajustes posteriores.

---

## 16. Parámetros de animación reutilizables

| Elemento | Entrada | Permanencia | Salida |
|---|---|---|---|
| Tarjeta inicial | 9–12 f, escala 90→100 %, +30 px | Estática o brillo único | 6–8 f, opacidad |
| Título principal | 8–12 f, escala 92→103→100 % | 1.2–2.8 s | 5–8 f |
| Icono | 8–12 f, escala 80→100 %, flotación | 1.5–3 s | 5–8 f |
| Subtítulo | 2–4 f de opacidad | Según frase | 2–4 f |
| Zoom progresivo | 24–60 f | — | Puede terminar en corte |
| Punch-in | 5–8 f | 12–30 f | 6–10 f |
| Disolución | 6–10 f | — | — |

`f` = fotogramas a 30 fps.

---

## 17. Reglas de decisión rápida

- **¿El plano está estático?** Aplicar un zoom progresivo pequeño o animar el título, no ambos con intensidad alta.
- **¿La persona señala?** Colocar el icono en la dirección del gesto y sincronizar su entrada.
- **¿Se menciona una cifra o fecha?** Usar palabra clave con relieve y mantenerla el tiempo suficiente para leerla.
- **¿Cambia la localización?** Utilizar transición suave; añadir woosh si el cambio es importante.
- **¿El fondo está cargado?** Añadir sombra o degradado localizado, no una tarjeta completa.
- **¿El rostro está cerca del borde superior?** Mover el título al lateral o reducirlo.
- **¿Ya hay animación incorporada en el material?** Reducir los gráficos adicionales y conservar únicamente subtítulos necesarios.

---

## 18. Control de calidad obligatorio

### Imagen

- [ ] Formato 9:16 correcto.
- [ ] Ningún título o icono tapa el rostro.
- [ ] Los textos respetan zonas seguras.
- [ ] Los zooms no cortan cabeza, manos ni objetos importantes.
- [ ] Los movimientos no producen saltos.
- [ ] El color es consistente entre escenas.
- [ ] Los iconos conservan proporción y nitidez.
- [ ] La tarjeta inicial es la única tarjeta pesada.

### Movimiento

- [ ] Cada animación tiene una razón narrativa.
- [ ] Los títulos principales tienen entrada y salida suaves.
- [ ] Los iconos aparecen sincronizados con voz o gesto.
- [ ] Hay dinamismo en planos estáticos, sin zoom excesivo.
- [ ] Las transiciones no cortan palabras ni respiraciones.

### Audio

- [ ] La voz se entiende en todo momento.
- [ ] La música permanece detrás de la voz.
- [ ] Los efectos coinciden con apariciones y cortes.
- [ ] No hay saturación, clics ni silencios accidentales.
- [ ] El inicio y el final tienen fundidos adecuados.

### Entrega

- [ ] Se conserva una copia anterior antes de reemplazar el montaje.
- [ ] El archivo final contiene los últimos cambios manuales.
- [ ] La duración de audio y video coincide.
- [ ] Se revisó el video completo después de exportar.
- [ ] El nombre de entrega incluye versión o fecha.

---

## 19. Errores que este sistema debe evitar

- Repetir tarjetas moradas grandes en todas las escenas.
- Colocar textos sobre el rostro.
- Usar demasiadas palabras en títulos.
- Aplicar zoom in y zoom out sin intención.
- Hacer que todos los iconos reboten continuamente.
- Añadir transiciones llamativas en cada corte.
- Cubrir una animación ya diseñada con más gráficos.
- Mezclar la música al mismo nivel que la voz.
- Confiar en tiempos automáticos sin verificar el audio.
- Regenerar una línea de tiempo y perder cambios manuales.
- Exportar sin revisar el archivo final completo.

---

## 20. Resultado esperado

Una pieza creada con este sistema debe mostrar:

- Un gancho visual inmediato.
- Una sola tarjeta inicial bien diseñada.
- Títulos breves, animados y con relieve.
- Subtítulos limpios durante toda la voz.
- Iconos integrados con los gestos.
- Zooms suaves en escenas que admiten movimiento.
- Transiciones profesionales y discretas.
- Música baja y efectos sincronizados.
- Color corporativo consistente.
- Una narrativa clara y una llamada a la acción fácil de recordar.

