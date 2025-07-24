from prometheus_client import start_http_server, Gauge
import random
import time

# Define custom metric
temperature_gauge = Gauge('room_temperature_celsius', 'Simulated room temperature in Celsius')
humidity_gauge = Gauge('room_humidity_percent', 'Simulated room humidity in percent')

def generate_metrics():
    while True:
        # Simulate sensor readings
        temp = random.uniform(20.0, 30.0)
        humidity = random.uniform(30.0, 60.0)

        # Update metrics
        temperature_gauge.set(temp)
        humidity_gauge.set(humidity)

        print(f"Pushed temperature={temp:.2f}°C, humidity={humidity:.2f}%")
        time.sleep(5)

if __name__ == "__main__":
    # Start metrics HTTP server on port 8000
    start_http_server(8000)
    generate_metrics()
