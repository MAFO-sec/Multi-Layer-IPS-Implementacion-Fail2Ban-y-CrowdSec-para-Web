import re
import psycopg2
from datetime import datetime

# Conexión a la DB de Superset
try:
    conn = psycopg2.connect(
        host="10.0.2.20", port="5432", database="superset", user="superset", password="superset"
    )
    cur = conn.cursor()
    log_pattern = re.compile(r'(\d+\.\d+\.\d+\.\d+) - - \[(.*?)\] "(.*?) (.*?) (.*?)" (\d+) (\d+|-)')

    with open('/var/log/apache2/access.log', 'r') as f:
        for line in f:
            match = log_pattern.match(line)
            if match:
                ip, dt_str, method, url, _, status, size = match.groups()
                dt = datetime.strptime(dt_str.split(' ')[0], '%d/%b/%Y:%H:%M:%S')
                size = 0 if size == '-' else int(size)
                cur.execute("INSERT INTO apache_logs (ip_address, datetime, method, url, status_code, size) VALUES (%s, %s, %s, %s, %s, %s)",
                            (ip, dt, method, url, int(status), size))
    conn.commit()
    print("¡Éxito! Logs insertados.")
except Exception as e:
    print(f"Error: {e}")
