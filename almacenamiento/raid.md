# 1. Crear un arreglo RAID1 con dos discos (/dev/sdb y /dev/sdc)
# RAID1 mantiene los datos duplicados en ambos discos (espejo).
sudo mdadm --create --verbose /dev/md0 --level=1 --raid-devices=2 /dev/sdb /dev/sdc

# 2. Verificar el estado del RAID recién creado
# Muestra los arreglos activos y su sincronización.
cat /proc/mdstat

# 3. Ver detalles completos del arreglo RAID
# Incluye nivel, discos activos, estado de sincronización y UUID.
sudo mdadm --detail /dev/md0

# 4. Simular una falla en uno de los discos (/dev/sdb)
# Marca el disco como "faulty" para probar la tolerancia a fallos.
sudo mdadm /dev/md0 --fail /dev/sdb

# 5. Verificar nuevamente los detalles del RAID
# Ahora debería mostrar que /dev/sdb está en estado "faulty".
sudo mdadm --detail /dev/md0

# 6. Remover el disco fallado del arreglo
# Se elimina /dev/sdb del RAID para simular reemplazo.
sudo mdadm /dev/md0 --remove /dev/sdb

# 7. Reagregar el disco al arreglo
# Esto inicia el proceso de reconstrucción automática (resync).
sudo mdadm /dev/md0 --add /dev/sdb

