#!/usr/bin/env python3
"""
Servidor local simple para el portafolio de Juan David Arango Morales
Sin Docker - Solo Python puro
"""

import http.server
import socketserver
import webbrowser
import os
import sys
from pathlib import Path

# Configuración
PORT = 8080
HOST = 'localhost'

class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    """Handler personalizado para servir archivos estáticos"""
    
    def end_headers(self):
        # Agregar headers CORS para desarrollo
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()
    
    def do_GET(self):
        # Servir index.html para rutas que no existen (SPA behavior)
        if self.path == '/' or not os.path.exists(self.path[1:]):
            self.path = '/index.html'
        return super().do_GET()
    
    def log_message(self, format, *args):
        # Log personalizado más limpio
        print(f"[{self.log_date_time_string()}] {format % args}")

def main():
    """Función principal para iniciar el servidor"""
    
    # Verificar que estamos en el directorio correcto
    if not os.path.exists('index.html'):
        print("❌ Error: No se encontró index.html")
        print("   Asegúrate de ejecutar este script desde la carpeta del portafolio")
        sys.exit(1)
    
    # Cambiar al directorio del script
    os.chdir(Path(__file__).parent)
    
    try:
        # Crear el servidor
        with socketserver.TCPServer((HOST, PORT), CustomHTTPRequestHandler) as httpd:
            print("🌊 Portafolio de Juan David Arango Morales")
            print("=" * 50)
            print(f"🚀 Servidor iniciado en: http://{HOST}:{PORT}")
            print(f"📁 Sirviendo archivos desde: {os.getcwd()}")
            print("=" * 50)
            print("💡 Presiona Ctrl+C para detener el servidor")
            print()
            
            # Abrir automáticamente en el navegador
            try:
                webbrowser.open(f'http://{HOST}:{PORT}')
                print("🌐 Abriendo navegador automáticamente...")
            except Exception as e:
                print(f"⚠️  No se pudo abrir el navegador automáticamente: {e}")
                print(f"   Abre manualmente: http://{HOST}:{PORT}")
            
            print()
            print("📊 Logs del servidor:")
            print("-" * 30)
            
            # Iniciar el servidor
            httpd.serve_forever()
            
    except KeyboardInterrupt:
        print("\n")
        print("🛑 Servidor detenido por el usuario")
        print("👋 ¡Gracias por usar el portafolio!")
        
    except OSError as e:
        if e.errno == 48:  # Address already in use
            print(f"❌ Error: El puerto {PORT} ya está en uso")
            print("   Intenta con otro puerto o cierra la aplicación que lo está usando")
        else:
            print(f"❌ Error del sistema: {e}")
        sys.exit(1)
        
    except Exception as e:
        print(f"❌ Error inesperado: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()

