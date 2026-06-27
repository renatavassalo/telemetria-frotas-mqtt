import random
import time
import paho.mqtt.client as mqtt
from config.mqtt_config import *

client = mqtt.Client(client_id=CLIENT_ID_PUBLISHER)
client.connect(BROKER, PORT)

print("🚚 Caminhão Cegonha na estrada... Enviando telemetria.")

while True:
    velocidade = random.randint(60, 110)
    client.publish(TOPIC, velocidade)
    print(f"Velocidade enviada: {velocidade} km/h")
    time.sleep(3)