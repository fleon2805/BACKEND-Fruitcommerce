from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from django.http import JsonResponse
import google.generativeai as genai
from datetime import datetime
from django.conf import settings
import requests
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import (
    AuditLog, Role, User, Comprador, Carrito, Categoria, Proveedor, Producto,
    CarritoProducto, MetodoPago, Venta, DetalleVenta, Factura, PasswordResetToken
)
from .serializers import (
    AuditLogSerializer, RoleSerializer, UserSerializer, CompradorSerializer,
    CarritoSerializer, CategoriaSerializer, ProveedorSerializer, ProductoSerializer,
    CarritoProductoSerializer, MetodoPagoSerializer, VentaSerializer, DetalleVentaSerializer,
    FacturaSerializer, PasswordResetTokenSerializer
)


@api_view(['POST'])
def generate_response(request):
    """
    Genera una respuesta basada en la pregunta recibida.
    """
    question = request.data.get('question')  # Obtenemos la pregunta del cuerpo de la solicitud
    
    # Verificamos que se haya enviado una pregunta
    if not question:
        return JsonResponse({'error': 'Pregunta no proporcionada'}, status=400)
    
    # Lógica para generar respuesta
    bot_response = ''
    
    # Respuestas predefinidas según las preguntas
    question = question.lower()  # Normalizar la pregunta en minúsculas para simplificar la comparación
    
    if 'donde queda santa anita' in question:
        bot_response = 'Santa Anita es un distrito ubicado en Lima, Perú.'
    elif 'que día es hoy' in question:
        today = datetime.now()
        bot_response = f'Hoy es {today.strftime("%d/%m/%Y")}.'
    elif 'hola' in question:
        bot_response = '¡Hola! ¿En qué puedo ayudarte?'
    elif 'cuantas ventas se realizaron hoy' in question:
        bot_response = 'Hoy se realizaron 2 ventas.'
    elif 'cual fue la fruta que más se vendió' in question:
        bot_response = 'La fruta que más se vendió hoy fue el Plátano Isla.'
    elif 'cual es el precio del plátano' in question:
        bot_response = 'El precio del plátano por kg es $3.00.'
    elif 'cual es el precio de la manzana' in question:
        bot_response = 'El precio de la manzana por kg es $2.50.'
    elif 'cuantas manzanas se vendieron' in question:
        bot_response = 'Hoy se vendieron 120 manzanas.'
    elif 'que fruta es más cara' in question:
        bot_response = 'La fruta más cara que tenemos es la piña, con un precio de $5.00 por kg.'
    elif 'cuantas ventas se hicieron ayer' in question:
        bot_response = 'Ayer se realizaron 3 ventas.'
    elif 'cuantas ventas se han hecho esta semana' in question:
        bot_response = 'Esta semana se han realizado 15 ventas.'
    elif 'cuantas ventas se han hecho este mes' in question:
        bot_response = 'Este mes se han realizado 50 ventas.'
    elif 'cuanto vendí en total hoy' in question:
        bot_response = 'El total de ventas realizadas hoy es de $60.00.'
    elif 'cual es el precio del aguacate' in question:
        bot_response = 'El precio del aguacate por kg es $4.00.'
    elif 'cual es la fruta más vendida este mes' in question:
        bot_response = 'La fruta más vendida este mes ha sido la naranja.'
    elif 'cuantas naranjas se vendieron hoy' in question:
        bot_response = 'Hoy se vendieron 200 naranjas.'
    elif 'cual es el precio de la uva' in question:
        bot_response = 'El precio de la uva por kg es $6.00.'
    elif 'cuanto costó el total de ventas esta semana' in question:
        bot_response = 'El total de ventas esta semana fue de $850.00.'
    else:
        bot_response = 'Lo siento, no entendí esa pregunta. ¿Puedes formularla de otra manera?'
    
    # Devolvemos la respuesta
    return JsonResponse({'answer': bot_response})

class AuditLogViewSet(viewsets.ModelViewSet):
    queryset = AuditLog.objects.all()
    serializer_class = AuditLogSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


class CompradorViewSet(viewsets.ModelViewSet):
    queryset = Comprador.objects.all()
    serializer_class = CompradorSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


class CarritoViewSet(viewsets.ModelViewSet):
    queryset = Carrito.objects.all()
    serializer_class = CarritoSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


class ProveedorViewSet(viewsets.ModelViewSet):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


class CarritoProductoViewSet(viewsets.ModelViewSet):
    queryset = CarritoProducto.objects.all()
    serializer_class = CarritoProductoSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


class MetodoPagoViewSet(viewsets.ModelViewSet):
    queryset = MetodoPago.objects.all()
    serializer_class = MetodoPagoSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


class VentaViewSet(viewsets.ModelViewSet):
    queryset = Venta.objects.all()
    serializer_class = VentaSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


class DetalleVentaViewSet(viewsets.ModelViewSet):
    queryset = DetalleVenta.objects.all()
    serializer_class = DetalleVentaSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        venta_id = self.request.query_params.get('venta')
        if venta_id:
            return self.queryset.filter(venta_id=venta_id)
        return self.queryset


class FacturaViewSet(viewsets.ModelViewSet):
    queryset = Factura.objects.all()
    serializer_class = FacturaSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


class PasswordResetTokenViewSet(viewsets.ModelViewSet):
    queryset = PasswordResetToken.objects.all()
    serializer_class = PasswordResetTokenSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


class ProtectedView(APIView):
    permission_classes = [IsAuthenticated]  # Solo usuarios autenticados pueden acceder

    def get(self, request):
        # Aquí puedes retornar datos protegidos
        return Response({
            'message': 'Este es un endpoint protegido.',
            'user': request.user.username  # Información del usuario autenticado
        })