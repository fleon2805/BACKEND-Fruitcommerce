from django.db import models


class AuditLog(models.Model):
    action = models.CharField(max_length=255, null=True, blank=True)
    note_content = models.CharField(max_length=255, null=True, blank=True)
    note_id = models.BigIntegerField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    username = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'audit_log'  

    def __str__(self):
        return f"Audit Log {self.id} - Action: {self.action}"
    

class Role(models.Model):
    ROLE_CHOICES = [
        ('ROLE_ADMIN', 'Admin'),
        ('ROLE_CLIENTE', 'Cliente'),
        ('ROLE_PRODUCTOR', 'Productor'),
        ('ROLE_USER', 'User'),
    ]
    
    role_name = models.CharField(
        max_length=50, 
        choices=ROLE_CHOICES, 
        null=True, 
        blank=True
    )

    class Meta:
        db_table = 'roles' 
    
    def __str__(self):
        return self.role_name 


class User(models.Model):
    role = models.ForeignKey(Role, null=True, blank=True, on_delete=models.SET_NULL)
    account_expiry_date = models.DateField(null=True, blank=True)
    account_non_expired = models.BooleanField(default=True)
    account_non_locked = models.BooleanField(default=True)
    created_date = models.DateTimeField(null=True, blank=True)
    credentials_expiry_date = models.DateField(null=True, blank=True)
    credentials_non_expired = models.BooleanField(default=True)
    email = models.EmailField(max_length=50, unique=True)
    enabled = models.BooleanField(default=True)
    is_two_factor_enabled = models.BooleanField(default=False)
    password = models.CharField(max_length=120, null=True, blank=True)
    sign_up_method = models.CharField(max_length=255, null=True, blank=True)
    two_factor_secret = models.CharField(max_length=255, null=True, blank=True)
    updated_date = models.DateTimeField(null=True, blank=True)
    username = models.CharField(max_length=20, unique=True)

    class Meta:
        db_table = 'users'  
        
class Comprador(models.Model):
    apellidos = models.CharField(max_length=255, null=True, blank=True)
    direccion = models.CharField(max_length=255, null=True, blank=True)
    dni = models.CharField(max_length=255, null=True, blank=True)
    nombres = models.CharField(max_length=255, null=True, blank=True)
    ruc = models.CharField(max_length=255, null=True, blank=True)
    telefono = models.CharField(max_length=255, null=True, blank=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='compradores')

    class Meta:
        db_table = 'comprador'  
        unique_together = ('usuario',)  

class Carrito(models.Model):
    fecha_creacion = models.CharField(max_length=255, null=True, blank=True)
    comprador = models.ForeignKey(
        Comprador, 
        null=True, 
        blank=True, 
        on_delete=models.SET_NULL
    )
    
    class Meta:
        db_table = 'carrito'  
        
class Categoria(models.Model):
    categoria = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'categoria'  
        
class Proveedor(models.Model):
    direccion = models.CharField(max_length=255, null=True, blank=True)
    horarios_atencion = models.CharField(max_length=255, null=True, blank=True)
    nombre_empresa = models.CharField(max_length=255, null=True, blank=True)
    ruc = models.CharField(max_length=255, null=True, blank=True)
    telefono = models.CharField(max_length=255, null=True, blank=True)
    ubicacion = models.CharField(max_length=255, null=True, blank=True)
    usuario_id = models.ForeignKey(User,on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'proveedor'  
        
class Producto(models.Model):
    nombre = models.CharField(max_length=255, null=True, blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    foto = models.CharField(max_length=255, null=True, blank=True)
    stock = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    activo = models.BooleanField(default=True)
    categoria_id = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    proveedor_id = models.ForeignKey(Proveedor, on_delete=models.CASCADE)

    class Meta:
        db_table = 'producto'
    
class CarritoProducto(models.Model):
    cantidad = models.CharField(max_length=255, null=True, blank=True)
    carrito = models.ForeignKey(
        Carrito, 
        on_delete=models.CASCADE,  
    )
    producto = models.ForeignKey(
        Producto, 
        on_delete=models.CASCADE,  
    )
    
    class Meta:
        db_table = 'carrito_producto'  
    
class MetodoPago(models.Model):
    metodo = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'metodos_pago'  
        
class Venta(models.Model):
    fecha_venta = models.CharField(max_length=255, null=True, blank=True)
    numero_venta = models.CharField(max_length=255, null=True, blank=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    comprador = models.ForeignKey(
        Comprador, 
        null=True, 
        blank=True, 
        on_delete=models.SET_NULL  
    )
    metodo_pago = models.ForeignKey(
        MetodoPago, 
        null=True, 
        blank=True, 
        on_delete=models.SET_NULL   
    )

    class Meta:
        db_table = 'venta'  

class DetalleVenta(models.Model):
    cantidad = models.CharField(max_length=255, null=True, blank=True)
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    
    producto = models.ForeignKey(
        Producto,
        null=True,
        blank=True,
        on_delete=models.SET_NULL  
    )
    venta = models.ForeignKey(
        Venta,
        null=True,
        blank=True,
        on_delete=models.SET_NULL  
    )

    class Meta:
        db_table = 'detalle_venta'  
        
class Factura(models.Model):
    fecha_emision = models.CharField(max_length=255, null=True, blank=True)
    monto_total = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    numero_factura = models.CharField(max_length=255, null=True, blank=True)
    venta = models.ForeignKey(
        Venta, 
        on_delete=models.SET_NULL,  
        null=True, 
        blank=True
    )
    
    class Meta:
        db_table = 'factura'  
        
class PasswordResetToken(models.Model):
    expiry_date = models.DateTimeField(null=False, blank=False)
    token = models.CharField(max_length=255, unique=True) 
    used = models.BooleanField(default=False)
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE  
    )
    
    class Meta:
        db_table = 'password_reset_token'  