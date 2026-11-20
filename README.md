# Big Data - IoT Sensor Monitoring

## Étudiant 1 : Sources de données et ingestion Kafka

### Objectif
Simuler des capteurs IoT et préparer l'envoi
des données vers Apache Kafka.

### Technologies
- Python
- JSON
- Apache Kafka
- kafka-python

### Fichiers
- data_generator.py : génération des données.
- sensor_data.jsonl : dataset de 50 mesures.
- producer.py : préparation et envoi des messages.
- requirements.txt : dépendances Python.

### Installation
pip install -r requirements.txt

### Exécution
1. python data_generator.py
2. python producer.py

### Topic Kafka proposé
iot_sensors

### Résultats des tests
- 5 capteurs IoT simulés.
- 50 enregistrements générés.
- Lecture des données réussie.
- Test local du Producer réussi (Dry Run).
- Test avec un Kafka Broker réel à effectuer.