"""
================================================================
 LIVE CODING · Sesiones 3 y 4
 "Una CuentaBancaria que aplique TODO lo aprendido."
================================================================

EL PROBLEMA
-----------
El banco necesita modelar una CuentaBancaria. Aplica reglas estrictas:

  - titular           → público, todos pueden leerlo.
  - numero_cuenta     → protegido, no lo enseñes alegremente.
  - __saldo           → privado, NADIE lo toca por fuera.
  - __nip             → privado, 4 dígitos, secreto.

REGLAS DE NEGOCIO
-----------------
  1. El saldo nunca puede ser negativo.
  2. El NIP debe ser un string de exactamente 4 dígitos.
  3. depositar(monto)         → suma al saldo, rechaza montos <= 0.
  4. retirar(monto, nip)      → valida nip, valida saldo, retira.
  5. consultar_saldo(nip)     → devuelve saldo SOLO si el nip es correcto.
  6. str(cuenta)              → "Cuenta de Daniel · ****7890"
                                (últimos 4 dígitos del número de cuenta).
  7. Dos cuentas son iguales  → si tienen el mismo numero_cuenta.

================================================================
 LA RUTA DEL LIVE CODING (vamos paso por paso)
================================================================

PASO 1 · Esqueleto
    Crea la clase con `__init__`. Recibe titular, numero_cuenta, nip,
    saldo_inicial=0. Solo guarda los atributos. Sin validar nada todavía.
    👉 Concepto: class, __init__, self, atributos.   (Sesión 3 · II–IV)

PASO 2 · Encapsulamiento
    Renombra los atributos:
        titular         → público
        numero_cuenta   → _numero_cuenta (protegido)
        saldo           → __saldo        (privado)
        nip             → __nip          (privado)
    Demuestra name mangling: `cuenta._CuentaBancaria__saldo` funciona,
    `cuenta.__saldo` truena.
    👉 Concepto: público / _protegido / __privado.   (Sesión 4 · II)

PASO 3 · Validación en el constructor
    Mueve las reglas de validación dentro del __init__:
        - saldo_inicial >= 0
        - nip es string de 4 dígitos (usa .isdigit() y len())
    Si algo falla, levanta ValueError.
    👉 Concepto: validar antes de asignar.            (Sesión 3 · VI)

PASO 4 · depositar(monto)
    if monto <= 0: raise ValueError
    self.__saldo += monto
    👉 Concepto: método con validación de entrada.

PASO 5 · _validar_nip(nip) (método privado de apoyo)
    Devuelve True si nip == self.__nip, False si no.
    Este método ayuda a no repetir la verificación en cada operación.
    👉 Concepto: método helper privado.

PASO 6 · retirar(monto, nip)
    Si el nip no coincide → raise PermissionError.
    Si monto <= 0          → raise ValueError.
    Si monto > __saldo     → raise ValueError("Saldo insuficiente").
    Si pasa todo           → self.__saldo -= monto.
    👉 Concepto: el método como guardia (Sesión 3 · VI).

PASO 7 · consultar_saldo(nip)
    Si nip incorrecto → raise PermissionError.
    Si correcto       → devuelve self.__saldo.
    👉 Concepto: getter con validación.

PASO 8 · __str__
    Devuelve f"Cuenta de {self.titular} · ****{self._numero_cuenta[-4:]}"
    👉 Concepto: representación humana.               (Sesión 3 · VII)

PASO 9 · __eq__ y __hash__
    Dos cuentas son iguales si tienen el mismo numero_cuenta.
    Recuerda: si defines __eq__, DEBES definir __hash__.
    👉 Concepto: identidad vs igualdad.               (Sesión 3 · VII)

PASO 10 · Mover a paquetes (cuando ya funcione todo)
    Crea esta estructura y mueve el código:
        banco/
            main.py
            modelos/
                __init__.py
                cuenta.py
            utilidades/
                __init__.py
                validador.py
    En main.py protege el demo con `if __name__ == "__main__":`.
    👉 Concepto: módulos, paquetes, __main__.         (Sesión 4 · IV, V)

================================================================
 ZONA DE LIVE CODING — empieza aquí, borra los TODO al avanzar
================================================================
"""


class CuentaBancaria:
    """TODO Paso 1 → 9: construir aquí, paso a paso, frente a la clase."""

    def __init__(self, titular, numero_cuenta, nip, saldo_inicial=0):
        # TODO Paso 1: guarda los atributos tal cual los recibes.
        # TODO Paso 2: renómbralos a _protegido / __privado.
        # TODO Paso 3: agrega validaciones.
        pass

    # TODO Paso 4: def depositar(self, monto): ...
    # TODO Paso 5: def _validar_nip(self, nip): ...
    # TODO Paso 6: def retirar(self, monto, nip): ...
    # TODO Paso 7: def consultar_saldo(self, nip): ...
    # TODO Paso 8: def __str__(self): ...
    # TODO Paso 9: def __eq__(self, otra): ...
    # TODO Paso 9: def __hash__(self): ...


# ================================================================
#  DEMOSTRACIÓN — ESTO ES LO QUE DEBE FUNCIONAR AL FINAL
# ================================================================
#  Descomenta los bloques conforme avancen los pasos.

if __name__ == "__main__":
    print("=" * 50)
    print(" Demo · Banco")
    print("=" * 50)

    # ---- Paso 1-3 ----
    # cuenta = CuentaBancaria("Daniel", "1234567890", "4242", saldo_inicial=1000)
    # print(cuenta.titular)             # "Daniel"
    # print(cuenta._numero_cuenta)      # "1234567890"  (funciona, pero ⚠)
    # # print(cuenta.__saldo)           # AttributeError (name mangling)
    # print(cuenta._CuentaBancaria__saldo)  # 1000 (saltando el guardia)

    # ---- Paso 4 ----
    # cuenta.depositar(500)
    # print(cuenta._CuentaBancaria__saldo)  # 1500

    # ---- Paso 6 y 7 ----
    # cuenta.retirar(200, "4242")
    # print(cuenta.consultar_saldo("4242"))  # 1300
    # try:
    #     cuenta.retirar(50, "0000")
    # except PermissionError as e:
    #     print("Bloqueado:", e)

    # ---- Paso 8 ----
    # print(cuenta)  # "Cuenta de Daniel · ****7890"

    # ---- Paso 9 ----
    # cuenta_gemela = CuentaBancaria("Otro Dueño", "1234567890", "9999")
    # print(cuenta == cuenta_gemela)        # True (mismo número)
    # print(hash(cuenta) == hash(cuenta_gemela))  # True

    pass
