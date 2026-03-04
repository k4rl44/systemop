import os
import sys
import time


def MostrarEstado(Pid: int, Etiqueta: str) -> None:


    try:
        with open(f"/proc/{Pid}/status") as F:
            for Linea in F:
                if Linea.startswith("State"):
                    print(f"  [{Etiqueta}]  {Linea.strip()}")
    except FileNotFoundError:
        print(f"  [{Etiqueta}]  /proc/{Pid}/status no existe — PCB liberado")


def Main() -> None:


    print("=" * 55)
    print("  EJERCICIO 2A — Proceso Zombie")
    print("=" * 55)


    Pid: int = os.fork()ps


    if Pid == 0:


        print(f"  [HIJO]   PID {os.getpid()} — terminando con exit(0).")
        print(f"  [HIJO]   Mi PCB quedara en la tabla como zombie.")
        sys.exit(0)


    print(f"  [PADRE]  PID {os.getpid()} — durmiendo 2s sin llamar waitpid().")
    print(f"  [PADRE]  El hijo PID {Pid} ya termino pero su PCB sigue en el kernel.")
    time.sleep(2)


    print(f"\n  [PADRE]  Leyendo estado del hijo MIENTRAS es zombie:")
    MostrarEstado(Pid, "ZOMBIE ACTIVO")


    print(f"\n  [PADRE]  Llamando waitpid()...")
    os.waitpid(Pid, 0)
    print(f"  [PADRE]  PCB del hijo liberado.")


    print(f"\n  [PADRE]  Leyendo estado del hijo DESPUÉS del waitpid():")
    MostrarEstado(Pid, "POST WAITPID")


    print("\n" + "=" * 55)




if __name__ == "__main__":
    Main()