import os
import sys


def MostrarPCB(Pid: int, Etiqueta: str) -> int:


    Campos: list[str] = [
        "Name",
        "State",
        "Pid",
        "PPid",
        "VmSize",
        "VmRSS",
        "voluntary_ctxt_switches",
    ]


    print(f"\n  ┌─ PCB de {Etiqueta} {'─' * (38 - len(Etiqueta))}")


    for Campo in Campos:
        try:
            with open(f"/proc/{Pid}/status") as F:
                for Linea in F:
                    if Linea.startswith(Campo + ":"):
                        # Solo mostramos el valor real — sin descripcion adicional
                        print(f"  │  {Linea.strip()}")
                        break
        except FileNotFoundError:
            print(f"  │  [{Campo}] — proceso {Pid} ya no existe en /proc")


    print(f"  └{'─' * 56}")
    return 0


def Main() -> int:


    print("=" * 60)
    print("  EJERCICIO 1 — Inspeccion del PCB: padre e hijo")
    print("=" * 60)
    print(f"\n  [PADRE] PID: {os.getpid()}")
    print(f"  [PADRE] Mostrando PCB antes del fork...")
    MostrarPCB(os.getpid(), f"PADRE antes del fork  (PID {os.getpid()})")


    print(f"\n  Ejecutando fork()...")
    Pid: int = os.fork()


    if Pid == 0:
        
        print(f"\n  [HIJO]  fork() retorno 0  →  soy el hijo")
        print(f"  [HIJO]  PID  : {os.getpid()}")
        print(f"  [HIJO]  PPID : {os.getppid()}  (apunta al padre)")
        print(f"  [HIJO]  Mostrando mi PCB...")
        MostrarPCB(os.getpid(), f"HIJO  (PID {os.getpid()}, PPID {os.getppid()})")


        sys.exit(0)


    else:
              print(f"\n  [PADRE] fork() retorno {Pid}  →  soy el padre, cree al hijo PID {Pid}")


        print(f"  [PADRE] Esperando al hijo con waitpid()...")
        os.waitpid(Pid, 0)


        print(f"\n  [PADRE] El hijo termino.")
        print(f"  [PADRE] PID: {os.getpid()}")
        print(f"  [PADRE] Mostrando PCB actualizado (comparar voluntary_ctxt_switches)...")
        MostrarPCB(os.getpid(), f"PADRE despues del fork (PID {os.getpid()})")


        print(f"\n  Programa finalizado.")
        print("=" * 60)
        return 0


if __name__ == "__main__":
    Main()