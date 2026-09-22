# Project Trading — Instrucciones para Agentes

## 1. Identidad del proyecto

Project Trading es un proyecto de ingeniería de software e ingeniería de IA cuyo objetivo es construir un sistema experimental de trading y, simultáneamente, desarrollar habilidades profesionales en:

* Ingeniería de IA (AI Engineering).
* Agentes de IA.
* Orquestación de agentes.
* Desarrollo guiado por especificaciones (SPEC-driven development).
* MCP.
* Arquitectura de software.
* Desarrollo en Python.
* Testing.
* Git y control de versiones.
* Integración de APIs.
* Ingeniería de datos.
* Backtesting.
* Gestión de riesgo.
* Diseño de sistemas de trading.
* Documentación técnica.

Este proyecto no consiste únicamente en construir una aplicación de trading.

También es un laboratorio para aprender a diseñar, supervisar, probar, documentar y mejorar sistemas de software construidos con asistencia de agentes de IA.

El proyecto debe permanecer comprensible y reproducible para un desarrollador o agente competente que se incorpore al proyecto meses o años después.

---

# 2. Principios fundamentales

El proyecto sigue estos principios:

1. Comprender antes de automatizar.
2. Automatizar el trabajo repetitivo cuando sea seguro y útil.
3. Documentar las decisiones importantes.
4. Probar antes de confiar.
5. Preferir soluciones simples antes que complejidad innecesaria.
6. Mantener una arquitectura modular y reemplazable.
7. Mantener los controles de trading determinísticos.
8. Considerar el código generado por IA como no confiable hasta que sea revisado y probado.
9. Realizar mejoras pequeñas y verificables.
10. No optimizar por cantidad de código.
11. Priorizar la reproducibilidad sobre la comodidad.
12. Mantener la revisión humana como parte del proceso de desarrollo.

Principio principal de trabajo:

> Resolver una pequeña cosa por sesión.

---

# 3. Fuente de verdad

El repositorio es la fuente de verdad principal del proyecto.

El chat, las conversaciones anteriores y el contexto temporal de los agentes no deben considerarse memoria permanente del proyecto.

Las decisiones importantes, cambios de arquitectura, detalles de implementación, limitaciones y conocimientos operativos deben registrarse en archivos versionados dentro del repositorio.

Cuando la información de una conversación entre en conflicto con el repositorio, se debe inspeccionar el repositorio antes de asumir cuál es el estado correcto.

No asumir que la implementación actual coincide con conversaciones anteriores.

El estado real del repositorio es la autoridad.

---

# 4. Jerarquía de instrucciones

Antes de realizar cualquier trabajo, el agente debe inspeccionar:

1. `AGENTS.md`
2. `docs/memory.md`
3. `ROADMAP.md`
4. La SPEC correspondiente.
5. La implementación y los tests actuales.

Cuando se trabaje dentro de un subdirectorio, también se debe comprobar si existe un `AGENTS.md` más específico aplicable a ese ámbito.

Las instrucciones más específicas pueden complementar las generales, pero no deben contradecir silenciosamente las reglas de seguridad o arquitectura del proyecto.

Cuando existan instrucciones contradictorias o requisitos ambiguos:

* detenerse;
* identificar el conflicto;
* explicarlo;
* pedir aclaraciones cuando sea necesario.

No inventar requisitos para resolver ambigüedades.

---

# 5. Estructura del proyecto

La estructura del proyecto puede evolucionar con el tiempo.

No crear todas las carpetas posibles de manera anticipada.

Las carpetas deben crearse cuando exista una necesidad real y justificada.

La estructura general esperada es:

```text
/project-trading

AGENTS.md
README.md
ROADMAP.md

/docs/
    memory.md

/specs/

src/
tests/

agents/
data/
strategies/
risk/
backtesting/
execution/
database/
api/
frontend/
mcp/
```

Esta estructura es orientativa y puede evolucionar.

No crear carpetas vacías o componentes arquitectónicos solamente porque aparecen en este documento.

---

# 6. Flujo de trabajo

Toda tarea significativa debe seguir este flujo:

