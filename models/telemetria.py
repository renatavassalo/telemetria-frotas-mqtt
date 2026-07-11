from datetime import datetime


def criar_telemetria(veiculo, placa, velocidade, latitude, longitude):
    return {
        "veiculo": veiculo,
        "placa": placa,
        "velocidade": velocidade,
        "latitude": latitude,
        "longitude": longitude,
        "timestamp": datetime.now().isoformat()
    }