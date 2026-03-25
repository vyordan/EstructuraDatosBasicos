cmake_minimum_required(VERSION 3.12)
project(estructuras_datos)

# Requerir C++11 (mínimo necesario para pybind11)
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Encontrar Python
find_package(Python COMPONENTS Interpreter Development REQUIRED)

# Encontrar pybind11 (asume que está instalado en el sistema)
# Si no está instalado, se puede descargar automáticamente con FetchContent
find_package(pybind11 CONFIG REQUIRED)

# Crear el módulo de pybind11
pybind11_add_module(estructuras estructuras_datos.cpp)

# Establecer las propiedades de compilación (opcional, por si necesitas flags adicionales)
target_compile_options(estructuras PRIVATE -Wall -Wextra)

# Instalar el módulo (opcional)
install(TARGETS estructuras DESTINATION ${Python_SITELIB})