```text
CONTEXTO
↓
TAREA
↓
PLAN
↓
IMPLEMENTACIÓN
↓
TEST
↓
REVISIÓN
↓
DOCUMENTACIÓN
↓
GIT
```

Antes de implementar:

1. Comprender la tarea.
2. Inspeccionar el repositorio actual.
3. Leer la documentación relevante.
4. Identificar la SPEC correspondiente.
5. Determinar el cambio mínimo necesario.
6. Comunicar brevemente el plan.

Durante la implementación:

* modificar únicamente los archivos necesarios;
* respetar la arquitectura existente;
* evitar dependencias innecesarias;
* evitar refactorizaciones no relacionadas.

Después de implementar:

* ejecutar los tests correspondientes;
* inspeccionar los cambios;
* verificar la documentación;
* comprobar el estado de Git;
* resumir lo realizado.

No continuar automáticamente con otra tarea no relacionada.

---

# 7. Alcance de las tareas

Los agentes deben respetar estrictamente el alcance de la tarea asignada.

Un agente NO debe:

* modificar archivos sin relación con la tarea;
* rediseñar la arquitectura por iniciativa propia;
* introducir dependencias innecesarias;
* reescribir componentes funcionales sin justificación;
* eliminar código funcional sin explicar el motivo;
* inventar APIs;
* inventar requisitos;
* saltarse tests;
* ocultar errores;
* cambiar silenciosamente las convenciones del proyecto;
* realizar tareas no solicitadas.

Si el agente detecta una mejora útil que está fuera del alcance de la tarea:

1. no debe implementarla automáticamente;
2. debe describirla;
3. puede registrarla como propuesta o tarea futura cuando corresponda.

Controlar el alcance es más importante que maximizar la cantidad de trabajo realizado durante una sesión.

---

# 8. Tamaño de las sesiones

El desarrollo está deliberadamente dividido en sesiones pequeñas.

Tiempo disponible aproximado:

```text
20–30 minutos
3–4 sesiones por semana
```

Las tareas deben ser suficientemente pequeñas para producir, siempre que sea posible, una mejora concreta y verificable durante una sesión.

Mala tarea:

```text
Construir todo el sistema de market data.
```

Mejor tarea:

```text
Crear la interfaz MarketDataProvider.
```

El agente debe preferir una implementación incremental antes que cambios grandes y difíciles de controlar.

---

# 9. Desarrollo guiado por SPEC

Las especificaciones se almacenan en:

```text
/specs/
```

Algunas posibles SPEC son:

```text
architecture.md
market-data.md
strategy.md
backtesting.md
risk.md
agents.md
mcp.md
broker.md
```

Antes de implementar una funcionalidad importante:

1. identificar la SPEC correspondiente;
2. leerla;
3. comprobar el alcance definido;
4. identificar los criterios de aceptación;
5. implementar solamente lo necesario;
6. probar los criterios de aceptación.

Si no existe una SPEC necesaria:

* no inventar requisitos importantes;
* proponer crear o actualizar la SPEC cuando la funcionalidad tenga relevancia arquitectónica.

La implementación debe respetar la SPEC.

Si la implementación y la SPEC no coinciden, no elegir silenciosamente una de las dos.

Informar la discrepancia.

Cuando una decisión temporal pase a formar parte de la arquitectura oficial, actualizar la SPEC y la documentación correspondiente.

---

# 10. Agentes de IA

Los agentes de IA son una parte fundamental de Project Trading desde el comienzo.

Los agentes pueden ayudar con:

* programación;
* generación de código;
* investigación;
* testing;
* debugging;
* refactoring;
* documentación;
* preparación de datos;
* tareas repetitivas;
* análisis;
* automatización.

El proyecto también tiene como objetivo desarrollar habilidades prácticas de AI Engineering.

Por lo tanto, los agentes deben utilizarse de manera intencional y no únicamente como generadores de código.

Flujo recomendado:

```text
DEFINIR
↓
PROPORCIONAR CONTEXTO
↓
CONSULTAR SPEC
↓
DEFINIR RESTRICCIONES
↓
DELEGAR
↓
IMPLEMENTAR
↓
REVISAR
↓
PROBAR
↓
VALIDAR
↓
DOCUMENTAR
```

Nunca aceptar código generado por IA ciegamente.

