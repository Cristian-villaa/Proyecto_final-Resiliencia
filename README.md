# Entorno de Alta Disponibilidad y Persistencia en Recursos Limitados

Este proyecto demuestra la implementación, gestión y recuperación de fallos en un entorno de infraestructura y orquestación utilizando una máquina virtual con recursos estrictamente limitados (**3 GB de RAM** y almacenamiento reducido). 

El objetivo principal es integrar conceptos avanzados de almacenamiento redundante, sistemas de archivos modernos, snapshots, orquestación con Kubernetes y automatización de respaldos para garantizar la **alta disponibilidad y continuidad del negocio**.

---

## 🚀 Objetivos del Proyecto

- **Redundancia de Almacenamiento:** Configuración y simulación de fallos en arreglos RAID1 y LVM.  
- **Gestión Eficiente de Archivos:** Implementación de BtrFS y comparación de snapshots frente a LVM.  
- **Orquestación en Entornos Reducidos:** Despliegue de un clúster de Kubernetes nativo en contenedores (Kind).  
- **Persistencia y Autorrecuperación:** Validación de volúmenes persistentes y cargas de trabajo con estado (StatefulSets).  
- **Automatización de Backups:** Scripts en Python integrados con `cron` para la resiliencia de datos.  

---

## 🛠️ Arquitectura y Tecnologías

- **Entorno:** Máquina Virtual (Linux Ubuntu/Debian) con **3 GB de RAM**. 
- **Almacenamiento:** RAID1 (MDADM), LVM (Logical Volume Manager), BtrFS. 
- **Contenedores y Orquestación:** Docker, Kind (Kubernetes IN Docker), Kubernetes (Pods, PVC, StatefulSets).  
- **Automatización:** Python 3, Cron. 

---

## 📋 Desarrollo del Proyecto

### 1. Capa de Almacenamiento Redundante (RAID1 y LVM)
Se configuró un arreglo RAID1 con dos discos virtuales en espejo para garantizar la redundancia física.  
Sobre este arreglo se implementó LVM, creando un volumen lógico que permite flexibilidad en la gestión del espacio.  
Se simuló la falla de un disco y se demostró la recuperación automática sin pérdida de datos, validando la tolerancia a fallos.

---

### 2. Gestión Avanzada con BtrFS y Snapshotting
Se configuró un sistema de archivos BtrFS para aprovechar sus capacidades modernas.  
Se crearon subvolúmenes y snapshots que permiten capturar el estado de los datos en un instante.  
Se simuló la pérdida de archivos y se demostró la restauración inmediata desde snapshots, comparando su eficiencia frente a los snapshots de LVM.

**Comparativa:**
- LVM opera a nivel de bloque y requiere espacio reservado. 
- BtrFS opera a nivel de sistema de archivos, con snapshots dinámicos y eficientes gracias a *Copy-on-Write*.  

---

### 3. Orquestación y Persistencia con Kubernetes (Kind)
Se desplegó un clúster mínimo con Kind, adaptado a los recursos limitados de la VM.  
Se validó la persistencia de datos mediante un Pod de Nginx con un volumen persistente.  
Se demostró que al eliminar el Pod, los datos permanecen intactos y son reutilizados por el nuevo Pod.  
Además, se implementó un StatefulSet con réplicas de Busybox, mostrando la autorrecuperación automática de Pods y la preservación de su identidad y almacenamiento.

---

### 4. Automatización de Respaldos (Python + Cron)
Se desarrolló un script en Python que genera respaldos comprimidos de un directorio crítico, incluyendo fecha y hora en el nombre del archivo.  
Se integró con `cron` para ejecutar respaldos periódicos de manera automática. 
Se probó la restauración de datos tras un borrado masivo, confirmando la resiliencia y continuidad del negocio.

---

## 📊 Resultados

- **RAID1:** Redundancia física validada, con recuperación automática tras la falla de un disco.  
- **LVM:** Flexibilidad en la gestión de volúmenes, funcionando sobre RAID. 
- **BtrFS:** Snapshots instantáneos y restauración inmediata de datos. 
- **Kubernetes (Kind):** Persistencia de datos en Pods y autorrecuperación con StatefulSets.  
- **Automatización:** Backups periódicos y restauración exitosa tras pérdida de datos.  

---

## 📈 Conclusiones
Este proyecto demuestra que las estrategias de **Alta Disponibilidad, Tolerancia a Fallos y Continuidad de Negocio** pueden implementarse incluso en entornos con recursos severamente limitados.  

Mediante el uso de **RAID1, LVM, BtrFS, Kubernetes con Kind y automatización con Python + cron**, se garantiza la resiliencia y recuperación de datos críticos en infraestructuras locales, ofreciendo una solución práctica y replicable para laboratorios y entornos educativos.

---

## 👤 Autor
**Cristian-Villavicencio** 
Proyecto Final — Administración de Sistemas Avanzada
Junio 2026 

---

## 🏁 Licencia
Este proyecto se distribuye bajo licencia MIT.
