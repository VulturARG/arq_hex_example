# Arquitectura Hexagonal

### ¿Qué es la Arq. Hexagonal?
- Permite separar la lógica de negocios del resto de la implementación (frameworks, etc)
- Promueve la separación de asuntos mediante la encapsulación de la lógica en diferentes capas de la aplicación.
-Es una implementación de la llamada Arq. Limpia (Clean Architecture)
- Se la conoce también como arq. de puertos y adaptadores o arq. cebolla.

### Objetivo
El objetivo de usar una arquitectura limpia es tener sistemas:
- Independientes del framework.
- Testables.
- Independientes de la UI.
- Independientes de la base de datos.
- Independiente de agentes externos.
- Más tolerantes al cambio.
- Reutilizables.
- Mantenibles.

### Esquema

![img.png](img.png)

### Estructura de ejemplo

```
app
├───adapter
│   └───repositories
│       └───package
├───domain
│   └───package
│       └───tests
└───seudo_django
```