El desarrollador humano continúa siendo responsable de comprender los cambios importantes.

---

# 11. Delegación entre agentes

Cuando se delegue una tarea a otro agente, proporcionar:

* objetivo;
* contexto relevante;
* SPEC aplicable;
* archivos relevantes;
* comportamiento esperado;
* restricciones;
* requisitos de testing;
* alcance explícito.

El agente delegado debe informar:

* qué modificó;
* por qué lo modificó;
* archivos modificados;
* tests realizados;
* limitaciones conocidas;
* problemas pendientes.

Los agentes no deben crear cadenas innecesarias de agentes.

La orquestación debe aportar un beneficio real.

---

# 12. Revisión humana

La revisión humana es obligatoria para cambios significativos.

El desarrollador humano debe poder comprender:

* qué cambió;
* por qué cambió;
* qué supuestos se utilizaron;
* qué tests se realizaron.

Los cambios relacionados con:

* arquitectura;
* seguridad;
* trading;
* brokers;
* lógica financiera;
* datos financieros;

requieren revisión humana antes de ser aceptados.

El resultado generado por IA nunca se considera automáticamente correcto.

---

# 13. Principios de código

Preferir:

* nombres claros;
* funciones pequeñas;
* interfaces explícitas;
* componentes modulares;
* comportamiento predecible;
* type hints cuando sean útiles;
* código testeable;
* lógica determinística cuando corresponda;
* dependency injection cuando mejore la capacidad de testing;
* manejo de errores claro.

Evitar:

* abstracciones innecesarias;
* optimización prematura;
* estado global oculto;
* lógica de negocio duplicada;
* valores mágicos sin explicación;
* dependencias innecesarias;
* componentes excesivamente acoplados.

No refactorizar código no relacionado solamente porque podría mejorarse.

---

# 14. Dependencias

Antes de agregar una dependencia, evaluar:

* ¿Es realmente necesaria?
* ¿La biblioteca estándar puede resolver el problema adecuadamente?
* ¿La dependencia está mantenida?
* ¿Presenta riesgos de seguridad o licencia?
* ¿Aumenta significativamente la complejidad?
* ¿Aporta un beneficio real?

No instalar paquetes simplemente por comodidad.

Las dependencias importantes deben quedar registradas en la documentación correspondiente.

---

# 15. Testing

Los tests forman parte de la implementación y no son una etapa opcional.

Los tests deben agregarse o actualizarse cuando cambie el comportamiento del sistema.

Según el componente, pueden utilizarse:

* unit tests;
* integration tests;
* API tests;
* tests de validación de datos;
* tests de estrategias;
* tests de backtesting;
* tests del risk engine;
* tests de ejecución.

Antes de considerar terminada una tarea significativa:

1. ejecutar los tests relevantes;
2. analizar los fallos;
3. corregir los fallos legítimos;
4. informar el resultado.

Nunca ocultar tests fallidos.

Nunca modificar tests únicamente para hacer que una implementación incorrecta parezca correcta.

---

# 16. Testing de lógica de trading

Los cálculos relacionados con trading requieren especial cuidado.

Los tests deben cubrir, cuando corresponda:

* comportamiento esperado;
* casos límite;
* datos faltantes;
* datos inválidos;
* condiciones de frontera;
* costos de transacción;
* slippage;
* límites de riesgo;
* condiciones inesperadas del mercado cuando puedan probarse.

Los cálculos financieros deben ser determinísticos siempre que sea posible.

Cuando se utilicen tolerancias numéricas, deben ser explícitas.

---

# 17. Git

Git forma parte obligatoria del workflow del proyecto.

Después de un cambio significativo:

1. inspeccionar los archivos modificados;
2. ejecutar los tests correspondientes;
3. verificar la documentación;
4. revisar `git status`;
5. revisar el diff;
6. crear un commit claro cuando corresponda.

Los mensajes de commit deben describir el cambio.

Ejemplos:

```text
feat: add market data provider
fix: validate missing price data
test: add RSI strategy coverage
docs: update project memory
refactor: separate broker adapter
```

Evitar mezclar cambios no relacionados dentro del mismo commit.

No crear commits que contengan cambios que el usuario no haya tenido oportunidad de comprender o revisar.

