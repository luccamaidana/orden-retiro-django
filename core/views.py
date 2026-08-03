# core/views.py

from django.shortcuts import render
from .models import OrdenRetiro


def _validar_datos_orden(datos):
    """
    Verifica que los campos esenciales del pedido estén presentes.
    Devuelve una lista de errores (vacía si todo está OK).
    Esto es lógica de negocio, separada de la view y del template.
    """
    errores = []

    if not datos.get('solicitante', '').strip():
        errores.append('El solicitante es obligatorio.')

    if not datos.get('referencia_interna', '').strip():
        errores.append('La referencia interna es obligatoria.')

    if not datos.get('tipo_servicio', '').strip():
        errores.append('El tipo de servicio es obligatorio.')

    cantidad_bultos = datos.get('cantidad_bultos', '').strip()
    if not cantidad_bultos:
        errores.append('La cantidad de bultos es obligatoria.')
    elif not cantidad_bultos.isdigit() or int(cantidad_bultos) <= 0:
        errores.append('La cantidad de bultos debe ser un número entero mayor a 0.')

    return errores


def crear_orden_retiro(request):
    """
    GET  -> muestra el formulario vacío, no persiste nada.
    POST -> valida los datos y, si son válidos, crea la orden.
    """

    if request.method == 'POST':
        datos = {
            'solicitante': request.POST.get('solicitante', ''),
            'referencia_interna': request.POST.get('referencia_interna', ''),
            'tipo_servicio': request.POST.get('tipo_servicio', ''),
            'cantidad_bultos': request.POST.get('cantidad_bultos', ''),
            'observaciones': request.POST.get('observaciones', ''),
        }

        errores = _validar_datos_orden(datos)

        if errores:
            contexto = {
                'errores': errores,
                'datos': datos,  # para repoblar el formulario con lo ya tipeado
            }
            return render(request, 'core/form_orden.html', contexto)

        orden = OrdenRetiro.objects.create(
            solicitante=datos['solicitante'].strip(),
            referencia_interna=datos['referencia_interna'].strip(),
            tipo_servicio=datos['tipo_servicio'].strip(),
            cantidad_bultos=int(datos['cantidad_bultos']),
            observaciones=datos['observaciones'].strip(),
            estado=OrdenRetiro.ESTADO_PENDIENTE,
        )

        contexto = {'orden': orden}
        return render(request, 'core/confirmacion_orden.html', contexto)

    # request.method == 'GET'
    contexto = {}
    return render(request, 'core/form_orden.html', contexto)