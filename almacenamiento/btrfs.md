# 1. Crear carpeta de montaje para el disco BtrFS
sudo mkdir /mnt/btrfs_test

# 2. Montar el disco /dev/sdd en la carpeta creada
sudo mount /dev/sdd /mnt/btrfs_test

# 3. Crear un subvolumen llamado "snap1"
sudo btrfs subvolume create /mnt/btrfs_test/snap1

# 4. Crear un archivo de prueba dentro del subvolumen
echo "Archivo de prueba restaurable" | sudo tee /mnt/btrfs_test/snap1/test.txt

# 5. Crear un snapshot del subvolumen "snap1" en "restore"
sudo btrfs subvolume snapshot /mnt/btrfs_test/snap1 /mnt/btrfs_test/restore

# 6. Simular pérdida de datos borrando el archivo original
sudo rm /mnt/btrfs_test/snap1/test.txt

# 7. Crear carpeta de montaje para acceder al snapshot
sudo mkdir /mnt/restore

# 8. Montar el snapshot "restore" directamente desde el disco
sudo mount -o subvol=restore /dev/sdd /mnt/restore

# 9. Verificar que el archivo sigue existiendo en el snapshot
ls /mnt/restore/snap1
