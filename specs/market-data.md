# SPEC-001 — Contrato de datos de mercado

## 1. Objetivo

Definir un contrato mínimo y agnóstico de proveedor para representar datos de mercado dentro de Project Trading.

El objetivo es permitir que el sistema consuma datos de diferentes fuentes sin acoplar la lógica interna de trading a un proveedor, broker o API concreta.

Esta SPEC define únicamente el contrato y su comportamiento básico.

No define todavía:

* un proveedor de datos concreto;
* una API externa;
* conexión con un broker;
* almacenamiento permanente;
* estrategia de trading;
* decisiones de compra o venta;
* ejecución de órdenes;
* uso de IA para generar señales.

---

## 2. Alcance

El componente debe poder representar un dato de mercado correspondiente a un instrumento financiero en un momento determinado.

Como mínimo, el dato debe contemplar:

* instrumento;
* timestamp;
* precio;
* volumen.

La representación debe permitir evolucionar posteriormente hacia datos OHLCV, distintos mercados y distintas fuentes de datos sin obligar a modificar la lógica de negocio existente.

---

## 3. Concepto principal

El sistema utilizará una representación interna de un dato de mercado.

Conceptualmente:

```text
MarketData
├── instrument
├── timestamp
├── price
└── volume
```

Los nombres concretos de clases, interfaces, tipos o archivos serán determinados durante la implementación siguiendo las convenciones del proyecto.

---

## 4. Requisitos funcionales

### RF-001 — Identificación del instrumento

Cada dato de mercado debe identificar de forma inequívoca el instrumento al que corresponde.

Ejemplo conceptual:

```text
AAPL
```

La SPEC no obliga a utilizar acciones estadounidenses ni ningún mercado específico.

---

### RF-002 — Timestamp

Cada dato debe contener el momento al que corresponde.

El timestamp debe permitir representar el instante de forma inequívoca.

La implementación debe evitar timestamps ambiguos relacionados con zonas horarias.

---

### RF-003 — Precio

Cada dato debe contener un precio numérico.

El precio debe representar un valor válido para el instrumento.

No se aceptarán valores que no puedan representar un precio válido.

---

### RF-004 — Volumen

Cada dato debe contener volumen.

El volumen debe ser un valor numérico no negativo.

---

### RF-005 — Inmutabilidad

Una vez creado un dato de mercado, sus valores no deberían modificarse.

Si se necesita representar un nuevo estado del mercado, debe crearse un nuevo dato.

---

## 5. Validaciones

La implementación debe rechazar datos inválidos.

Como mínimo:

* instrumento vacío o inválido → rechazo;
* timestamp inválido → rechazo;
* precio inválido o no positivo → rechazo;
* volumen negativo → rechazo.

Los detalles concretos de las excepciones o mecanismos de error quedan a criterio de la implementación, siempre que el comportamiento sea determinístico y testeable.

---

## 6. Independencia del proveedor

El modelo interno de Market Data no debe depender directamente de:

* un broker;
* una API externa;
* una biblioteca específica de un proveedor;
* credenciales;
* conexión de red.

Un proveedor externo podrá transformarse posteriormente al modelo definido por esta SPEC.

Conceptualmente:

```text
Proveedor externo
       ↓
Adapter / integración
       ↓
MarketData
       ↓
Sistema interno
```

---

## 7. Tests mínimos

La implementación debe incluir tests que comprueben como mínimo:

1. creación de un dato válido;
2. conservación correcta de sus valores;
3. rechazo de instrumento inválido;
4. rechazo de timestamp inválido;
5. rechazo de precio inválido;
6. rechazo de volumen negativo;
7. imposibilidad de modificar el dato después de su creación.

Los tests deben comprobar comportamiento, no detalles internos innecesarios de la implementación.

---

## 8. Fuera de alcance

Esta SPEC NO incluye:

* conexión a mercados reales;
* APIs de brokers;
* APIs de proveedores de Market Data;
* autenticación;
* API keys;
* almacenamiento en base de datos;
* streaming en tiempo real;
* WebSockets;
* históricos;
* backtesting;
* indicadores técnicos;
* estrategias;
* señales BUY/SELL;
* gestión de riesgo;
* ejecución de órdenes;
* agentes de IA.

Estas funcionalidades podrán tener SPECs posteriores cuando exista una necesidad concreta.

---

## 9. Criterios de aceptación

La SPEC se considera implementada cuando:

* existe una representación interna de Market Data;
* cumple las validaciones definidas;
* no depende de un proveedor externo;
* es testeable de forma determinística;
* los tests cubren los comportamientos mínimos definidos;
* no se incorporan funcionalidades fuera del alcance;
* la implementación respeta `AGENTS.md`.

---

## 10. Principio de diseño

La implementación debe ser deliberadamente pequeña.

No se debe crear infraestructura futura que esta SPEC no necesite.

El objetivo de esta primera implementación es establecer un contrato sólido y comprobable sobre el cual puedan construirse posteriormente otras partes de Project Trading.
