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
- Implementado `MarketDataSeries` en `src/market_data_series.py`.
- Añadidos tests unitarios en `tests/test_market_data_series.py`.
- Implementada la utilidad `calculate_price_change` en `src/price_change.py`.
- Añadidos tests unitarios en `tests/test_price_change.py`.

## Decisiones de componentes de Market Data

- La serie comienza vacía y recibe observaciones mediante `add`.
- La colección se mantiene privada, ordenada por timestamp y solo permite un instrumento.
- La colección se puede recorrer en orden cronológico mediante una instantánea de solo lectura.
- `latest` devuelve la observación más reciente o `None` cuando la serie está vacía; se elige ausencia explícita porque una serie vacía es un estado normal y no una condición excepcional.
- La consulta se limita a longitud, indexación, iteración y observación más reciente para mantener el contrato pequeño.
- `calculate_price_change` devuelve cambio absoluto y porcentual como una tupla de `Decimal`.

## Próximos pasos

- Definir la siguiente tarea pequeña y verificable.
- Crear nuevas especificaciones solo cuando una necesidad concreta lo justifique.
- Revisar humanamente la API de `MarketDataSeries` antes de realizar cambios adicionales.
