from django.db import models

# Create your models here.
# core/models.py

class OrdenRetiro(models.Model):

    ESTADO_PENDIENTE = 'pendiente'
    ESTADO_EN_PROCESO = 'en_proceso'
    ESTADO_COMPLETADO = 'completado'

    ESTADO_CHOICES = [
        (ESTADO_PENDIENTE, 'Pendiente'),
        (ESTADO_EN_PROCESO, 'En proceso'),
        (ESTADO_COMPLETADO, 'Completado'),
    ]

    solicitante = models.CharField(
        max_length=150,
        help_text="Nombre de la persona o empresa que solicita el retiro"
    )
    referencia_interna = models.CharField(
        max_length=50,
        unique=True,
        help_text="Código interno para identificar la orden"
    )
    tipo_servicio = models.CharField(
        max_length=100,
        help_text="Tipo de servicio requerido (ej: retiro estándar, urgente, refrigerado)"
    )
    cantidad_bultos = models.PositiveIntegerField(
        help_text="Cantidad de bultos a retirar"
    )
    observaciones = models.TextField(
        blank=True,
        help_text="Observaciones libres sobre el pedido"
    )
    estado = models.CharField(
        max_length=20,
        choices=ESTADO_CHOICES,
        default=ESTADO_PENDIENTE,
    )
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.referencia_interna} - {self.solicitante} ({self.estado})"