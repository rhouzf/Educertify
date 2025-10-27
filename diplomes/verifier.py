import requests
import base64
from django.conf import settings

def verifier_hash_hedera(hash_value):
    topic_id = settings.HEDERA_TOPIC_ID
    url = f"https://testnet.mirrornode.hedera.com/api/v1/topics/{topic_id}/messages?limit=100"
    
    try:
        response = requests.get(url)
        if response.status_code != 200:
            return {
                'success': False,
                'error': 'Impossible de contacter le Mirror Node',
                'hash': hash_value
            }

        messages = response.json().get("messages", [])
        all_hashes = []

        for msg in messages:
            try:
                decoded = base64.b64decode(msg["message"]).decode().strip()
                all_hashes.append(decoded)
            except Exception as e:
                print(f"Erreur lors du décodage d'un message: {str(e)}")
                continue

        print("Liste de tous les hashes décodés :", all_hashes)
        
        # Vérification
        valid = hash_value in all_hashes
        print(f"✅ Hash recherché '{hash_value}' trouvé : {valid}")
        
        if valid:
            print("🎯 DIPLÔME AUTHENTIFIÉ AVEC SUCCÈS !")
            return {
                'success': True,
                'message': 'Diplôme authentifié avec succès',
                'hash': hash_value,
                'found': True
            }
        else:
            print("❌ Diplôme non trouvé dans la blockchain")
            return {
                'success': False,
                'error': 'Diplôme non trouvé dans la blockchain',
                'hash': hash_value,
                'found': False
            }
            
    except Exception as e:
        return {
            'success': False,
            'error': f'Erreur lors de la vérification: {str(e)}',
            'hash': hash_value
        }