No realizar `push` a repositorios remotos automáticamente salvo que haya sido solicitado explícitamente.

---

# 18. GitHub

GitHub forma parte del workflow de control de versiones, pero debe mantenerse separado de las decisiones de desarrollo local.

No crear ni modificar un repositorio remoto de GitHub salvo que se solicite explícitamente.

Antes de realizar un `push`:

* verificar el estado del repositorio;
* verificar `.gitignore`;
* comprobar que no existan secretos;
* revisar los archivos importantes;
* revisar el historial de commits;
* confirmar el repositorio remoto de destino.

Nunca publicar secretos o credenciales privadas.

---

# 19. Documentación

La documentación forma parte de la implementación.

Los principales documentos incluyen:

```text
README.md
ROADMAP.md
/docs/memory.md
/specs/
```

La documentación debe explicar decisiones y comportamientos importantes, no simplemente repetir el código.

Debe mantenerse:

* concisa;
* estructurada;
* actualizada;
* útil.

No convertir la documentación en un diario desordenado.

---

# 20. Memoria técnica del proyecto

La memoria técnica persistente se encuentra en:

```text
/docs/memory.md
```

Debe mantenerse organizada y ser útil para un desarrollador o agente que se incorpore al proyecto en el futuro.

Estructura recomendada:

```text
# Project Memory

## Current State

## Completed Work

## Architecture Decisions

## Important Changes

## Problems and Solutions

## Tools and Agents

## Known Limitations

## Pending Work

## Next Steps

## Useful Commands

## Important References
```

Después de una implementación significativa:

1. revisar qué cambió;
2. actualizar `memory.md`;
3. registrar decisiones importantes;
4. registrar problemas y soluciones relevantes;
5. registrar limitaciones pendientes;
6. actualizar los próximos pasos;
7. comprobar que un agente nuevo pueda comprender el estado actual.

No registrar cada acción trivial.

---

# 21. Arquitectura

Project Trading debe utilizar una arquitectura modular.

Los componentes principales deben tener responsabilidades e interfaces claras.

Arquitectura conceptual esperada:

```text
Market Data
↓
Analysis / Agents
↓
Decision Engine
↓
Risk Engine
↓
Execution Engine
↓
Broker
```

Los componentes deben permanecer reemplazables siempre que resulte práctico.

La lógica de trading no debe depender directamente de una implementación específica de broker.

---

# 22. Abstracción del broker

La funcionalidad específica de cada broker debe aislarse detrás de una abstracción como:

```text
BrokerAdapter
```

Posibles implementaciones futuras:

```text
IOLAdapter
CocosAdapter
BullMarketAdapter
AlpacaAdapter
```

Son solamente ejemplos y no implican que todas deban implementarse.

Preferir APIs oficiales antes que scraping cuando exista una API oficial.

Antes de implementar una integración con un broker:

1. verificar la documentación oficial vigente;
2. verificar los requisitos de autenticación;
3. verificar las operaciones disponibles;
4. verificar límites de uso;
5. verificar disponibilidad de sandbox o paper trading;
6. documentar las limitaciones relevantes.

No inventar el comportamiento de una API de broker.

---

# 23. Seguridad del sistema de trading

Project Trading es un proyecto experimental de software e investigación.

Durante las primeras etapas:

## NO UTILIZAR DINERO REAL.

El sistema debe permitir experimentación segura antes de considerar cualquier ejecución real.

Las posibles decisiones del sistema incluyen:

```text
BUY
SELL
HOLD
NO TRADE
```

`NO TRADE` es una decisión válida.

El sistema nunca debe diseñarse alrededor de una obligación de generar ganancias diarias.

Ningún componente debe forzar una operación simplemente porque se espera una oportunidad.

Los controles de riesgo deben ser determinísticos y poder aplicarse independientemente de las recomendaciones de la IA.

---

# 24. IA y decisiones de trading

La IA puede participar en:

* análisis;
* generación de señales;
* generación de hipótesis;
* investigación de mercado;
* experimentación de estrategias;
* clasificación;
* explicación.

Sin embargo:

> LA IA PROPONE. EL SOFTWARE CONTROLA.

