import os
import sys
import time


def Main() -> None:


    print("=" * 55)
    print("  EJERCICIO 3 — Proceso Huerfano")
    print("=" * 55)


    Pid: int = os.fork()


    if Pid == 0:


        PpidInicial: int = os.getppid()
        print(f"  [HIJO]   PID {os.getpid()} — PPID inicial: {PpidInicial}")
        print(f"  [HIJO]   Durmiendo 2s. El padre terminara antes que yo.")
        time.sleep(2)
        
        PpidFinal: int = os.getppid()
        print(f"\n  [HIJO]   Mi padre original (PID {PpidInicial}) ya no existe.")
        print(f"  [HIJO]   Mi nuevo PPID: {PpidFinal} — adoptado por init/systemd.")
        sys.exit(0)


    print(f"  [PADRE]  PID {os.getpid()} — terminando antes que el hijo PID {Pid}.")
    print(f"  [PADRE]  Sin waitpid(). El hijo quedara huerfano.")
    print(f"  [PADRE]  El kernel reasignara al hijo a init/systemd automaticamente.")
    sys.exit(0)


if __name__ == "__main__":
    Main()