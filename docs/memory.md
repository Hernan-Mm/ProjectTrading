# Project Memory

## Estado actual

La estructura inicial fue creada y el contrato mínimo de Market Data está implementado. No existen proveedores externos, conexiones de red ni dependencias adicionales.

## Decisiones tomadas

- Mantener una arquitectura modular y reemplazable.
- Usar desarrollo guiado por especificaciones.
- Mantener los controles de trading determinísticos.
- Priorizar la reproducibilidad, el testing y la revisión humana.
- Representar un dato de mercado con un `dataclass` inmutable y validaciones determinísticas.
- Requerir timestamps con información de zona horaria y valores numéricos finitos para precio y volumen.

## Trabajo completado

- Implementado `MarketData` en `src/market_data.py`.
- Añadidos tests unitarios en `tests/test_market_data.py`.

## Próximos pasos

- Definir la siguiente tarea pequeña y verificable.
- Crear nuevas especificaciones solo cuando una necesidad concreta lo justifique.
