# Arquitectura conceptual inicial

## Objetivo

Definir una arquitectura modular para que los componentes puedan evolucionar y reemplazarse sin acoplar la lógica de trading a una implementación específica.

## Flujo conceptual

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

## Principios iniciales

- Cada componente debe tener responsabilidades e interfaces claras.
- La lógica de trading no debe depender directamente de un broker concreto.
- Las recomendaciones de IA deben pasar por validaciones determinísticas y controles de riesgo.
- La arquitectura se concretará de forma incremental mediante SPECs y necesidades reales.
