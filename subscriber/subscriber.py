import json
import paho.mqtt.client as mqtt

from config.mqtt_config import *

def on_message(client, userdata, msg):
    data = json.loads(msg.payload.decode())

    veiculo = data["veiculo"]
    placa = data["placa"]
    velocidade = data["velocidade"]
    latitude = data["latitude"]
    longitude = data["longitude"]
    timestamp = data["timestamp"]

    print("=" * 50)
    print("🚚 NOVA TELEMETRIA RECEBIDA")
    print(f"Veículo.....: {veiculo}")
    print(f"Placa.......: {placa}")
    print(f"Velocidade..: {velocidade} km/h")
    print(f"Latitude....: {latitude}")
    print(f"Longitude...: {longitude}")
    print(f"Horário.....: {timestamp}")

client = mqtt.Client(client_id=CLIENT_ID_SUBSCRIBER)

client.on_message = on_message

client.connect(BROKER, PORT)

client.subscribe(TOPIC)

print("🖥️ Central de Monitoramento Ativa. Aguardando dados da frota...")

client.loop_forever()