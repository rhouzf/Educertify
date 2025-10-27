# Educertify - Système de Certification de Diplômes sur Blockchain

## 📋 Description
Educertify est une plateforme innovante qui utilise la technologie blockchain (Hedera Hashgraph) pour certifier et vérifier l'authenticité des diplômes universitaires. Cette solution permet aux établissements d'éducation d'émettre des diplômes numériques infalsifiables, tout en offrant aux étudiants un moyen simple et sécurisé de partager leurs certifications avec des employeurs ou d'autres institutions.

## ✨ Fonctionnalités Principales

### Pour les Établissements
- **Publication sécurisée** des diplômes sur la blockchain Hedera
- **Gestion simplifiée** des émissions de diplômes
- **Traçabilité complète** de chaque diplôme émis

### Pour les Étudiants
- **Accès permanent** à vos diplômes certifiés
- **Partage facile** avec les employeurs
- **Vérification instantanée** de l'authenticité

### Pour les Employeurs
- **Vérification en temps réel** de la validité des diplômes
- **Processus de recrutement** simplifié et sécurisé
- **Confiance accrue** dans les documents présentés

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

## 📚 Documentation API
L'API RESTful permet d'intégrer Educertify avec d'autres systèmes. Consultez la documentation complète dans le dossier `/docs`.

## 🤝 Contribution
Les contributions sont les bienvenues ! N'hésitez pas à ouvrir une issue ou à soumettre une pull request.

## 📄 Licence
Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.

## 📧 Contact
Pour toute question ou suggestion, contactez [votre-email@exemple.com](mailto:votre-email@exemple.com)
