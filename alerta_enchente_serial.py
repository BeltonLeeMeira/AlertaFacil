import serial
import time
import pandas as pd
import matplotlib.pyplot as plt

porta = 'COM3'  # Altere conforme sua porta
baud_rate = 9600
dados = []

try:
    arduino = serial.Serial(porta, baud_rate)
    print("Conectado ao Arduino!")
    time.sleep(2)

    while True:
        if arduino.in_waiting > 0:
            linha = arduino.readline().decode('utf-8').strip()
            print(f"[ALERTA] {linha}")
            tempo = time.strftime("%H:%M:%S")
            dados.append([tempo, linha])

            if len(dados) % 10 == 0:
                df = pd.DataFrame(dados, columns=["Horário", "Alerta"])
                df.to_csv("dados_enchente.csv", index=False)

except serial.SerialException:
    print("Não foi possível conectar ao Arduino. Verifique a porta.")
