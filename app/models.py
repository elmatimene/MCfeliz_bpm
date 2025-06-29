from django.db import models

# Create your models here.

class reserva(models.Model):
    estados= [
        ('adopatado', 'adopcion'),
        ('foster', 'temporal'),
        ('transfer', 'traslado'),
        ('medical', 'medico'),
    ]

    motivos =[
        ('peluqueria', 'peluqueria'),
        ('vacuna', 'vacuna'),
        ('atencion medica', 'atencion medica'),
    ]

    nombre_dueño = models.CharField(max_length=100)
    correo = models.EmailField(blank=True, null=True)
    direccion = models.TextField()
    nombre_mascota = models.CharField(max_length=100)
    raza = models.CharField(max_length=100, blank=True)
    fecha_reserva = models.DateField()
    estado = models.CharField(max_length=50)
    motivo = models.CharField(max_length=50, choices=motivos, null=True)
    
    def __str__(self):
        return f"{self.nombre_mascota} - {self.fecha_reserva}"
