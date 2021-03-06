from dataclasses import field
from pyexpat import model
from rest_framework.serializers import ModelSerializer

from core.models import Categoria, Livro, Editora, Autor

class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = "__all__"

class LivroSerializer(ModelSerializer):
    class Meta:
        model = Livro
        fields = "__all__"
        depth = 1

class EditoraSerializer(ModelSerializer):
    class Meta:
        model = Editora
        fields = "__all__"

class AutorSerializer(ModelSerializer):
    class Meta:
        model = Autor
        fields = "__all__"