Las recomendaciones de IA deben pasar por validaciones determinísticas y controles de riesgo antes de cualquier ejecución.

La IA no debe poder saltarse:

* límites de riesgo;
* límites de posición;
* validaciones;
* controles de ejecución;
* permisos de trading;
* mecanismos de seguridad.

Una señal generada por IA no constituye automáticamente una orden ejecutable.

---

# 25. Estrategia baseline

Project Trading debe mantener una estrategia baseline simple y explicable.

El baseline existe para poder evaluar enfoques experimentales contra una referencia:

```text
ESTRATEGIA BASE
VS
ESTRATEGIA + IA
```

La existencia del baseline no significa que el desarrollo deba realizarse sin agentes de IA.

La Ingeniería de IA comienza desde el inicio del proyecto.

El baseline existe para investigación y comparación.

---

# 26. Backtesting

El backtesting debe intentar representar condiciones realistas.

Las métricas relevantes incluyen:

* retorno;
* P&L;
* drawdown;
* win rate;
* profit factor;
* volatilidad;
* Sharpe ratio;
* cantidad de operaciones;
* costos de transacción;
* slippage;
* pérdida máxima.

En etapas posteriores se pueden investigar:

* out-of-sample testing;
* walk-forward analysis;
* diferentes regímenes de mercado;
* robustez;
* análisis de sensibilidad;
* overfitting;
* estabilidad de parámetros.

Los resultados de backtesting no deben interpretarse como garantía del rendimiento futuro.

---

# 27. Integridad de datos

Los datos de mercado deben considerarse potencialmente:

* incompletos;
* retrasados;
* incorrectos;
* duplicados;
* inconsistentes.

Los sistemas que procesen datos de mercado deben validar, cuando corresponda:

* timestamps;
* valores faltantes;
* duplicados;
* valores inesperados;
* tipos de datos;
* orden temporal;
* límites o sesiones de mercado.

No reparar silenciosamente datos financieros sospechosos sin documentar la transformación realizada.

Los supuestos sobre los datos deben ser explícitos.

---

# 28. Seguridad de credenciales

Nunca almacenar en el código o en el control de versiones:

* API keys;
* passwords;
* authentication tokens;
* credenciales privadas;
* certificados privados;
* secrets.

Utilizar variables de entorno o mecanismos apropiados de gestión de secretos.

Los archivos sensibles deben excluirse mediante `.gitignore` cuando corresponda.

Antes de realizar un commit o `push`:

* revisar los archivos;
* comprobar la existencia de secretos;
* verificar `.gitignore`.

Nunca exponer credenciales en:

* logs;
* documentación;
* tests;
* prompts;
* resultados de agentes.

---

# 29. MCP

MCP puede incorporarse progresivamente cuando proporcione un beneficio real.

Posibles capacidades:

```text
filesystem
git
python
database
market-data
testing
documentation
```

No incorporar MCP simplemente porque sea técnicamente interesante.

Antes de incorporar una herramienta MCP evaluar:

* utilidad;
* seguridad;
* permisos;
* mantenimiento;
* confiabilidad;
* impacto arquitectónico;
* beneficio real para el desarrollo.

Las herramientas MCP deben utilizar permisos mínimos siempre que sea posible.

Una integración MCP nunca debe saltarse los controles de seguridad del proyecto.

---

# 30. Herramientas y automatización

La automatización debe eliminar trabajo repetitivo sin eliminar el control humano necesario.

Puede utilizarse para:

* tests;
* linting;
* formatting;
* comprobaciones de documentación;
* verificaciones del repositorio;
* validación de datos;
* investigación repetitiva;
* workflows de agentes.

La automatización debe ser:

* observable;
* reproducible;
* testeable;
* documentada.

Evitar automatizaciones ocultas que modifiquen el estado importante del proyecto sin visibilidad clara.

---

# 31. Manejo de errores

Los errores deben ser visibles y accionables.

No:

* ocultar excepciones silenciosamente;
* ocultar fallos de APIs;
* sustituir datos inválidos silenciosamente;
* fingir que una operación tuvo éxito;
* fabricar resultados exitosos.

Cuando una operación falle:

