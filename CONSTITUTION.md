# Constitución de Project Trading

La Constitución establece los principios fundamentales que rigen el proyecto. Las instrucciones operativas deben respetarla.

1. **La IA propone; el software controla.** Las propuestas generadas por IA no sustituyen las validaciones determinísticas ni los controles del sistema.
2. **Desarrollo guiado por especificaciones.** Toda funcionalidad debe estar respaldada por una SPEC antes de implementarse.
3. **La SPEC conduce al código.** Ante un cambio de comportamiento, primero se modifica o crea la SPEC y luego se adapta el código.
4. **Clarificación antes de implementación.** Las ambigüedades relevantes deben resolverse antes de comenzar una tarea.
5. **Plan antes de ejecutar.** Toda funcionalidad debe dividirse en tareas pequeñas y verificables.
6. **Una tarea a la vez.** No se deben implementar simultáneamente varias tareas independientes.
7. **Tests primero.** Para cada comportamiento nuevo, se definen primero los tests correspondientes y después se implementa el comportamiento.
8. **Validación obligatoria.** Una implementación no está terminada hasta ejecutar los tests y las validaciones relevantes.
9. **Cambios pequeños y revisables.** Se evitan cambios no relacionados, refactors innecesarios y expansión de alcance.
10. **No sobrearquitectura.** No se crean infraestructura, abstracciones o dependencias futuras sin una necesidad concreta.
11. **Seguridad y control.** No se incluyen secretos, credenciales ni API keys en el repositorio.
12. **Trading controlado.** Durante las etapas iniciales no se utiliza dinero real.
13. **Git y trazabilidad.** Los cambios importantes deben registrarse mediante commits claros.
14. **Revisión humana.** La IA puede implementar y validar técnicamente, pero las decisiones importantes de alcance, arquitectura y cambios de comportamiento requieren revisión humana.
