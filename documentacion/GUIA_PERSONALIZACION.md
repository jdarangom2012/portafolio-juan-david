# 🎨 Guía de Personalización - Portafolio Juan David Arango

## 🖼️ **Cambiar tu Foto Personal**

### Opción 1: Foto Local
```html
<!-- En index.html, línea ~90 -->
<img src="mi-foto.jpg" alt="Juan David Arango" class="w-48 h-48 rounded-full mx-auto mb-6 border-4 border-ocean-light shadow-2xl animate-float">
```

### Opción 2: Foto Online
```html
<!-- Usar servicio como Imgur, Cloudinary, etc. -->
<img src="https://tu-servicio.com/tu-foto.jpg" alt="Juan David Arango">
```

### Recomendaciones para la Foto
- **Tamaño**: 400x400px mínimo
- **Formato**: JPG o PNG
- **Fondo**: Profesional o neutro
- **Calidad**: Alta resolución
- **Estilo**: Profesional, sonriente

## 🔗 **Actualizar Enlaces Personales**

### LinkedIn
```html
<!-- Línea ~180 y ~530 -->
<a href="https://linkedin.com/in/TU-PERFIL-LINKEDIN">
```

### GitHub
```html
<!-- Línea ~185 y ~535 -->
<a href="https://github.com/TU-USUARIO-GITHUB">
```

### Email y Teléfono
```html
<!-- Líneas ~175 y ~525 -->
<span>tu-email@gmail.com</span>
<span>tu-numero-telefono</span>
```

## 🎨 **Cambiar Colores del Tema**

### Paleta Actual (Oceánica)
```javascript
// En index.html, línea ~15
colors: {
    'ocean-deep': '#0f172a',
    'ocean-blue': '#1e40af',
    'ocean-cyan': '#0891b2',
    'ocean-teal': '#0d9488',
    'ocean-light': '#67e8f9',
    'ocean-foam': '#a7f3d0',
    'ocean-surface': '#e0f2fe'
}
```

### Alternativas de Color

#### Tema Bosque 🌲
```javascript
colors: {
    'forest-deep': '#1a2e05',
    'forest-green': '#22c55e',
    'forest-emerald': '#10b981',
    'forest-lime': '#84cc16',
    'forest-light': '#bbf7d0',
    'forest-mint': '#d1fae5',
    'forest-surface': '#f0fdf4'
}
```

#### Tema Atardecer 🌅
```javascript
colors: {
    'sunset-deep': '#451a03',
    'sunset-orange': '#ea580c',
    'sunset-amber': '#f59e0b',
    'sunset-yellow': '#eab308',
    'sunset-light': '#fef3c7',
    'sunset-cream': '#fffbeb',
    'sunset-surface': '#fefce8'
}
```

#### Tema Espacio 🌌
```javascript
colors: {
    'space-deep': '#0c0a09',
    'space-purple': '#7c3aed',
    'space-indigo': '#4f46e5',
    'space-blue': '#2563eb',
    'space-light': '#c7d2fe',
    'space-nebula': '#ddd6fe',
    'space-surface': '#f1f5f9'
}
```

## 📝 **Personalizar Contenido**

### Título y Descripción Principal
```html
<!-- Línea ~95 -->
<h1>TU NOMBRE COMPLETO</h1>
<h2>Tu Título Profesional | Tu Especialización</h2>
<p>Tu descripción personal y profesional aquí...</p>
```

### Sección "Sobre Mí"
```html
<!-- Línea ~150 -->
<p>Tu historia profesional personalizada...</p>
```

### Experiencia Laboral
```html
<!-- Línea ~220 -->
<h3>Tu Cargo Actual</h3>
<h4>Tu Empresa Actual</h4>
<span>Fechas de trabajo</span>
<!-- Agregar tus logros específicos -->
```

## 🚀 **Agregar Nuevos Proyectos**

### Estructura de Proyecto
```html
<div class="project-card glass-effect p-6 rounded-lg" data-aos="fade-up">
    <div class="mb-4">
        <i class="fas fa-TU-ICONO text-4xl text-ocean-light mb-4"></i>
        <h3 class="text-xl font-bold text-ocean-light mb-2">Nombre del Proyecto</h3>
        <p class="text-ocean-surface mb-4">
            Descripción detallada de tu proyecto...
        </p>
    </div>
    <div class="flex flex-wrap gap-2 mb-4">
        <span class="bg-ocean-teal px-3 py-1 rounded-full text-xs">Tecnología 1</span>
        <span class="bg-ocean-teal px-3 py-1 rounded-full text-xs">Tecnología 2</span>
    </div>
    <a href="https://github.com/tu-usuario/tu-proyecto" target="_blank" class="inline-flex items-center text-ocean-light hover:text-ocean-foam transition-colors">
        <i class="fab fa-github mr-2"></i>
        Ver en GitHub
    </a>
</div>
```

