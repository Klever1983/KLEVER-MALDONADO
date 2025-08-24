# Sistema de Gestión de Inventarios (con archivos y excepciones)

**Cómo ejecutar**  
1. Descarga `inventario.py`.  
2. En una terminal, navega hasta la carpeta del archivo.  
3. Ejecuta:  
   ```bash
   python inventario.py
   ```

**Qué hace**  
- Al iniciar, intenta cargar `inventario.json`.  
  - Si no existe, lo crea vacío y te avisa.  
  - Si está corrupto, crea un respaldo `inventario.corrupto-AAAAMMDD-HHMMSS.json` y reinicia uno sano.  
- Todas las operaciones (agregar, actualizar, eliminar) guardan automáticamente y la interfaz notifica **éxito** o **fallo** explicando la causa (permisos, errores del sistema, etc.).  
- Escritura atómica (archivo temporal + reemplazo) para minimizar corrupción por cortes de energía/cierres abruptos.  
- Exporta a CSV desde el menú.

**Pruebas manuales sugeridas**
1. **Archivo inexistente**: borra `inventario.json` y ejecuta; debe crearlo.  
2. **Archivo corrupto**: abre `inventario.json` y borra algunas llaves o comas; al ejecutar, debe respaldarlo y crear uno nuevo.  
3. **Permisos**: en sistemas tipo Unix, cambia permisos a solo lectura y prueba agregar/actualizar (debe fallar con mensaje claro):  
   ```bash
   chmod -w inventario.json
   ```
   Luego restáuralos:  
   ```bash
   chmod +w inventario.json
   ```
4. **Datos inválidos**: intenta ingresar cantidades/precios negativos (la UI debe rechazarlos).  
5. **IDs duplicados**: intenta agregar dos productos con el mismo `id` (debe fallar).

**Estructura del JSON**
```json
[
  {"id": "A001", "nombre": "Teclado", "cantidad": 10, "precio": 19.99},
  {"id": "B002", "nombre": "Mouse", "cantidad": 5, "precio": 9.5}
]
```

¡Éxitos con tu entrega!
