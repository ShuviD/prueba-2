"""from django.shortcuts import render
from django.http import HttpResponse
from .models import rucs

def mostrar_ruc(request, ruc):
    try:
        registro = rucs.objects.get(ruc=ruc)
        return render(request, 'detalle_ruc.html', {'registro': registro})
    except rucs.DoesNotExist:
        return HttpResponse('No se encontró el registro')"""
"""
import json
from django.http import HttpResponse, JsonResponse
from .models import rucs

def mostrar_ruc(request, ruc):
    try:
        registro = rucs.objects.get(ruc=ruc)
        data = {
            'ruc': registro.ruc,
            'razon_social': registro.razon_social,
            'estado_del_contribuyente': registro.estado_del_contribuyente,
            'condicion_de_domicilio': registro.condicion_de_domicilio,
            'ubigeo': registro.ubigeo,
            'tipo_via': registro.tipo_via,
            'nombre_via': registro.nombre_via,
            'codigo_zona': registro.codigo_zona,
            'tipo_zona': registro.tipo_zona,
            'numero': registro.numero,
            'interior': registro.interior,
            'lote': registro.lote,
            'departamento': registro.departamento,
            'manzana': registro.manzana,
            'kilometro': registro.kilometro,
        }
        return JsonResponse(data, safe=False)
    except rucs.DoesNotExist:
        return HttpResponse('No se encontró el registro')"""

from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import rucs

def mostrar_ruc(request, ruc):
    try:
        ruc_obj = rucs.objects.get(ruc=ruc)
    except rucs.DoesNotExist:
        return JsonResponse({'error': 'La RUC no fue encontrada'}, status=404)
    


    data = {
        'RUC': ruc_obj.ruc,
        'Razon_social': ruc_obj.razon_social if ruc_obj.razon_social != '-' else '',
        'Estado_del_contribuyente': ruc_obj.estado_del_contribuyente if ruc_obj.estado_del_contribuyente != '-' else '',
        'Condicion_de_domicilio': ruc_obj.condicion_de_domicilio if ruc_obj.condicion_de_domicilio != '-' else '',
        'Ubigeo': ruc_obj.ubigeo if ruc_obj.ubigeo != '-' else '',
        'Direccion': f"{ruc_obj.tipo_via} {ruc_obj.nombre_via} {ruc_obj.codigo_zona} {ruc_obj.tipo_zona} {ruc_obj.numero} {ruc_obj.interior} {ruc_obj.lote} {ruc_obj.departamento} {ruc_obj.manzana} {ruc_obj.kilometro}" if ruc_obj.tipo_via != '-' and ruc_obj.nombre_via != '-' else ''
    }
        
    return JsonResponse(data)



