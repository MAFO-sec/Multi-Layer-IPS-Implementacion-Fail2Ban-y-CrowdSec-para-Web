Multi-Layer IPS: Implementing Fail2Ban and CrowdSec for Web Security

Este repositorio documenta el diseño y despliegue de un laboratorio de Ciberseguridad Defensiva, centrado en un Sistema de Prevención de Intrusiones (IPS) multicapa y monitorización avanzada a través de un SOC (Security Operations Center).

El laboratorio cubre el ciclo completo de respuesta ante incidentes: detección de ataques de fuerza bruta, visualización de métricas en tiempo real y mitigación automatizada.
🚀 Resumen del Proyecto

La infraestructura simula un entorno real donde una aplicación web es protegida por dos capas de defensa activa que reaccionan ante comportamientos maliciosos detectados en los logs del servidor.
🛡️ Capas de Defensa (IPS)

    Fail2Ban (Capa Local): Monitoriza logs en busca de patrones específicos mediante expresiones regulares (Regex) y bloquea IPs en el firewall local tras superar un umbral de reintentos.

    CrowdSec (Capa Inteligente): Utiliza un motor de análisis de comportamiento y una base de datos comunitaria para bloquear amenazas conocidas antes de que comprometan el sistema.

📊 Monitorización (SOC)

    Apache Superset: Dashboard interactivo que visualiza el tráfico malicioso.

    Python ETL: Un pipeline personalizado que procesa los logs de acceso en formato CLF y alimenta una base de datos PostgreSQL.

🛠️ Tecnologías Utilizadas

    Contenedores: Docker & Docker Compose.

    Servidor Web: Nginx (Proxy Inverso) & Flask (Backend Python).

    Seguridad: Fail2Ban & CrowdSec (LAPI + Firewall Bouncer).

    Análisis de Datos: Apache Superset & PostgreSQL.

    Lenguajes: Python y Bash.

📂 Estructura del Repositorio

    /app: Código fuente de la aplicación Flask, plantillas HTML y Dockerfile.

    /proxy: Configuración de Nginx para la transparencia de IPs (X-Forwarded-For).

    /fail2ban: Filtros (filter.d) y cárceles (jail.d) personalizadas para el login.

    /crowdsec: Configuración de adquisición de logs (acquis.yaml) y whitelists.

    /scripts: Script Python para el procesamiento de logs hacia Superset.

    /docs: Documentación técnica detallada (PDF).

🧪 Pruebas de Concepto (PoC)

Para validar la eficacia del sistema, se realizaron las siguientes pruebas:

    Ataque de Fuerza Bruta: Uso de Hydra contra el puerto 8081 para simular un intento de intrusión.

    Detección: Los logs registran errores 401 en formato estándar, detectados por Fail2Ban y CrowdSec.

    Bloqueo: Verificación del baneo inmediato mediante comandos cscli y fail2ban-client.

    Visualización: Observación en tiempo real del pico de ataques en el Dashboard de Superset.

🔧 Instalación Rápida

    Levantar infraestructura:
    Bash

    docker-compose up -d

    Configurar CrowdSec:
    Añadir el bouncer de firewall y ajustar la whitelist en /etc/crowdsec/parsers/s02-enrich/whitelists.yaml para permitir pruebas en red local.

    Ejecutar Monitorización:
    Bash

    python3 scripts/procesar_logs.py

👤 Autor

    MAFO-sec
