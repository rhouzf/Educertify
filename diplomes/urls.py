from django.urls import path
from . import api
from . import views

# URLs API (préfixées par /api/)
urlpatterns = [
    path('upload/', api.upload_diplome_api, name='upload_diplome'),
    path('verify/', api.verify_diplome_api, name='verify_diplome'),
]

# URLs des vues (sans préfixe)
urlpatterns_view = [
    path('verifier/', views.verifier_diplome, name='verifier_diplome'),
]