# Sistema de Telemetria para Frotas Rodoviárias utilizando MQTT

## Disciplina

Redes de Computadores

---

# 1. Introdução

O transporte rodoviário é um dos principais meios de movimentação de cargas no Brasil. Empresas transportadoras dependem de informações em tempo real sobre seus veículos para aumentar a segurança, reduzir custos operacionais e acompanhar o comportamento dos motoristas durante as viagens.

Neste projeto será desenvolvido um sistema de telemetria utilizando o protocolo **MQTT (Message Queuing Telemetry Transport)** para monitorar veículos de uma frota em tempo real.

Como estudo de caso será utilizado o monitoramento de uma carreta rodoviária, simulando o envio periódico da velocidade do veículo para uma central de monitoramento.

O objetivo é demonstrar como protocolos de comunicação voltados para Internet das Coisas (IoT) podem ser utilizados em aplicações reais de transporte e logística.

---

# 2. Problema

Em rodovias, principalmente em longas viagens, é comum que veículos de carga percorram regiões com cobertura de internet limitada ou instável.

Além disso, equipamentos embarcados normalmente utilizam chips M2M (Machine-to-Machine), que possuem franquias reduzidas de dados móveis e exigem protocolos eficientes.

Outro problema é a necessidade de monitoramento em tempo real. Caso um caminhão ultrapasse o limite de velocidade estabelecido pela empresa, a central deve ser informada imediatamente para que ações possam ser tomadas rapidamente.

Essas características tornam inadequada a utilização de protocolos que geram grande volume de dados ou que dependam de requisições constantes entre cliente e servidor.

---

# 3. Objetivo

Desenvolver uma simulação de um sistema de telemetria para frotas utilizando o protocolo MQTT.

Durante a simulação, um dispositivo embarcado representará o equipamento instalado no caminhão, enviando periodicamente sua velocidade para um Broker MQTT.

Uma central de monitoramento receberá essas informações em tempo real e poderá identificar situações de risco, como excesso de velocidade.

O foco principal do projeto não é o desenvolvimento da aplicação, mas sim compreender a utilização do protocolo MQTT dentro de um cenário real de comunicação em redes.

---

# 4. Arquitetura da Solução

O sistema será composto por três elementos principais.

**Dispositivo Embarcado (Publisher)**

Simula o rastreador instalado no caminhão.

Responsável por enviar periodicamente informações de telemetria utilizando MQTT através da rede móvel.

↓

**Broker MQTT**

Servidor responsável por receber as mensagens publicadas pelos dispositivos e distribuí-las para todos os clientes interessados.

↓

**Central de Monitoramento (Subscriber)**

Recebe automaticamente todas as mensagens publicadas pelo caminhão e monitora os dados em tempo real.

---

# 5. Por que o MQTT foi escolhido?

A escolha do protocolo MQTT foi baseada nas características do cenário proposto.

O MQTT foi criado especificamente para comunicação entre dispositivos com poucos recursos computacionais e conexões de rede instáveis.

Em aplicações de telemetria, normalmente são transmitidas pequenas quantidades de dados diversas vezes ao longo do dia.

Nesse tipo de aplicação, reduzir o consumo de banda e aumentar a confiabilidade da comunicação é fundamental.

Comparado a outros protocolos, o MQTT oferece diversas vantagens para esse cenário.

---

# 6. Baixo consumo de banda

Uma das maiores vantagens do MQTT é seu cabeçalho extremamente pequeno.

O cabeçalho mínimo possui apenas **2 bytes**, reduzindo significativamente a quantidade de dados transmitidos.

Em um sistema de telemetria, onde milhares de mensagens podem ser enviadas diariamente, essa economia representa menor utilização da rede móvel e menor custo operacional.

Protocolos como HTTP possuem cabeçalhos muito maiores, contendo diversas informações de controle que não agregam valor à transmissão de pequenos dados de sensores.

---

# 7. Comunicação Publish/Subscribe

Diferentemente do HTTP, o MQTT utiliza o modelo **Publish/Subscribe**.

Nesse modelo, o dispositivo embarcado não envia dados diretamente para a central de monitoramento.

Ele apenas publica mensagens em um tópico.

O Broker MQTT é responsável por entregar essas mensagens para todos os dispositivos que estiverem inscritos nesse tópico.

Essa arquitetura reduz o acoplamento entre os sistemas, facilita a escalabilidade e permite que vários clientes recebam simultaneamente as mesmas informações.

