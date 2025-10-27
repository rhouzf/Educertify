from django.shortcuts import render

def verifier_diplome(request):
    """
    Vue pour afficher la page de vérification des diplômes
    """
    return render(request, 'verifier.html')
