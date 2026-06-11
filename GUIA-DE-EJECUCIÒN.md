## 1. RAID — Configuración y pruebas
(Contenido ubicado en almacenamiento/raid.md)

## 2. LVM — Volúmenes lógicos y expansión
(Contenido ubicado en almacenamiento/lvm.md)

## 3. BtrFS — Snapshots y restauración
(Contenido ubicado en almacenamiento/btrfs.md)

## 4. Orquestación y Resiliencia con Kubernetes (Kind)
Esta sección levanta un clúster de Kubernetes local, despliega aplicaciones con almacenamiento persistente y realiza pruebas de fallos para verificar la autorrecuperación.

## kind create cluster --config ~/proyecto-final/kubernetes/kind-config.yaml

Crea un clúster local de Kubernetes usando contenedores Docker, basándose en las reglas de arquitectura definidas en el archivo kind-config.yaml.

## kubectl apply -f ~/proyecto-final/kubernetes/nginx-pvc.yaml

Despliega un servidor Nginx configurado para usar un PVC (Persistent Volume Claim) , asegurando que sus datos no se pierdan si el pod muere.

## kubectl apply -f ~/proyecto-final/kubernetes/statefulset.yaml

Despliega un conjunto de Pods de Busybox usando un StatefulSet , ideal para aplicaciones que requieren una identidad única y almacenamiento persistente ordenado.

## kubectl get pods

Muestra el listado y el estado actual de todos los Pods en el clúster (comprobando si están corriendo correctamente).

## kubectl delete pod nginx-pod

Elimina manualmente el Pod de Nginx para simular una caída o falla del servidor.

## kubectl get pods

(Segunda ejecución) Permite verificar que Kubernetes, de forma automática, detecta la caída y levanta un nuevo Pod para reemplazar al eliminado ( Prueba de resiliencia ).

## kubectl delete pod busybox-set-0

Elimina el primer Pod del StatefulSet para probar su comportamiento ante fallos.

## kubectl get pods

(Tercera ejecución) Verifica que el StatefulSet crea automáticamente el Pod manteniendo el mismo nombre e identidad ( Prueba de autorrecuperación ).

## 5. Automatización de Copias de Seguridad (Python, Cron y Tar)
Esta sección ejecuta un script de respaldo, programa su ejecución automática cada 5 minutos y simula la restauración total de un archivo web borrado accidentalmente.

## python3 ~/proyecto-final/backups/backup.py ~/proyecto-final

Ejecuta manualmente el script de Python para realizar un respaldo del directorio~/proyecto-final .

## ls ~/proyecto-final | grep backup_cristian

Lista los archivos de la carpeta y filtra el resultado para confirmar que el archivo de respaldo (con el prefijobackup_cristian ) se creó correctamente.

## crontab -e

Abra el editor de tareas programadas del sistema (cron) para agregar o modificar automatizaciones.

Configuración de la línea Cron añadida:
## */5 * * * * /usr/bin/python3 /home/cristian/proyecto-final/backups/backup.py /home/cristian/proyecto-final >> /home/cristian/proyecto-final/cron.log 2>&1

*/5 * * * *: Indica al sistema que ejecuta la tarea cada 5 minutos .

/usr/bin/python3 ...: Lanza el script de copia de seguridad en Python usando las rutas absolutas recomendadas.

>> .../cron.log 2>&1: Guarde tanto el historial de ejecuciones exitosas como los errores dentro del archivo cron.logpara auditoría.

## tail -f ~/proyecto-final/cron.log

Muestra en tiempo real las últimas líneas del archivo log para monitorizar que el cron se ejecuta automáticamente sin errores.

## rm ~/proyecto-final/test.txt

Simulación de desastre: Borra el archivo principal de la web ( index.html) para probar el plan de recuperación.

## tar -xzf ~/proyecto-final/backup_cristian_YYYY-MM-DD_HH-MM-SS.tar.gz -C ~/proyecto-final

Descomprime ( -xf) el archivo de respaldo comprimido ( .tar.gz) y extrae su contenido directamente en la carpeta del proyecto ( -C ~/proyecto-final), restaurando el estado anterior.

## ls ~/proyecto-final
