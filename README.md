# MediPulse - Medical IoT & Big Data

## Étudiant 1 : Sources de données et ingestion Kafka

### Objectif
Simuler la surveillance des constantes vitales
de patients en temps réel et préparer leur
transmission vers Apache Kafka.

### Données simulées
- 5 patients fictifs
- 5 capteurs IoT
- 50 enregistrements JSON
- Une mesure par seconde

### Schéma des données
- record_id : identifiant unique
- patient_id : identifiant du patient
- sensor_id : identifiant du capteur
- heart_rate : fréquence cardiaque (BPM)
- body_temperature : température corporelle (°C)
- spo2 : saturation en oxygène (%)
- respiratory_rate : fréquence respiratoire
- location : chambre du patient
- event_time : horodatage UTC

### Technologies
Python, JSON, Apache Kafka, Git et GitHub.

### Installation
python -m pip install -r requirements.txt

### Exécution
1. python data_generator.py
2. python validate_data.py
3. python producer.py

### Topic Kafka proposé
medical_sensors


### Sources de données

Le projet MediPulse utilise deux sources :

1. Données synthétiques :
   - Générées avec data_generator.py
   - 5 patients fictifs
   - 50 enregistrements de test

2. Données médicales enregistrées :
   - BIDMC PPG and Respiration Dataset (PhysioNet)
   - Fichier : bidmc_01_DATA.csv
   - Conversion : read_real_data.py
   - Résultat : bidmc_real_data.jsonl

### Résultats des tests

- 481 lignes BIDMC analysées.
- 468 enregistrements conservés.
- 13 lignes incomplètes exclues.
- 468 enregistrements traités en Dry Run.
- Transmission Kafka réelle : à valider.

### Commandes de test

python read_real_data.py
python producer.py

### Limites

Les données BIDMC proviennent de mesures historiques
enregistrées par de véritables équipements médicaux.

Elles sont relues progressivement pour simuler un flux,
mais ne sont pas acquises en direct.

Les capteurs physiques ne sont pas encore connectés.
Le projet est un prototype pédagogique non clinique.

### Documentation

Consulter INTEGRATION.md pour les instructions
de configuration et d'intégration Kafka.
