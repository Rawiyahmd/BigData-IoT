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

## Source de données réelles — BIDMC

Source : BIDMC PPG and Respiration Dataset (PhysioNet)

Fichiers :
- bidmc_01_DATA.csv : mesures médicales enregistrées
- read_real_data.py : conversion et nettoyage
- bidmc_real_data.jsonl : données prêtes pour le Producer

Résultats :
- 481 lignes analysées
- 468 enregistrements conservés
- 13 lignes incomplètes exclues
- 468 enregistrements traités en mode Dry Run

Commandes de test :

python read_real_data.py
python producer.py

Remarque :
Les données proviennent d'enregistrements historiques de
capteurs médicaux réels.

Leur lecture progressive reproduit un flux de données,
mais ne constitue pas une acquisition en direct.

La transmission vers un Kafka Broker et l'intégration de
capteurs physiques restent à valider.
