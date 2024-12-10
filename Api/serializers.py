from rest_framework import serializers
from .models import (
    AuditLog, Role, User, Comprador, Carrito, Categoria, Proveedor, Producto,
    CarritoProducto, MetodoPago, Venta, DetalleVenta, Factura, PasswordResetToken
)


class AuditLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuditLog
        fields = '__all__'


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class CompradorSerializer(serializers.ModelSerializer):
    usuario = UserSerializer(read_only=True)

    class Meta:
        model = Comprador
        fields = '__all__'


class CarritoSerializer(serializers.ModelSerializer):
    comprador = CompradorSerializer(read_only=True)

    class Meta:
        model = Carrito
        fields = '__all__'


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'


class ProveedorSerializer(serializers.ModelSerializer):
    usuario = UserSerializer(read_only=True)

    class Meta:
        model = Proveedor
        fields = '__all__'


class ProductoSerializer(serializers.ModelSerializer):
    categoria = CategoriaSerializer(read_only=True)
    proveedor = ProveedorSerializer(read_only=True)

    class Meta:
        model = Producto
        fields = '__all__'


class CarritoProductoSerializer(serializers.ModelSerializer):
    carrito = CarritoSerializer(read_only=True)
    producto = ProductoSerializer(read_only=True)

    class Meta:
        model = CarritoProducto
        fields = '__all__'


class MetodoPagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetodoPago
        fields = '__all__'


class VentaSerializer(serializers.ModelSerializer):
    comprador = CompradorSerializer(read_only=True)
    metodo_pago = MetodoPagoSerializer(read_only=True)

    class Meta:
        model = Venta
        fields = '__all__'


class DetalleVentaSerializer(serializers.ModelSerializer):
    producto = ProductoSerializer(read_only=True)
    venta = VentaSerializer(read_only=True)

    class Meta:
        model = DetalleVenta
        fields = '__all__'


class FacturaSerializer(serializers.ModelSerializer):
    venta = VentaSerializer(read_only=True)

    class Meta:
        model = Factura
        fields = '__all__'


class PasswordResetTokenSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = PasswordResetToken
        fields = '__all__'