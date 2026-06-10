 1. Inicializar el RAID como Physical Volume (PV) para LVM
# Esto convierte el dispositivo /dev/md0 en un volumen físico que LVM puede usar.
sudo pvcreate /dev/md0

# 2. Crear un Volume Group (VG) llamado "vg_lab"
# Agrupa uno o más PV en un conjunto lógico de almacenamiento.
sudo vgcreate vg_lab /dev/md0

# 3. Crear un Logical Volume (LV) de 500 MB llamado "lv_test"
# Es un volumen lógico dentro del VG, similar a una partición flexible.
sudo lvcreate -L 500M -n lv_test vg_lab

# 4. Formatear el LV con sistema de archivos ext4
# Esto prepara el volumen para almacenar datos.
sudo mkfs.ext4 /dev/vg_lab/lv_test

# 5. Crear carpeta de montaje para el LV
sudo mkdir /mnt/lvm_test

# 6. Montar el LV en la carpeta creada
# Permite acceder al volumen lógico como si fuera un disco normal.
sudo mount /dev/vg_lab/lv_test /mnt/lvm_test

# 7. Verificar que el LV está montado y disponible
# Muestra el espacio en disco y confirma que /mnt/lvm_test está activo.
df -h | grep lvm_test
