
import paho.mqtt.client as mqtt

# Configurações do broker
broker = "broker.hivemq.com"
port = 1883
topic = "alerta/enchente/aluno560760"

# Callback quando a conexão é estabelecida
def on_connect(client, userdata, flags, rc):
    print("Conectado ao broker MQTT com código:", rc)
    client.subscribe(topic)

# Callback quando uma mensagem é recebida
def on_message(client, userdata, msg):
    print(f"Mensagem recebida [{msg.topic}]: {msg.payload.decode()}")

# Criação do cliente MQTT
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(broker, port, 60)

# Loop infinito para escutar as mensagens
print("Aguardando mensagens MQTT...\n")

client.loop_forever()
