import platform
import psutil
import wmi
from datetime import datetime

print("¡Hola, mundo mi nombre es Joel Alcalá y este es mi primer codigo Python!")
print(f"fecha y hora: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ")

# información basica del sistema

print(f" Sistema Operativo: {platform.system()} {platform.release()}\n")
print(f"Procesador: {platform.processor()}")

# CPU y memoria con psutil
print(f"  CPU física: {psutil.cpu_count(logical=False)} núcleos")
print(f"  CPU lógica: {psutil.cpu_count(logical=True)} hilos")
print(f"  RAM total: {round(psutil.virtual_memory().total / (1024**3), 2)} GB")

# infor avanzada con WMI (solo Windows)

try:
    c = wmi.WMI()
    for board in c.Win32_baseBoard():
        print(f"Placa Base: {board.Manufacturer} {board.Product}")

    for gpu in c.Win32_VideoController():
        print(f"Tarjeta de Video: {gpu.Name}")


finally:
    print("codigo ejecutado")