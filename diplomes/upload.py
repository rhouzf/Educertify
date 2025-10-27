import os
import hashlib
from hedera import Client, PrivateKey, AccountId, TopicId, TopicMessageSubmitTransaction
from django.conf import settings

def publier_hash(pdf_file):
    # Lire le fichier PDF
    pdf_bytes = pdf_file.read()
    pdf_hash = hashlib.sha256(pdf_bytes).hexdigest()

    # Config Hedera depuis settings ou env
    client = Client.forTestnet()
    client.setOperator(
        AccountId.fromString(settings.HEDERA_ACCOUNT_ID),
        PrivateKey.fromString(settings.HEDERA_PRIVATE_KEY)
    )
    topic_id = TopicId.fromString(settings.HEDERA_TOPIC_ID)

    # Publier le hash sur Hedera
    tx = TopicMessageSubmitTransaction().setTopicId(topic_id).setMessage(pdf_hash)
    tx_response = tx.execute(client)
    receipt = tx_response.getReceipt(client)
    status = receipt.status
    tx_id = tx_response.transactionId.toString()

    return { "success": True,
            "hash": pdf_hash,
            "status": str(status),
            "transaction_id": tx_id,
            "message": "Diplôme publié avec succès sur la blockchain"}
