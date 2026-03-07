// estructuras_datos.cpp
#include <iostream>
#include <string>
#include <stdexcept>

// ==================== STRUCT NODO BASE ====================
struct Nodo {
    int dato;
    Nodo* siguiente;
    
    Nodo(int valor) : dato(valor), siguiente(nullptr) {}
};

// ==================== STRUCT NODO PARA LISTA DOBLE ====================
struct NodoDoble {
    int dato;
    NodoDoble* siguiente;
    NodoDoble* anterior;
    
    NodoDoble(int valor) : dato(valor), siguiente(nullptr), anterior(nullptr) {}
};

// ==================== CLASE PILA (STACK) ====================
class Pila {
private:
    Nodo* cima;
    
public:
    Pila() : cima(nullptr) {}
    
    ~Pila() {
        while (!estaVacia()) {
            desapilar();
        }
    }
    
    void apilar(int valor) {
        Nodo* nuevo = new Nodo(valor);
        nuevo->siguiente = cima;
        cima = nuevo;
    }
    
    int desapilar() {
        if (estaVacia()) {
            throw std::runtime_error("La pila esta vacia");
        }
        Nodo* aux = cima;
        int valor = aux->dato;
        cima = cima->siguiente;
        delete aux;
        return valor;
    }
    
    int obtenerCima() {
        if (estaVacia()) {
            throw std::runtime_error("La pila esta vacia");
        }
        return cima->dato;
    }
    
    bool estaVacia() {
        return cima == nullptr;
    }
    
    std::string mostrar() {
        std::string resultado;
        Nodo* actual = cima;
        while (actual != nullptr) {
            resultado = std::to_string(actual->dato) + " " + resultado;
            actual = actual->siguiente;
        }
        return resultado;
    }
    
    int tamano() {
        int cont = 0;
        Nodo* actual = cima;
        while (actual != nullptr) {
            cont++;
            actual = actual->siguiente;
        }
        return cont;
    }
};

// ==================== CLASE COLA (QUEUE) ====================
class Cola {
private:
    Nodo* frente;
    Nodo* fin;
    
public:
    Cola() : frente(nullptr), fin(nullptr) {}
    
    ~Cola() {
        while (!estaVacia()) {
            desencolar();
        }
    }
    
    void encolar(int valor) {
        Nodo* nuevo = new Nodo(valor);
        nuevo->siguiente = nullptr;
        
        if (estaVacia()) {
            frente = nuevo;
        } else {
            fin->siguiente = nuevo;
        }
        fin = nuevo;
    }
    
    int desencolar() {
        if (estaVacia()) {
            throw std::runtime_error("La cola esta vacia");
        }
        Nodo* aux = frente;
        int valor = aux->dato;
        
        if (frente == fin) {
            frente = nullptr;
            fin = nullptr;
        } else {
            frente = frente->siguiente;
        }
        delete aux;
        return valor;
    }
    
    int obtenerFrente() {
        if (estaVacia()) {
            throw std::runtime_error("La cola esta vacia");
        }
        return frente->dato;
    }
    
    bool estaVacia() {
        return frente == nullptr;
    }
    
    std::string mostrar() {
        std::string resultado;
        Nodo* actual = frente;
        while (actual != nullptr) {
            resultado += std::to_string(actual->dato) + " ";
            actual = actual->siguiente;
        }
        return resultado;
    }
    
    int tamano() {
        int cont = 0;
        Nodo* actual = frente;
        while (actual != nullptr) {
            cont++;
            actual = actual->siguiente;
        }
        return cont;
    }
};

// ==================== CLASE LISTA SIMPLE ====================
class ListaSimple {
private:
    Nodo* cabeza;
    
public:
    ListaSimple() : cabeza(nullptr) {}
    
    ~ListaSimple() {
        while (cabeza != nullptr) {
            Nodo* temp = cabeza;
            cabeza = cabeza->siguiente;
            delete temp;
        }
    }
    
    void insertarInicio(int valor) {
        Nodo* nuevo = new Nodo(valor);
        nuevo->siguiente = cabeza;
        cabeza = nuevo;
    }
    
    void insertarFinal(int valor) {
        Nodo* nuevo = new Nodo(valor);
        nuevo->siguiente = nullptr;
        
        if (cabeza == nullptr) {
            cabeza = nuevo;
        } else {
            Nodo* actual = cabeza;
            while (actual->siguiente != nullptr) {
                actual = actual->siguiente;
            }
            actual->siguiente = nuevo;
        }
    }
    