1. informar el fallo;
2. identificar la causa probable si se conoce;
3. conservar información útil para diagnóstico;
4. proponer el siguiente paso.

---

# 32. APIs externas e investigación

Al implementar integraciones con servicios externos:

* verificar la documentación oficial vigente;
* no depender de suposiciones antiguas;
* no inventar endpoints;
* no inventar flujos de autenticación;
* documentar las restricciones relevantes.

Para sistemas externos que cambian frecuentemente, verificar la información antes de implementar.

---

# 33. Cambios de arquitectura no autorizados

Un agente puede proponer mejoras arquitectónicas.

Un agente no debe introducir por iniciativa propia cambios importantes como:

* reemplazar frameworks;
* reemplazar bases de datos;
* cambiar el lenguaje principal;
* reemplazar la estrategia de testing;
* agregar infraestructura compleja;
* introducir un framework de orquestación;
* rediseñar la arquitectura central del sistema de trading.

Los cambios arquitectónicos importantes requieren revisión y aprobación explícita.

---

# 34. Trabajo no informado

Los agentes no deben realizar trabajo significativo sin informarlo.

El agente debe comunicar claramente:

* archivos creados;
* archivos modificados;
* archivos eliminados;
* dependencias agregadas;
* comandos ejecutados;
* tests ejecutados;
* decisiones importantes;
* problemas pendientes.

Los cambios inesperados deben investigarse antes de continuar.

---

# 35. Definition of Done

Una tarea significativa no se considera terminada simplemente porque se escribió código.

Una tarea se considera terminada cuando corresponda:

* la implementación existe;
* se respetó el alcance;
* los tests relevantes pasan;
* los errores fueron comprendidos;
* la documentación fue actualizada;
* `docs/memory.md` fue actualizado cuando corresponde;
* el diff de Git fue revisado;
* no existen secretos expuestos;
* el resultado coincide con la SPEC correspondiente;
* las limitaciones restantes son conocidas;
* el siguiente paso está definido.

---

# 36. Informe al finalizar una sesión

Al finalizar una sesión significativa, informar siempre:

```text
✅ Completado

📁 Archivos modificados

🧪 Tests ejecutados

📚 Documentación actualizada

🧠 Qué aprendimos

⚠️ Problemas / riesgos

📝 Estado de Git / Commit

➡️ Próximo paso
```

El siguiente paso debe ser pequeño y estar claramente definido.

No continuar automáticamente con la siguiente tarea.

---

# 37. Estilo de comunicación

Los agentes deben comunicarse de forma clara y práctica.

Preferir:

* explicaciones concisas;
* supuestos explícitos;
* referencias concretas a archivos;
* resultados claros de los tests;
* próximos pasos accionables.

Cuando aparezca un concepto técnico importante, explicar:

1. qué hace;
2. por qué existe;
3. qué problema resuelve;
4. cómo podemos comprobar que funciona.

No convertir tareas simples en clases teóricas innecesariamente extensas.

---

# 38. Objetivo de aprendizaje

Project Trading también es un proyecto educativo.

El desarrollador debe aprender progresivamente:

* cómo funcionan los agentes;
* cómo delegar tareas;
* cómo escribir instrucciones efectivas para agentes;
* cómo crear y mantener SPECs;
* cómo utilizar MCP;
* cómo revisar código generado por IA;
* cómo diseñar arquitectura de software;
* cómo probar sistemas desarrollados con IA;
* cómo utilizar Git profesionalmente;
* cómo construir infraestructura de trading confiable.

El objetivo no es únicamente producir software.

El objetivo es desarrollar la capacidad de supervisar y construir sistemas de software utilizando IA.

---

# 39. Principio final

Project Trading debe ser simultáneamente:

1. Un proyecto real de ingeniería de software.
2. Un laboratorio de AI Engineering.
3. Un sistema experimental de trading.
4. Un proyecto documentado y reproducible.

La prioridad es:

```text
COMPRENDER
+
AUTOMATIZAR
+
DOCUMENTAR
+
PROBAR
+
MEJORAR
```

No construir la mayor cantidad posible de código.

Construir un sistema que un desarrollador o agente competente pueda comprender, probar, mantener y continuar años después.

## Resolver una pequeña cosa por sesión.
