# Entorno de Alta Disponibilidad y Persistencia en Recursos Limitados

Este proyecto demuestra la implementación, gestión y recuperación de fallos en un entorno de infraestructura y orquestación utilizando una máquina virtual con recursos estrictamente limitados (**3 GB de RAM** y almacenamiento reducido). 

El objetivo principal es integrar conceptos avanzados de almacenamiento redundante, sistemas de archivos modernos, snapshots, orquestación con Kubernetes y automatización de respaldos para garantizar la **alta disponibilidad y continuidad del negocio**.

---
## 🎯 Objetivos del Proyecto

- *Redundancia Física:* RAID1 para tolerancia a fallos de disco.  
- *Flexibilidad Lógica:* LVM y BtrFS para snapshots y gestión dinámica.  
- *Orquestación y Persistencia:* Kubernetes con Kind para cargas de trabajo con estado.  
- *Automatización:* Backups periódicos con Python + cron.  

---

## 🧱 Arquitectura en Capas

El proyecto se organiza en *cuatro capas de respaldo*, cada una relacionada con la anterior:

| Capa | Tecnología | Relación con la anterior |
|------|-------------|--------------------------|
| *Hardware* | RAID1 (MDADM) | Base física: asegura que los discos no sean un único punto de falla. |
| *Volúmenes Lógicos* | LVM + BtrFS | Se construyen sobre RAID: agregan flexibilidad y snapshots para restaurar estados internos. |
| *Copias Externas* | Python + Cron | Se apoyan en los volúmenes: generan respaldos fuera del sistema para recuperación total. |
| *Orquestación* | Kubernetes (Kind) | Se apoya en las capas inferiores: garantiza la persistencia y autorrecuperación de aplicaciones y servicios. |

👉 *Relación:* RAID protege el hardware → LVM/BtrFS protegen la lógica → Backups externos aseguran continuidad → Kubernetes mantiene la disponibilidad de los servicios.
---

## ⚙️ Desarrollo del Proyecto

### 1️⃣ RAID1 + LVM
- RAID1 con discos en espejo para redundancia física.  
- LVM sobre RAID para crear volúmenes lógicos flexibles.  
- Simulación de falla de disco con recuperación automática.  

📌 Resultado: redundancia física validada.

---

### 2️⃣ BtrFS y Snapshots
- Configuración de BtrFS con subvolúmenes y snapshots instantáneos.  
- Comparación frente a snapshots de LVM.  
- Restauración inmediata tras pérdida de archivos.  

📌 Resultado: resiliencia lógica y eficiencia superior.

---

### 3️⃣ Kubernetes (Kind)
- Clúster mínimo adaptado a recursos limitados.  
- Validación de persistencia en Pods y StatefulSets.  
- Autorrecuperación automática de cargas de trabajo.  

📌 Resultado: continuidad de servicios garantizada.

---

### 4️⃣ Backups Automatizados
- Script en Python para respaldos comprimidos con fecha/hora.  
- Integración con cron para ejecución periódica.  
- Restauración tras borrado masivo validada.  

📌 Resultado: copias externas y recuperación total.

---

## 📈 Conclusiones

Este proyecto demuestra que la *resiliencia completa* se logra combinando capas:  
- *RAID1* protege contra fallos físicos.  
- *LVM/BtrFS* permiten snapshots y flexibilidad lógica.  
- *Backups externos* aseguran continuidad frente a desastres.  

La integración de estas capas, junto con Kubernetes y automatización, ofrece una solución práctica y replicable para entornos educativos y laboratorios.

---

## 👤 Autor
**Cristian-Villavicencio** 
Proyecto Final — Administración de Sistemas Avanzada
Junio 2026 

---

## 🏁 Licencia
Este proyecto se distribuye bajo licencia MIT.
