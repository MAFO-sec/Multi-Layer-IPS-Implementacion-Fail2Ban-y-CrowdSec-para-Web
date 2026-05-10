# 🛡️ Multi-Layer IPS: Defensive Security Lab

### Implementación de Fail2Ban y CrowdSec para Seguridad Web

Este repositorio contiene el diseño y despliegue de un laboratorio de **Ciberseguridad Defensiva**, enfocado en un Sistema de Prevención de Intrusiones (IPS) multicapa y monitorización avanzada mediante un **SOC (Security Operations Center)**.

El laboratorio cubre el ciclo completo de respuesta ante incidentes: detección de ataques de fuerza bruta, visualización de métricas en tiempo real y mitigación automatizada.

---

## 🚀 Resumen del Proyecto

La arquitectura simula un entorno de producción donde una aplicación web es protegida por dos capas de defensa activa.

* **Fail2Ban (Capa de Reglas Locales):** Analiza logs mediante Regex y bloquea IPs en el firewall local.
* **CrowdSec (Capa de Inteligencia Colectiva):** Análisis de comportamiento y base de datos global de reputación.
* **Monitorización SOC:** Dashboard en **Apache Superset** alimentado por un pipeline ETL en Python.

---

## 🛠️ Tecnologías y Herramientas

* **Infraestructura:** Docker, Docker Compose, Nginx (Proxy Inverso).
* **Seguridad:** Fail2Ban, CrowdSec (LAPI + Firewall Bouncer).
* **Backend:** Python (Flask), PostgreSQL.
* **Análisis:** Apache Superset, Python ETL.
* **Pentesting:** Kali Linux, Hydra.

---

## 📂 Estructura del Proyecto

* `/app`: Aplicación Flask y Dockerfile.
* `/proxy`: Configuración de Nginx.
* `/fail2ban`: Filtros y cárceles (jail.d).
* `/crowdsec`: Configuración de adquisición y whitelists.
* `/scripts`: Pipeline ETL para logs.
* `/docs`: Documentación técnica detallada (PDF).

---

## 🧪 Validación: Prueba de Concepto (PoC)

1.  **Ataque:** Uso de **Hydra** contra `/login` para generar fuerza bruta.
2.  **Detección:** Generación de logs 401 detectados por Fail2Ban y CrowdSec.
3.  **Bloqueo:** Verificación del baneo con `cscli decisions list` y `fail2ban-client`.
4.  **Visualización:** El pico de ataques se refleja en el dashboard de Superset.

---

## 🔧 Instalación Rápida

```bash
# 1. Levantar el entorno
docker-compose up -d

# 2. Iniciar monitorización
python3 scripts/procesar_logs.py

## 📑 Documentación Detallada
Puedes consultar la guía técnica completa en formato PDF aquí: 
[👉 Descargar Guía del Proyecto (PDF)](docs/Guia_Tecnica_IPS.pdf)