    void insertarEnPosicion(int valor, int posicion) {
        if (posicion < 0) {
            throw std::runtime_error("Posicion no valida");
        }
        
        if (posicion == 0) {
            insertarInicio(valor);
            return;
        }
        
        Nodo* nuevo = new Nodo(valor);
        Nodo* actual = cabeza;
        int cont = 0;
        
        while (actual != nullptr && cont < posicion - 1) {
            actual = actual->siguiente;
            cont++;
        }
        
        if (actual == nullptr) {
            delete nuevo;
            throw std::runtime_error("Posicion fuera de rango");
        }
        
        nuevo->siguiente = actual->siguiente;
        actual->siguiente = nuevo;
    }
    
    bool eliminar(int valor) {
        if (cabeza == nullptr) return false;
        
        if (cabeza->dato == valor) {
            Nodo* temp = cabeza;
            cabeza = cabeza->siguiente;
            delete temp;
            return true;
        }
        
        Nodo* actual = cabeza;
        while (actual->siguiente != nullptr && actual->siguiente->dato != valor) {
            actual = actual->siguiente;
        }
        
        if (actual->siguiente == nullptr) return false;
        
        Nodo* temp = actual->siguiente;
        actual->siguiente = temp->siguiente;
        delete temp;
        return true;
    }
    
    bool buscar(int valor) {
        Nodo* actual = cabeza;
        while (actual != nullptr) {
            if (actual->dato == valor) return true;
            actual = actual->siguiente;
        }
        return false;
    }
    
    std::string mostrar() {
        std::string resultado;
        Nodo* actual = cabeza;
        while (actual != nullptr) {
            resultado += std::to_string(actual->dato) + " ";
            actual = actual->siguiente;
        }
        return resultado;
    }
    
    int obtener(int posicion) {
        if (posicion < 0) {
            throw std::runtime_error("Posicion no valida");
        }
        
        Nodo* actual = cabeza;
        int cont = 0;
        
        while (actual != nullptr && cont < posicion) {
            actual = actual->siguiente;
            cont++;
        }
        
        if (actual == nullptr) {
            throw std::runtime_error("Posicion fuera de rango");
        }
        
        return actual->dato;
    }
    
    int tamano() {
        int cont = 0;
        Nodo* actual = cabeza;
        while (actual != nullptr) {
            cont++;
            actual = actual->siguiente;
        }
        return cont;
    }
};

// ==================== CLASE LISTA DOBLE ====================
class ListaDoble {
private:
    NodoDoble* cabeza;
    NodoDoble* cola;
    
public:
    ListaDoble() : cabeza(nullptr), cola(nullptr) {}
    
    ~ListaDoble() {
        while (cabeza != nullptr) {
            NodoDoble* temp = cabeza;
            cabeza = cabeza->siguiente;
            delete temp;
        }
    }
    
    void insertarInicio(int valor) {
        NodoDoble* nuevo = new NodoDoble(valor);
        
        if (cabeza == nullptr) {
            cabeza = nuevo;
            cola = nuevo;
        } else {
            nuevo->siguiente = cabeza;
            cabeza->anterior = nuevo;
            cabeza = nuevo;
        }
    }
    
    void insertarFinal(int valor) {
        NodoDoble* nuevo = new NodoDoble(valor);
        
        if (cabeza == nullptr) {
            cabeza = nuevo;
            cola = nuevo;
        } else {
            nuevo->anterior = cola;
            cola->siguiente = nuevo;
            cola = nuevo;
        }
    }
    
    void insertarEnPosicion(int valor, int posicion) {
        if (posicion < 0) {
            throw std::runtime_error("Posicion no valida");
        }
        
        if (posicion == 0) {
            insertarInicio(valor);
            return;
        }
        
        NodoDoble* actual = cabeza;
        int cont = 0;
        
        while (actual != nullptr && cont < posicion) {
            actual = actual->siguiente;
            cont++;
        }
        
        if (actual == nullptr) {
            if (cont == posicion) {
                insertarFinal(valor);
                return;
            }
            throw std::runtime_error("Posicion fuera de rango");
        }
        
        NodoDoble* nuevo = new NodoDoble(valor);
        nuevo->siguiente = actual;
        nuevo->anterior = actual->anterior;
        
        if (actual->anterior != nullptr) {
            actual->anterior->siguiente = nuevo;
        }
        actual->anterior = nuevo;
    }
    
