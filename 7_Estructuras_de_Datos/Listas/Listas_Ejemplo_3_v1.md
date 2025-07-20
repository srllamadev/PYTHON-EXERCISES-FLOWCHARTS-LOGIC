Aquí tienes el contenido en formato Markdown para GitHub:

markdown

Copiar
# Explicación de Variables Globales

Las variables globales en Python son aquellas definidas fuera de cualquier función o clase, en el nivel superior de un módulo. En este ejemplo:

```python
CATEGORIAS = ["Electrónicos", "Ropa", "Alimentos", "Muebles", "Juguetes"]
ALMACENES = ["Norte", "Sur", "Centro", "Este", "Oeste"]
PROVEEDORES = ["ProveedorA", "ProveedorB", "ProveedorC", "ProveedorD"]
```

Características Clave:
Ámbito (Scope):
Accesibles desde cualquier parte del módulo.
Pueden ser leídas dentro de funciones/clases sin declaración especial.
Para modificarlas dentro de funciones se necesita global.
Uso en este sistema:
Configuración centralizada: Actúan como constantes de configuración.
Consistencia: Garantizan valores uniformes en todo el sistema.
Facilidad de mantenimiento: Cambios en un solo lugar afectan toda la aplicación.
Ventajas:
Evitan "hardcoding" repetido en múltiples lugares.
Mejoran la legibilidad del código.
Facilitan la internacionalización o cambios futuros.
Alternativas Consideradas:
Podrían estar en un archivo de configuración separado.
En sistemas más complejos, podrían cargarse desde una base de datos.
Para valores que cambian frecuentemente, usar variables de entorno.
Por qué Usarlas con Cuidado:
Estado compartido: Pueden causar efectos laterales inesperados.
Dificultad para rastrear cambios: Cualquier parte del código puede modificarlas.
Problemas en concurrencia: No son thread-safe.
Mejores Prácticas Observadas:
Usar mayúsculas para indicar que son "constantes".
No modificarlas después de la inicialización.
Usarlas solo para datos verdaderamente globales.
Documentar su propósito claramente.
Características Avanzadas del Sistema
Gestión Multi-Almacén:
Inventario distribuido con seguimiento por ubicación.
Movimientos específicos por almacén.
Sistema FIFO (First-In-First-Out):
Seguimiento de lotes y fechas de ingreso.
Priorización de stock más antiguo.
Reabastecimiento Automático:
Umbrales configurables por categoría.
Cálculo de tiempo de reposición por proveedor.
Pedidos automáticos con fechas estimadas.
Análisis Avanzado:
Cálculo de valor de inventario.
Ratios de rotación de productos.
Visualización de tendencias temporales.
Simulación Completa:
Generación de datos iniciales.
Simulación histórica de movimientos.
Integración con visualización (matplotlib).
Instalar matplotlib ejecutando este comando en tu terminal:

```bash
pip install matplotlib
Si tienes múltiples versiones de Python, usa:
```

```bash
pip3 install matplotlib
Después de instalar, verifica que se instaló correctamente:
```
```bash
pip show matplotlib
```