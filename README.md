# Educertify - Système de Certification de Diplômes sur Blockchain

## 📋 Description
Educertify est une plateforme innovante qui utilise la technologie blockchain (Hedera Hashgraph) pour certifier et vérifier l'authenticité des diplômes universitaires. Cette solution permet aux établissements d'éducation d'émettre des diplômes numériques infalsifiables, tout en offrant aux étudiants un moyen simple et sécurisé de partager leurs certifications avec des employeurs ou d'autres institutions.

## ✨ Fonctionnalités Principales

### Pour les Établissements
- **Publication sécurisée** des diplômes sur la blockchain Hedera
- **Gestion simplifiée** des émissions de diplômes
- **Traçabilité complète** de chaque diplôme émis

####exemple:
![WhatsApp Image 2025-10-27 à 22 03 52_a622a3a0](https://github.com/user-attachments/assets/7852ea5f-ed46-4bc8-aa5a-e30682083b3f)


### Pour les Étudiants
- **Accès permanent** à vos diplômes certifiés
- **Partage facile** avec les employeurs
- **Vérification instantanée** de l'authenticité

### Pour les Employeurs
- **Vérification en temps réel** de la validité des diplômes
- **Processus de recrutement** simplifié et sécurisé
- **Confiance accrue** dans les documents présentés

####exemple:
![WhatsApp Image 2025-10-27 à 22 04 16_74509a16](https://github.com/user-attachments/assets/ed9e39a6-7e48-4685-a125-bc985b283bc4)


## 🛠️ Technologies Utilisées
- **Backend**: Django (Python)
- **Blockchain**: Hedera Hashgraph
- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap 5
- **Base de données**: SQLite (développement) / PostgreSQL (production)

## 🚀 Installation

1. **Cloner le dépôt**
   ```bash
   git clone https://github.com/rhouzf/Educertify.git
   cd Educertify/backend
   ```

2. **Configurer l'environnement**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Sur Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Configurer les variables d'environnement**
   Créez un fichier `.env` à la racine du projet avec :
   ```
   HEDERA_ACCOUNT_ID=votre_compte_hedera
   HEDERA_PRIVATE_KEY=votre_cle_privee
   HEDERA_TOPIC_ID=votre_topic_id
   SECRET_KEY=votre_secret_key_django
   DEBUG=True
   ```

4. **Lancer les migrations**
   ```bash
   python manage.py migrate
   ```

5. **Démarrer le serveur**
   ```bash
   python manage.py runserver
   ```

## 🤝 Contribution
Les contributions sont les bienvenues .

## P.S
Ce projet n’est pas encore terminé.