    bool eliminar(int valor) {
        NodoDoble* actual = cabeza;
        
        while (actual != nullptr) {
            if (actual->dato == valor) {
                if (actual->anterior != nullptr) {
                    actual->anterior->siguiente = actual->siguiente;
                } else {
                    cabeza = actual->siguiente;
                }
                
                if (actual->siguiente != nullptr) {
                    actual->siguiente->anterior = actual->anterior;
                } else {
                    cola = actual->anterior;
                }
                
                delete actual;
                return true;
            }
            actual = actual->siguiente;
        }
        return false;
    }
    
    bool buscar(int valor) {
        NodoDoble* actual = cabeza;
        while (actual != nullptr) {
            if (actual->dato == valor) return true;
            actual = actual->siguiente;
        }
        return false;
    }
    
    std::string mostrarAdelante() {
        std::string resultado;
        NodoDoble* actual = cabeza;
        while (actual != nullptr) {
            resultado += std::to_string(actual->dato) + " ";
            actual = actual->siguiente;
        }
        return resultado;
    }
    
    std::string mostrarAtras() {
        std::string resultado;
        NodoDoble* actual = cola;
        while (actual != nullptr) {
            resultado += std::to_string(actual->dato) + " ";
            actual = actual->anterior;
        }
        return resultado;
    }
    
    int obtener(int posicion) {
        if (posicion < 0) {
            throw std::runtime_error("Posicion no valida");
        }
        
        NodoDoble* actual = cabeza;
        int cont = 0;
        
        while (actual != nullptr && cont < posicion) {
            actual = actual->siguiente;
            cont++;
        }
        
        if (actual == nullptr) {
            throw std::runtime_error("Posicion fuera de rango");
        }
        
        return actual->dato;
    }
    
    int tamano() {
        int cont = 0;
        NodoDoble* actual = cabeza;
        while (actual != nullptr) {
            cont++;
            actual = actual->siguiente;
        }
        return cont;
    }
};

// ==================== WRAPPERS PARA PYBIND11 ====================
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <pybind11/functional.h>

namespace py = pybind11;

PYBIND11_MODULE(estructuras, m) {
    m.doc() = "Estructuras de datos en C++ para usar con Python";
    
    // Clase Pila
    py::class_<Pila>(m, "Pila")
        .def(py::init<>())
        .def("apilar", &Pila::apilar)
        .def("desapilar", &Pila::desapilar)
        .def("obtener_cima", &Pila::obtenerCima)
        .def("esta_vacia", &Pila::estaVacia)
        .def("mostrar", &Pila::mostrar)
        .def("tamano", &Pila::tamano);
    
    // Clase Cola
    py::class_<Cola>(m, "Cola")
        .def(py::init<>())
        .def("encolar", &Cola::encolar)
        .def("desencolar", &Cola::desencolar)
        .def("obtener_frente", &Cola::obtenerFrente)
        .def("esta_vacia", &Cola::estaVacia)
        .def("mostrar", &Cola::mostrar)
        .def("tamano", &Cola::tamano);
    
    // Clase ListaSimple
    py::class_<ListaSimple>(m, "ListaSimple")
        .def(py::init<>())
        .def("insertar_inicio", &ListaSimple::insertarInicio)
        .def("insertar_final", &ListaSimple::insertarFinal)
        .def("insertar_en_posicion", &ListaSimple::insertarEnPosicion)
        .def("eliminar", &ListaSimple::eliminar)
        .def("buscar", &ListaSimple::buscar)
        .def("mostrar", &ListaSimple::mostrar)
        .def("obtener", &ListaSimple::obtener)
        .def("tamano", &ListaSimple::tamano);
    
    // Clase ListaDoble
    py::class_<ListaDoble>(m, "ListaDoble")
        .def(py::init<>())
        .def("insertar_inicio", &ListaDoble::insertarInicio)
        .def("insertar_final", &ListaDoble::insertarFinal)
        .def("insertar_en_posicion", &ListaDoble::insertarEnPosicion)
        .def("eliminar", &ListaDoble::eliminar)
        .def("buscar", &ListaDoble::buscar)
        .def("mostrar_adelante", &ListaDoble::mostrarAdelante)
        .def("mostrar_atras", &ListaDoble::mostrarAtras)
        .def("obtener", &ListaDoble::obtener)
        .def("tamano", &ListaDoble::tamano);
}