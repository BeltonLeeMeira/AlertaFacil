# AlertaFácil – Sistema de Alerta para Enchentes

Este projeto foi desenvolvido como parte da disciplina Edge Computing & IoT da Global Solution 2025, com o objetivo de propor uma solução tecnológica para minimizar os impactos causados por enchentes em áreas de risco no Brasil.

## Problema Identificado

As enchentes causam danos severos todos os anos, atingindo principalmente regiões com pouca infraestrutura e acesso a informações em tempo real. A falta de monitoramento constante e alertas precoces dificulta a evacuação e coloca vidas em risco.

## Solução Proposta

Desenvolvi o AlertaFácil, um sistema que simula um monitoramento inteligente de áreas alagáveis. A solução combina hardware e software para:

- Medir o nível da água com um sensor ultrassônico
- Classificar o risco (seguro, atenção, emergência)
- Acionar alertas locais com LEDs e buzzer
- Enviar os dados para uma aplicação externa via rede
- Armazenar as medições em um arquivo .csv e visualizar com gráficos

## Tecnologias Utilizadas

- ESP32 (simulado via Wokwi)
- Sensor ultrassônico HC-SR04
- LEDs e buzzer
- Python 3
  - Bibliotecas: serial, pandas, matplotlib, paho-mqtt

## Link para o Projeto no Wokwi

https://wokwi.com/projects/432410859495840769

## Instruções para Execução

1. Abra o projeto no Wokwi
2. Observe os LEDs e buzzer mudando conforme a altura simulada da água
3. Rode o script mqtt.py no seu computador
4. Os dados serão recebidos via rede e salvos em dados_enchente.csv
5. Um gráfico pode ser gerado a partir do arquivo .csv usando o script alerta_enchente_serial.py

## Estrutura do Repositório

```
 AlertaFacil
├── alerta_enchente_serial.py       # Gera gráfico e salva CSV com base nos dados recebidos
├── mqtt.py                         # Cliente que escuta dados de alerta do servidor
├── grafico_alerta_enchente.png    # Gráfico gerado com os dados simulados
├── AlertaFacil.docx                # Documentação técnica do projeto
├── README.md                       # Este arquivo
```

## Funcionalidades Demonstradas

- Simulação de hardware com sensores
- Ações automáticas locais
- Captura e transmissão de dados
- Armazenamento estruturado (servidor local)
- Visualização de alertas com gráfico

## Autor

Belton Meira  RM 560760
