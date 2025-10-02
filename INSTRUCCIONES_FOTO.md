# 📸 Instrucciones para Agregar tu Foto

## 🎯 **Pasos para agregar tu foto profesional:**

### Opción 1: Guardar la foto localmente (Recomendado)

1. **Guarda tu foto** que me enviaste como:
   ```
   C:/Users/ASUS/portafolio-juan-david/images/juan-david-foto.jpg
   ```

2. **Cómo hacerlo:**
   - Haz clic derecho en tu foto
   - Selecciona "Guardar imagen como..."
   - Navega a: `C:/Users/ASUS/portafolio-juan-david/images/`
   - Nómbrala exactamente: `juan-david-foto.jpg`

3. **¡Listo!** Recarga tu página (F5) y verás tu foto

### Opción 2: Usar un servicio online

Si prefieres usar un servicio online:

1. **Sube tu foto a:**
   - [Imgur.com](https://imgur.com) (gratis)
   - [Cloudinary.com](https://cloudinary.com) (gratis)
   - Google Drive (público)

2. **Copia la URL directa** de la imagen

3. **Actualiza el HTML:**
   ```html
   <!-- En index.html, línea ~143 -->
   <img src="TU_URL_AQUI" alt="Juan David Arango" class="w-48 h-48 rounded-full mx-auto mb-6 border-4 border-ocean-light shadow-2xl animate-float object-cover">
   ```

## 🔧 **Si tienes problemas:**

### ❌ **No se ve la foto**
- Verifica que el archivo esté en: `images/juan-david-foto.jpg`
- Verifica que el nombre sea exacto (sin espacios, sin mayúsculas)
- Presiona F5 para recargar la página

### ❌ **La foto se ve distorsionada**
- La clase `object-cover` ya está agregada para que se vea bien
- Si quieres ajustar, puedes cambiar a `object-contain`

### ❌ **Quiero cambiar el tamaño**
```html
<!-- Cambiar w-48 h-48 por otros tamaños: -->
w-32 h-32  <!-- Más pequeña -->
w-56 h-56  <!-- Más grande -->
w-64 h-64  <!-- Aún más grande -->
```

## 📱 **Recomendaciones para la foto:**

- **Formato**: JPG o PNG
- **Tamaño**: 400x400px mínimo
- **Peso**: Menos de 500KB para carga rápida
- **Calidad**: Profesional, bien iluminada
- **Fondo**: Neutro o profesional

## ✅ **Verificación:**

Una vez que agregues la foto:
1. Ve a: http://localhost:8080
2. Deberías ver tu foto en lugar del placeholder
3. La foto debe verse redonda y bien centrada
4. Debe tener el borde azul oceánico

---

**¡Tu foto profesional hará que el portafolio se vea increíble!** 📸✨

