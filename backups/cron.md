# Configuración de cron para automatizar backups

# Este cron ejecuta el script backup.py cada 5 minutos.
# - Cambia al directorio que quiero respaldar
# - Ejecuta el script con Python3
# - Redirige salida y errores a cron.log

*/5 * * * * cd /home/cristian/proyecto-final && /usr/bin/python3 /home/cristian/proyecto-final/backups/backup.py /home/cristian/proyecto-final >> /home/cristian/proyecto-final/cron.log 2>&1
