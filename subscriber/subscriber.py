import json
import paho.mqtt.client as mqtt

from config.mqtt_config import *

LIMITE_VELOCIDADE = 90


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

    if velocidade > LIMITE_VELOCIDADE:
        print("\n🚨 ALERTA DE EXCESSO DE VELOCIDADE!")
        print(f"Veículo: {veiculo}")
        print(f"Velocidade atual: {velocidade} km/h")
        print(f"Limite permitido: {LIMITE_VELOCIDADE} km/h")
    else:
        print("\n✅ Velocidade dentro do limite.")


client = mqtt.Client(client_id=CLIENT_ID_SUBSCRIBER)

client.on_message = on_message

client.connect(BROKER, PORT)

client.subscribe(TOPIC, qos=1)

print("🖥️ Central de Monitoramento Ativa. Aguardando dados da frota...")

client.loop_forever()