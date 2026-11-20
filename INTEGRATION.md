# MediPulse - Guide d'intégration Kafka

## Configuration proposée

- Topic Kafka : medical_sensors
- Format des messages : JSON UTF-8
- Identifiant unique : record_id
- Horodatage : event_time (UTC)
- Fréquence : environ 1 message/seconde

## Installation

python -m pip install -r requirements.txt

## Test local sans Docker

python data_generator.py
python validate_data.py
python producer.py

## Test réel avec Kafka (PowerShell)

Prérequis : Kafka démarré et topic créé.

$env:DRY_RUN="false"
$env:KAFKA_BOOTSTRAP_SERVERS="localhost:9092"
python producer.py

Adapter l'adresse du broker selon Docker Compose.

## Vérification

- Vérifier la réception des 50 messages.
- Vérifier le contenu JSON avec un Consumer.
- Enregistrer les preuves du test.

## Retour au mode local

$env:DRY_RUN="true"

## État actuel

Les tests locaux sont réussis.
La transmission réelle reste à valider.

Toutes les données sont synthétiques.