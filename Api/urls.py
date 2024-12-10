from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import generate_response
from . import views
from .views import ProtectedView
from rest_framework_simplejwt.views import(
    TokenObtainPairView,
    TokenRefreshView,
)

# Crear un router para registrar los viewsets
router = DefaultRouter()
router.register(r'auditlog', views.AuditLogViewSet)
router.register(r'roles', views.RoleViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'compradores', views.CompradorViewSet)
router.register(r'carritos', views.CarritoViewSet)
router.register(r'categorias', views.CategoriaViewSet)
router.register(r'proveedores', views.ProveedorViewSet)
router.register(r'productos', views.ProductoViewSet)
router.register(r'carritoproductos', views.CarritoProductoViewSet)
router.register(r'metodospago', views.MetodoPagoViewSet)
router.register(r'ventas', views.VentaViewSet)
router.register(r'detalleventas', views.DetalleVentaViewSet)
router.register(r'facturas', views.FacturaViewSet)
router.register(r'passwordresettoken', views.PasswordResetTokenViewSet)


urlpatterns = [
    path('', include(router.urls)),  
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/protected/', ProtectedView.as_view(), name='protected'),
    path('api/generate-response/', generate_response, name='generate_response')
]
