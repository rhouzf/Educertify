from rest_framework.decorators import api_view
from rest_framework.response import Response
from .upload import publier_hash
from .verifier import verifier_hash_hedera
from rest_framework.decorators import parser_classes
from rest_framework.parsers import JSONParser

@api_view(['POST'])
def upload_diplome_api(request):
    pdf_file = request.FILES.get('file')
    if not pdf_file:
        return Response({"error": "Aucun fichier fourni"}, status=400)
    try:
        result = publier_hash(pdf_file)
        return Response(result)
    except Exception as e:
        return Response({"error": str(e)}, status=500)

@api_view(['POST'])
@parser_classes([JSONParser])
def verify_diplome_api(request):
    try:
        hash_value = request.data.get('hash')
        if not hash_value:
            return Response({"error": "Aucun hash fourni"}, status=400)
        
        result = verifier_hash_hedera(hash_value)
        return Response(result)
    except Exception as e:
        return Response({"error": str(e)}, status=500)
