# SPEC-002 — Cálculo del cambio de precio

## 1. Objetivo

Definir el comportamiento de `calculate_price_change` al calcular el cambio absoluto y porcentual entre dos observaciones `MarketData`.

La función recibe una observación inicial y una observación final del mismo instrumento.

## 2. Alcance

Esta SPEC define únicamente:

* la relación temporal válida entre las observaciones;
* la validación de tipos;
* la validación del instrumento;
* el resultado del cálculo del cambio de precio.

No define indicadores, estrategias, proveedores, APIs, agentes ni ejecución de órdenes.

## 3. Requisitos funcionales

### RF-001 — Tipos de entrada

`initial` y `final` deben ser instancias de `MarketData`.

Si alguno de los argumentos tiene un tipo incorrecto, la operación debe producir un error determinístico de tipo `TypeError`.

### RF-002 — Instrumento

`initial` y `final` deben corresponder al mismo instrumento.

Si los instrumentos son diferentes, la operación debe producir un error determinístico de tipo `ValueError`.

### RF-003 — Consistencia temporal

La relación temporal entre las observaciones debe cumplir:

* `initial.timestamp < final.timestamp` → operación válida;
* `initial.timestamp == final.timestamp` → operación válida;
* `initial.timestamp > final.timestamp` → operación inválida.

Cuando `initial.timestamp > final.timestamp`, la operación debe producir un error determinístico de tipo `ValueError`.

Los timestamps de `MarketData` deben conservar las garantías definidas por la SPEC de Market Data.

### RF-004 — Cambio absoluto

Para una relación temporal válida, el cambio absoluto se calcula como:

```text
final.price - initial.price
```

### RF-005 — Cambio porcentual

Para una relación temporal válida, el cambio porcentual se calcula como:

```text
(final.price - initial.price) / initial.price * 100
```

El resultado debe conservar el comportamiento numérico definido por la implementación actual.

## 4. Criterios de aceptación

La SPEC se considera implementada cuando existen tests que comprueban como mínimo:

1. una observación final posterior es válida;
2. dos observaciones con el mismo timestamp son válidas;
3. una observación final anterior produce `ValueError`;
4. dos instrumentos diferentes siguen produciendo `ValueError`;
5. tipos de entrada incorrectos siguen produciendo `TypeError`;
6. los cálculos absoluto y porcentual existentes siguen produciendo sus resultados actuales.

El error por orden temporal inválido debe ser determinístico y no debe depender de servicios externos, estado global ni valores aleatorios.

## 5. Fuera de alcance

Esta SPEC no incluye:

* modificación o normalización de timestamps;
* conversión entre zonas horarias fuera de las garantías de `MarketData`;
* tolerancias temporales;
* ordenamiento de observaciones;
* indicadores técnicos;
* estrategias de trading;
* proveedores de datos;
* APIs;
* agentes;
* ejecución de órdenes.
