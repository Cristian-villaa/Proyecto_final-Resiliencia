#!/usr/bin/python3
import os
import sys
import tarfile
import datetime

def crear_backup(ruta_directorio):
    # Verificar que el directorio existe
    if not os.path.isdir(ruta_directorio):
        print(f"❌ Error: El directorio {ruta_directorio} no existe.")
        return

    # Crear nombre del archivo con formato requerido
    fecha_hora = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    nombre_backup = f"backup_cristian_{fecha_hora}.tar.gz"
    ruta_backup = os.path.join(ruta_directorio, nombre_backup)

    # Crear archivo comprimido (solo contenido, no carpeta raíz)
    with tarfile.open(ruta_backup, "w:gz") as tar:
        tar.add(ruta_directorio, arcname=".")

    # Mensaje de éxito con DNI
    print(f"✅ Backup creado exitosamente: {nombre_backup} - DNI: 10345654")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python3 backup.py <ruta_directorio>")
    else:
        crear_backup(sys.argv[1])
