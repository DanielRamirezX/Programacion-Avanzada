"""
================================================================
 LABORATORIO · Sesiones 3 y 4
 "Una clase es bonita. Un proyecto está ORDENADO."
================================================================

Este archivo FUNCIONA. Si lo corres con `python codigo_monolitico.py`
obtienes una salida válida. Pero está MAL organizado:
    - dos clases viviendo en el mismo archivo
    - funciones sueltas mezcladas con clases
    - el demo de uso pegado al final, sin proteccion __main__
    - imposible de reutilizar desde otro programa

----------------------------------------------------------------
 TU MISIÓN
----------------------------------------------------------------
Refactoriza este archivo a la siguiente estructura de carpetas
y archivos. Crea una carpeta hermana llamada `proyecto_refactor/`:

    proyecto_refactor/
        main.py
        modelos/
            __init__.py
            estudiante.py
            materia.py
        utilidades/
            __init__.py
            validador.py

----------------------------------------------------------------
 REGLAS DEL JUEGO
----------------------------------------------------------------
 1. UNA clase por archivo. Estudiante en su archivo, Materia en el suyo.
 2. Las funciones de validación van en `utilidades/validador.py`.
 3. `main.py` SOLO debe ejecutar el demo cuando lo corres directo,
    nunca cuando lo importa otro módulo. Usa `if __name__ == "__main__":`.
 4. Cada paquete necesita su `__init__.py` (puede estar vacío).
 5. Usa imports relativos o absolutos coherentes:
        from modelos.estudiante import Estudiante
        from utilidades.validador import validar_email
 6. NO cambies el comportamiento. Tras refactorizar:
        python main.py
    debe imprimir lo MISMO que imprime hoy este archivo.

----------------------------------------------------------------
 CONCEPTOS QUE DEBES RECONOCER (y proteger al mover)
----------------------------------------------------------------
   [x] class, __init__, self                       (Sesión 3 · II, III)
   [x] atributos públicos, _protegidos, __privados (Sesión 4 · II)
   [x] getters & setters con validación            (Sesión 3 · VI)
   [x] __str__, __eq__, __hash__                   (Sesión 3 · VII)
   [x] f-strings                                   (Sesión 3 · II)
   [x] if __name__ == "__main__"                   (Sesión 4 · V)
   [x] paquetes con __init__.py                    (Sesión 4 · IV)

================================================================
"""

# ----------------------------------------------------------------
# Validadores (deberían vivir en utilidades/validador.py)
# ----------------------------------------------------------------

def validar_email(email):
    if "@" not in email or "." not in email:
        raise ValueError(f"Email inválido: {email}")
    return email


def validar_edad(edad):
    if not isinstance(edad, int):
        raise ValueError("La edad debe ser un entero")
    if edad < 0 or edad > 120:
        raise ValueError(f"Edad fuera de rango: {edad}")
    return edad


def validar_clave_materia(clave):
    if not isinstance(clave, str) or len(clave) < 3:
        raise ValueError(f"Clave de materia inválida: {clave}")
    return clave.upper()


# ----------------------------------------------------------------
# Clase Materia (debería vivir en modelos/materia.py)
# ----------------------------------------------------------------

class Materia:
    """Una materia del plan de estudios."""

    def __init__(self, clave, nombre, creditos):
        self.clave = validar_clave_materia(clave)
        self.nombre = nombre
        self._creditos = creditos          # protegido por convención
        self.__codigo_interno = id(self)   # privado: name mangling

    def get_creditos(self):
        return self._creditos

    def set_creditos(self, valor):
        if valor < 1 or valor > 12:
            raise ValueError("Créditos fuera de rango (1-12)")
        self._creditos = valor

    def __str__(self):
        return f"{self.clave} · {self.nombre} ({self._creditos} créditos)"

    def __eq__(self, otra):
        if not isinstance(otra, Materia):
            return False
        return self.clave == otra.clave

    def __hash__(self):
        return hash(self.clave)


# ----------------------------------------------------------------
# Clase Estudiante (debería vivir en modelos/estudiante.py)
# ----------------------------------------------------------------

class Estudiante:
    """Representa a un alumno inscrito en el curso."""

    def __init__(self, nombre, edad, email):
        self.nombre = nombre                  # público
        self._edad = validar_edad(edad)       # protegido
        self.__email = validar_email(email)   # privado
        self.materias = []                    # lista, arranca vacía

    # ---- getters / setters ----
    def get_edad(self):
        return self._edad

    def set_edad(self, valor):
        self._edad = validar_edad(valor)

    def get_email(self):
        return self.__email

    def set_email(self, valor):
        self.__email = validar_email(valor)

    # ---- comportamiento propio ----
    def saludar(self):
        return f"Hola, soy {self.nombre} y tengo {self._edad} años."

    def inscribir(self, materia):
        if not isinstance(materia, Materia):
            raise ValueError("Solo se inscriben objetos Materia")
        if materia in self.materias:
            return False
        self.materias.append(materia)
        return True

    # ---- dunders ----
    def __str__(self):
        return f"Estudiante({self.nombre}, {self._edad}, materias={len(self.materias)})"

    def __eq__(self, otro):
        if not isinstance(otro, Estudiante):
            return False
        return self.__email == otro.get_email()

    def __hash__(self):
        return hash(self.__email)


# ----------------------------------------------------------------
# Demo de uso (debería vivir en main.py, bajo __name__ == "__main__")
# ----------------------------------------------------------------

print("=" * 50)
print(" Demo · Sistema de inscripciones")
print("=" * 50)

ana = Estudiante("Ana", 20, "ana@unitec.mx")
luis = Estudiante("Luis", 22, "luis@unitec.mx")

mct158 = Materia("mct158", "Programación Avanzada", 8)
mct200 = Materia("mct200", "Bases de Datos", 6)

ana.inscribir(mct158)
ana.inscribir(mct200)
luis.inscribir(mct158)

print(ana.saludar())
print(luis.saludar())
print()
print("Inscripciones de Ana:")
for m in ana.materias:
    print(f"   - {m}")

print()
print("¿Ana y Luis son la misma persona?", ana == luis)

# Probemos name mangling — esto debería FALLAR si descomentas:
# print(ana.__email)
# Pero esto funciona (lo que demuestra que "privado" en Python es por convención):
print("Email (saltando el guardia):", ana._Estudiante__email)
