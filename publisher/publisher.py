import random
import time
import json
from datetime import datetime

import paho.mqtt.client as mqtt

from config.mqtt_config import *

VEICULOS = [
    {
        "veiculo": "TRUCK-001",
        "placa": "ABC-1234"
    },
    {
        "veiculo": "TRUCK-002",
        "placa": "XYZ-5678"
    },
    {
        "veiculo": "TRUCK-003",
        "placa": "DEF-9012"
    }
]

client = mqtt.Client(client_id=CLIENT_ID_PUBLISHER)
client.connect(BROKER, PORT)

print("🚚 Frota na estrada... Enviando telemetria.")

while True:

    veiculo_atual = random.choice(VEICULOS)

    payload = {
        "veiculo": veiculo_atual["veiculo"],
        "placa": veiculo_atual["placa"],
        "velocidade": random.randint(60, 110),
        "latitude": -29.765432,
        "longitude": -51.153214,
        "timestamp": datetime.now().isoformat()
    }

    topic_veiculo = f"telemetria/frotas/{payload['veiculo']}"

    client.publish(
        topic_veiculo,
        json.dumps(payload),
        qos=1
    )

    print("📤 Telemetria enviada:")
    print(json.dumps(payload, indent=4, ensure_ascii=False))

    time.sleep(3)