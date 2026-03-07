# setup.py
from setuptools import setup, Extension
import pybind11
import sys
import sysconfig
import platform

print("="*60)
print(" CONFIGURANDO COMPILACIÓN DE ESTRUCTURAS_DATOS.CPP")
print("="*60)

# Configuración según el sistema operativo
if platform.system() == "Windows":
    # Para Windows con MinGW
    extra_compile_args = ['-std=c++11', '-O3', '-Wall']
    extra_link_args = ['-shared']
    libraries = []
    
    print(f"Sistema: Windows")
    print(f"Compilador: MinGW (TDM-GCC)")
    
else:
    # Para Linux/Mac
    extra_compile_args = ['-std=c++11', '-O3', '-Wall', '-fPIC']
    extra_link_args = []
    libraries = ['python' + sys.version[:3]]
    print(f"Sistema: Linux/Mac")

# Obtener rutas de Python
python_include = sysconfig.get_path('include')
python_lib = sysconfig.get_config_var('LIBDIR')

print(f"Python include: {python_include}")
print(f"Python lib: {python_lib}")

# Obtener includes de pybind11
pybind11_includes = pybind11.get_include()
print(f"pybind11 include: {pybind11_includes}")

# Crear la extensión
ext_modules = [
    Extension(
        'estructuras',  # Nombre del módulo
        ['estructuras_datos.cpp'],  # Archivo fuente ACTUALIZADO
        include_dirs=[
            pybind11_includes,
            python_include
        ],
        library_dirs=[python_lib] if python_lib else [],
        libraries=libraries,
        language='c++',
        extra_compile_args=extra_compile_args,
        extra_link_args=extra_link_args,
    ),
]

# Configuración del setup
setup(
    name='estructuras_datos',
    version='1.0.0',
    author='Tu Nombre',
    description='Estructuras de datos en C++ con pybind11',
    ext_modules=ext_modules,
    zip_safe=False,
)

print("\n" + "="*60)
print(" CONFIGURACIÓN COMPLETADA")
print("="*60)
print("\nPara compilar, ejecuta uno de estos comandos:")
print("  python setup.py build_ext --inplace --compiler=mingw32    (Windows)")
print("  python setup.py build_ext --inplace                       (Linux/Mac)")
print("="*60)