from rest_framework import serializers
from .models import Blog

class BlogSerializer(serializers.ModelSerializer):

    # validacion
    titulo = serializers.CharField(
        required=True, 
        min_length=5, 
        error_messages={
            'required': 'El título es obligatorio.',
            'min_length': 'El título debe tener al menos 5 caracteres.'
        }
    )

    contenido = serializers.CharField(
        required=True, 
        min_length=10, 
        error_messages={
            'required': 'El contenido es obligatorio.',
            'min_length': 'El contenido debe tener al menos 10 caracteres.'
        }
    )

    class Meta:
        model=Blog
        fields = '__all__'