### Iconos Sugeridos (Font Awesome)
- `fa-code`: Desarrollo web
- `fa-mobile-alt`: Apps móviles
- `fa-database`: Bases de datos
- `fa-chart-line`: Analytics
- `fa-robot`: IA/ML
- `fa-cloud`: Cloud computing
- `fa-shield-alt`: Seguridad

## 📊 **Modificar Habilidades**

### Agregar Nueva Habilidad
```html
<div>
    <div class="flex justify-between mb-2">
        <span class="text-ocean-surface">Nueva Tecnología</span>
        <span class="text-ocean-light">85%</span>
    </div>
    <div class="w-full bg-ocean-deep rounded-full h-3">
        <div class="skill-bar bg-gradient-to-r from-ocean-light to-ocean-foam h-3 rounded-full" style="width: 85%"></div>
    </div>
</div>
```

### Habilidades Sugeridas
- **Frontend**: React, Vue, Angular
- **Backend**: Node.js, Django, Flask
- **Bases de datos**: MongoDB, MySQL, Redis
- **Cloud**: AWS, Azure, Google Cloud
- **DevOps**: Docker, Kubernetes, CI/CD
- **Mobile**: React Native, Flutter

## 🎓 **Agregar Certificaciones**

```html
<div class="glass-effect p-4 rounded-lg">
    <h4 class="font-semibold text-ocean-light">Nombre de la Certificación</h4>
    <p class="text-sm text-ocean-surface">Institución | Año</p>
</div>
```

## 📱 **Personalizar Información de Contacto**

### Agregar Nuevas Redes Sociales
```html
<a href="https://twitter.com/tu-usuario" target="_blank" class="bg-ocean-blue hover:bg-ocean-cyan p-3 rounded-full transition-colors">
    <i class="fab fa-twitter text-white text-xl"></i>
</a>
```

### Redes Disponibles
- Twitter: `fab fa-twitter`
- Instagram: `fab fa-instagram`
- YouTube: `fab fa-youtube`
- Medium: `fab fa-medium`
- Dev.to: `fab fa-dev`

## 🌐 **SEO y Metadatos**

### Título de la Página
```html
<title>Tu Nombre - Tu Profesión | Portafolio</title>
```

### Meta Description
```html
<meta name="description" content="Tu descripción profesional optimizada para SEO">
```

### Keywords
```html
<meta name="keywords" content="tus, tecnologías, principales, ubicación">
```

## 🎭 **Personalizar Animaciones**

### Cambiar Velocidad de Animaciones
```javascript
// En script.js
AOS.init({
    duration: 800,  // Más rápido (era 1000)
    easing: 'ease-in-out',
    once: true,
    offset: 50     // Activar antes (era 100)
});
```

### Desactivar Animaciones
```javascript
// Para mejor performance en dispositivos lentos
AOS.init({
    disable: 'mobile'  // Desactivar en móviles
});
```

## 🔧 **Configuraciones Avanzadas**

### Cambiar Fuente
```html
<!-- Reemplazar Google Fonts -->
<link href="https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;600;700&display=swap" rel="stylesheet">
```

```javascript
// En configuración Tailwind
fontFamily: {
    'sans': ['Roboto', 'system-ui', 'sans-serif']
}
```

### Agregar Google Analytics
```html
<!-- Antes de </head> -->
<script async src="https://www.googletagmanager.com/gtag/js?id=TU-ID"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'TU-ID');
</script>
```

## 📋 **Checklist de Personalización**

- [ ] Cambiar foto personal
- [ ] Actualizar información de contacto
- [ ] Verificar enlaces de redes sociales
- [ ] Personalizar descripción profesional
- [ ] Agregar proyectos reales
- [ ] Actualizar experiencia laboral
- [ ] Modificar habilidades técnicas
- [ ] Agregar certificaciones recientes
- [ ] Optimizar SEO
- [ ] Probar en diferentes dispositivos

---

¡Con esta guía podrás personalizar completamente tu portafolio! 🎨✨

