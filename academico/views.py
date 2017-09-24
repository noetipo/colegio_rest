from django.shortcuts import render
from academico.models import * 
from rest_framework import serializers, viewsets
class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = '__all__'
class PersonaViewSet(viewsets.ModelViewSet):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer



class PeriodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Periodo
        fields = '__all__'
class PeriodoViewSet(viewsets.ModelViewSet):
    queryset = Periodo.objects.all()
    serializer_class = PeriodoSerializer



class MateriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Materia
        fields = '__all__'
class MateriaViewSet(viewsets.ModelViewSet):
    queryset = Materia.objects.all()
    serializer_class = MateriaSerializer



class GradoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grado
        fields = '__all__'
class GradoViewSet(viewsets.ModelViewSet):
    queryset = Grado.objects.all()
    serializer_class = GradoSerializer




class SeccionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Seccion
        fields = '__all__'



class SeccionViewSet(viewsets.ModelViewSet):
    queryset = Seccion.objects.all()
    serializer_class = SeccionSerializer



class SeccionGetSerializer(serializers.ModelSerializer):
    grado =GradoSerializer() 
    periodo = PeriodoSerializer()
    class Meta:
        model = Seccion
        fields = '__all__'



class SeccionGetViewSet(viewsets.ModelViewSet):
    queryset = Seccion.objects.all()
    serializer_class = SeccionGetSerializer

class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        fields = '__all__'
class MatriculaViewSet(viewsets.ModelViewSet):
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer

class MatriculaGetSerializer(serializers.ModelSerializer):
    seccion=SeccionGetSerializer()
    persona=PersonaSerializer()
    class Meta:
        model = Matricula
        fields = '__all__'
class MatriculaGetViewSet(viewsets.ModelViewSet):
    queryset = Matricula.objects.all()
    serializer_class = MatriculaGetSerializer

# Create your views here.
