#!/usr/bin/env python
# compilar.py
"""
Script para compilar automáticamente estructuras_datos.cpp con pybind11
Ejecutar: python compilar.py
"""

import subprocess
import sys
import os
import platform
import time

def print_header(text):
    """Imprimir un encabezado formateado"""
    print("\n" + "="*70)
    print(f" {text}")
    print("="*70)

def check_dependencies():
    """Verificar que todas las dependencias están instaladas"""
    print_header("VERIFICANDO DEPENDENCIAS")
    
    # Verificar pybind11
    try:
        import pybind11
        print(f"✅ pybind11 {pybind11.__version__} encontrado")
    except ImportError:
        print("❌ pybind11 no está instalado. Instalando...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pybind11"])
        import pybind11
        print("✅ pybind11 instalado correctamente")
    
    # Verificar setuptools
    try:
        import setuptools
        print(f"✅ setuptools {setuptools.__version__} encontrado")
    except ImportError:
        print("❌ setuptools no está instalado. Instalando...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "setuptools"])
        print("✅ setuptools instalado correctamente")

def check_files():
    """Verificar que los archivos necesarios existen"""
    print_header("VERIFICANDO ARCHIVOS")
    
    required_files = ['estructuras_datos.cpp', 'setup.py']
    missing = []
    
    for file in required_files:
        if os.path.exists(file):
            size = os.path.getsize(file)
            print(f"✅ {file} encontrado ({size} bytes)")
        else:
            print(f"❌ {file} NO encontrado")
            missing.append(file)
    
    if missing:
        print(f"\n❌ Archivos faltantes: {', '.join(missing)}")
        return False
    
    return True

def compile_windows():
    """Compilar en Windows usando MinGW"""
    print_header("COMPILANDO PARA WINDOWS")
    
    # Verificar que MinGW está disponible
    try:
        result = subprocess.run(['g++', '--version'], capture_output=True, text=True, check=True)
        print(f"✅ MinGW encontrado:")
        print(f"   {result.stdout.splitlines()[0]}")
    except:
        print("❌ MinGW no encontrado")
        print("\n   Asegúrate de que TDM-GCC esté instalado y en el PATH")
        print("   Puedes descargarlo de: https://jmeubank.github.io/tdm-gcc/")
        return False
    
    # Verificar que el archivo fuente existe
    if not os.path.exists('estructuras_datos.cpp'):
        print("❌ No se encuentra estructuras_datos.cpp")
        return False
    
    # Ejecutar la compilación
    cmd = [sys.executable, 'setup.py', 'build_ext', '--inplace', '--compiler=mingw32']
    
    print(f"\n🔧 Ejecutando: {' '.join(cmd)}")
    print("-"*70)
    
    try:
        # Mostrar output en tiempo real
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, 
                                  text=True, bufsize=1)
        
        for line in process.stdout:
            print(line, end='')
        
        process.wait()
        
        if process.returncode == 0:
            print("-"*70)
            print("✅ ¡COMPILACIÓN EXITOSA!")
            return True
        else:
            print("-"*70)
            print("❌ Error en la compilación")
            return False
            
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def compile_linux():
    """Compilar en Linux"""
    print_header("COMPILANDO PARA LINUX")
    
    cmd = [sys.executable, 'setup.py', 'build_ext', '--inplace']
    
    print(f"🔧 Ejecutando: {' '.join(cmd)}")
    print("-"*70)
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode == 0:
            print(result.stdout)
            print("-"*70)
            print("✅ ¡COMPILACIÓN EXITOSA!")
            return True
        else:
            print("❌ Error en la compilación:")
            print(result.stderr)
            return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def find_module_file():
    """Buscar el archivo del módulo compilado"""
    possible_files = [
        'estructuras.pyd',
        'estructuras.so',
        'estructuras.dll',
        'estructuras.cp*-win*.pyd',
        'estructuras.*.so',
        'build/lib.*/estructuras*.pyd',
        'build/lib.*/estructuras*.so'
    ]
    
    import glob
    for pattern in possible_files:
        files = glob.glob(pattern)
        if files:
            return files[0]
    return None

