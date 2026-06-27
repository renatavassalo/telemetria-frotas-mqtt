import paho.mqtt.client as mqtt
from config.mqtt_config import *

def on_message(client, userdata, msg):
    velocidade = int(msg.payload.decode())
    print(f"📡 Telemetria recebida | Velocidade: {velocidade} km/h")

client = mqtt.Client(client_id=CLIENT_ID_SUBSCRIBER)

client.on_message = on_message

client.connect(BROKER, PORT)

client.subscribe(TOPIC)

print("🖥️ Central de Monitoramento Ativa. Aguardando dados da frota...")

client.loop_forever()