Por exemplo:

* Central de Monitoramento
* Dashboard Web
* Aplicativo Mobile
* Banco de Dados
* Sistema de Alertas

Todos podem receber exatamente a mesma informação sem alterar o dispositivo instalado no caminhão.

---

# 8. Conexões persistentes

Outra vantagem importante é que o MQTT mantém uma conexão persistente entre cliente e Broker.

No HTTP, normalmente cada comunicação exige uma nova requisição.

Em aplicações onde informações são enviadas continuamente, estabelecer uma nova conexão a cada envio gera maior consumo de recursos e maior tempo de resposta.

No MQTT, após a conexão inicial, as mensagens são transmitidas continuamente pela mesma sessão.

Isso reduz a latência e melhora a eficiência da comunicação.

---

# 9. Funcionamento em redes instáveis

Rodovias frequentemente apresentam falhas de cobertura de internet.

Durante uma viagem o caminhão pode passar por:

* áreas rurais;
* túneis;
* regiões com troca de antenas da operadora;
* oscilações no sinal móvel.

O MQTT foi projetado para esse tipo de ambiente.

O protocolo permite reconexão automática e mecanismos que aumentam a confiabilidade da entrega das mensagens.

Essa característica torna o MQTT muito utilizado em aplicações de Internet das Coisas (IoT).

---

# 10. Qualidade de Serviço (QoS)

O MQTT oferece três níveis de Quality of Service (QoS), permitindo escolher o equilíbrio entre desempenho e confiabilidade.

### QoS 0

Entrega sem confirmação.

Menor consumo de banda.

Maior velocidade.

Pode ocorrer perda de mensagens.

---

### QoS 1

Entrega garantida pelo menos uma vez.

Existe confirmação de recebimento entre cliente e Broker.

Caso ocorra falha de comunicação, a mensagem poderá ser retransmitida.

É um bom equilíbrio entre desempenho e confiabilidade.

---

### QoS 2

Entrega exatamente uma vez.

É o nível mais seguro do protocolo.

Entretanto, exige maior troca de mensagens e maior consumo de recursos.

---

Neste projeto, o QoS 1 é considerado o mais adequado, pois oferece confiabilidade suficiente para aplicações de telemetria sem aumentar excessivamente o tráfego da rede.

---

# 11. Comparação entre MQTT, HTTP e CoAP

| Característica            | MQTT              | HTTP             | CoAP             |
| ------------------------- | ----------------- | ---------------- | ---------------- |
| Modelo de comunicação     | Publish/Subscribe | Cliente-Servidor | Cliente-Servidor |
| Transporte                | TCP               | TCP              | UDP              |
| Consumo de banda          | Muito baixo       | Alto             | Muito baixo      |
| Cabeçalho                 | Muito pequeno     | Grande           | Pequeno          |
| Comunicação em tempo real | Excelente         | Limitada         | Boa              |
| Redes instáveis           | Muito adequado    | Menos eficiente  | Adequado         |
| QoS nativo                | Sim               | Não              | Limitado         |

Embora o CoAP também seja um protocolo leve voltado para IoT, o MQTT foi escolhido por oferecer uma arquitetura baseada em Broker, comunicação Publish/Subscribe e suporte nativo a diferentes níveis de QoS, características bastante adequadas para monitoramento contínuo de frotas.

---

# 12. Tecnologias utilizadas

* Python
* MQTT
* Broker MQTT
* Biblioteca Paho MQTT
* Git
* GitHub



---

# 13. Conclusão

O protocolo MQTT foi escolhido por apresentar características compatíveis com sistemas de telemetria e Internet das Coisas.

Seu baixo consumo de banda, comunicação baseada em Publish/Subscribe, suporte a conexões persistentes e diferentes níveis de QoS tornam o protocolo uma solução eficiente para monitoramento contínuo de veículos em rodovias.

A proposta deste projeto busca demonstrar, de forma prática, como um protocolo de aplicação pode atender às necessidades de comunicação de um sistema de telemetria, priorizando eficiência, confiabilidade e escalabilidade.

---

# Referências

* OASIS. MQTT Version 5.0. OASIS Standard.
* MQTT.org. MQTT: The Standard for IoT Messaging.
* RFC 7252 - The Constrained Application Protocol (CoAP).
* RFC 9110 - HTTP Semantics.