def test_module():
    """Probar que el módulo se puede importar"""
    print_header("PROBANDO EL MÓDULO")
    
    module_file = find_module_file()
    
    if not module_file:
        print("❌ No se encontró el módulo compilado")
        print("   Buscando en el directorio actual...")
        print("\n   Archivos en directorio:")
        for f in os.listdir('.'):
            if 'estructuras' in f:
                print(f"   - {f}")
        return False
    
    print(f"✅ Módulo encontrado: {module_file}")
    
    try:
        # Intentar importar el módulo
        import importlib.util
        import os
        
        # Asegurar que el directorio actual está en sys.path
        sys.path.insert(0, os.getcwd())
        
        # Intentar importar
        import estructuras
        print("✅ Módulo importado correctamente")
        
        # Probar las clases
        print("\n📋 Clases disponibles:")
        
        # Verificar cada clase
        clases = ['Pila', 'Cola', 'ListaSimple', 'ListaDoble']
        for clase in clases:
            if hasattr(estructuras, clase):
                print(f"   ✅ {clase}")
            else:
                print(f"   ❌ {clase}")
        
        # Crear instancias para probar
        print("\n🧪 Probando funcionalidad básica...")
        
        pila = estructuras.Pila()
        pila.apilar(10)
        pila.apilar(20)
        print(f"   Pila: {pila.mostrar()}")
        
        cola = estructuras.Cola()
        cola.encolar(10)
        cola.encolar(20)
        print(f"   Cola: {cola.mostrar()}")
        
        lista = estructuras.ListaSimple()
        lista.insertar_final(10)
        lista.insertar_final(20)
        print(f"   ListaSimple: {lista.mostrar()}")
        
        lista2 = estructuras.ListaDoble()
        lista2.insertar_final(10)
        lista2.insertar_final(20)
        print(f"   ListaDoble: {lista2.mostrar_adelante()}")
        
        print("\n✅ TODAS LAS PRUEBAS PASARON EXITOSAMENTE")
        return True
        
    except ImportError as e:
        print(f"❌ Error al importar: {e}")
        print("\n   Verifica que el módulo esté en el directorio correcto")
        return False
    except Exception as e:
        print(f"❌ Error durante las pruebas: {e}")
        return False

def main():
    print_header("COMPILADOR DE ESTRUCTURAS_DATOS.CPP CON PYBIND11")
    
    # Información del sistema
    system = platform.system()
    python_version = f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"
    print(f"Sistema: {system}")
    print(f"Python: {python_version}")
    print(f"Directorio: {os.getcwd()}")
    
    # Verificar dependencias
    check_dependencies()
    
    # Verificar archivos
    if not check_files():
        print("\n❌ No se puede continuar. Archivos faltantes.")
        print("\n   Asegúrate de tener:")
        print("   - estructuras_datos.cpp (código fuente C++)")
        print("   - setup.py (configuración de compilación)")
        return
    
    # Compilar según el sistema
    success = False
    start_time = time.time()
    
    if system == "Windows":
        success = compile_windows()
    elif system == "Linux":
        success = compile_linux()
    else:
        print(f"❌ Sistema no soportado: {system}")
        return
    
    elapsed_time = time.time() - start_time
    
    if success:
        print_header("COMPILACIÓN COMPLETADA")
        print(f"⏱️  Tiempo: {elapsed_time:.2f} segundos")
        
        # Probar el módulo
        test_module()
        
        print_header("INSTRUCCIONES DE USO")
        print("\n📦 Módulo generado exitosamente!")
        print("\nPara usar en tu código Python:")
        print("\n   from estructuras import Pila, Cola, ListaSimple, ListaDoble")
        print("   ")
        print("   # Crear una pila")
        print("   pila = Pila()")
        print("   pila.apilar(10)")
        print("   pila.apilar(20)")
        print("   print(pila.mostrar())  # 10 20")
        print("   ")
        print("   # Crear una cola")
        print("   cola = Cola()")
        print("   cola.encolar(5)")
        print("   cola.encolar(15)")
        print("   print(cola.mostrar())  # 5 15")
        print("   ")
        print("   # Crear una lista")
        print("   lista = ListaSimple()")
        print("   lista.insertar_final(100)")
        print("   print(lista.mostrar())  # 100")
        
        print("\n" + "="*70)
        print(" ¡LISTO PARA USAR!")
        print("="*70)
        
    else:
        print_header("ERROR DE COMPILACIÓN")
        print("\n❌ La compilación falló. Posibles soluciones:")
        print("   1. Verifica que TDM-GCC esté instalado correctamente")
        print("   2. Asegúrate de que pybind11 esté instalado: pip install pybind11")
        print("   3. Verifica que estructuras_datos.cpp no tenga errores")
        print("   4. Intenta compilar manualmente:")
        print("      python setup.py build_ext --inplace --compiler=mingw32")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n❌ Compilación interrumpida por el usuario")
    except Exception as e:
        print(f"\n❌ Error inesperado: {e}")
    
    input("\nPresiona Enter para salir...")