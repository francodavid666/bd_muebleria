from django.shortcuts import render,redirect

from .models import *
from bd_app.forms import *
from django import forms
from django.db.models import Q
# Create your views here.


def inicio (request):
    queryset = request.GET.get('buscar')
    queryset2 = request.GET.get('direccion')
      
 
    
    clientes = datos_propiedad_model.objects.all()
    
    if queryset: 
        clientes= datos_propiedad_model.objects.filter(dueño = True)
        clientes= datos_propiedad_model.objects.filter(
          Q(tipo__icontains = queryset) |
          Q(direccion__icontains = queryset) |
          Q(localidad__icontains = queryset) |
          Q(propiedad__icontains = queryset) |
          Q(estado__icontains = queryset) |
          Q(tipo__icontains = queryset) |
          Q(precio__icontains = queryset) |
          Q(tipo__icontains = queryset) |
          Q(dueño__icontains = queryset)
        ).distinct()
    elif queryset2:
      clientes =  datos_propiedad_model.objects.all().order_by('-dueño')
      print('entra')
    

        
        
   
      
        
    #form = dueño_model.objects.all()
    #form2 = datos_propiedad_model.objects.all()
    return render (request,'bd_app/inicio.html',{'clientes':clientes})

#DUEÑO
#DUEÑO
#DUEÑO
#DUEÑO



#DUEÑO DE A Z
def dueño_az (request):
  
  
  
      queryset = request.GET.get('buscar')
     
  
      clientes= datos_propiedad_model.objects.all().order_by('dueño')
    
      if queryset: 
          clientes= datos_propiedad_model.objects.filter(dueño = True)
          clientes= datos_propiedad_model.objects.filter(
            Q(dueño__icontains = queryset) 
            ).distinct().order_by('dueño')
      return render (request,'bd_app/filtros/dueño/dueño_az.html',{'clientes':clientes})




#DUEÑO DE Z A
def dueño_za (request):
  
  
  
      queryset = request.GET.get('buscar')
     
  
      clientes= datos_propiedad_model.objects.all().order_by('-dueño')
    
      if queryset: 
          clientes= datos_propiedad_model.objects.filter(dueño = True)
          clientes= datos_propiedad_model.objects.filter(
            Q(dueño__icontains = queryset) 
            ).distinct().order_by('-dueño')
      return render (request,'bd_app/filtros/dueño/dueño_za.html',{'clientes':clientes})


#DUEÑO
#DUEÑO
#DUEÑO
#DUEÑO





#DIRECCION 
#DIRECCION 
#DIRECCION 
#DIRECCION 



#DIRECCION DE A Z
def direccion_az (request):
  
  
  
      queryset = request.GET.get('buscar')
     
  
      clientes= datos_propiedad_model.objects.all().order_by('direccion')
    
      if queryset: 
          clientes= datos_propiedad_model.objects.filter(direccion = True)
          clientes= datos_propiedad_model.objects.filter(
            Q(direccion__icontains = queryset) 
            ).distinct().order_by('direccion')
      return render (request,'bd_app/filtros/direccion/direccion_az.html',{'clientes':clientes})
  
  


#DIRECCION DE Z A
def direccion_za (request):
  
  
  
      queryset = request.GET.get('buscar')
     
  
      clientes= datos_propiedad_model.objects.all().order_by('-direccion')
    
      if queryset: 
          clientes= datos_propiedad_model.objects.filter(direccion = True)
          clientes= datos_propiedad_model.objects.filter(
            Q(direccion__icontains = queryset) 
            ).distinct().order_by('-direccion')
      return render (request,'bd_app/filtros/direccion/direccion_za.html',{'clientes':clientes})
    
    
  
#DIRECCION 
#DIRECCION 
#DIRECCION 
#DIRECCION 



#LOCALIDAD
#LOCALIDAD
#LOCALIDAD
#LOCALIDAD


#DIRECCION DE A Z
def localidad_az (request):
  
  
  
      queryset = request.GET.get('buscar')
     
  
      clientes= datos_propiedad_model.objects.all().order_by('localidad')
    
      if queryset: 
          clientes= datos_propiedad_model.objects.filter(localidad = True)
          clientes= datos_propiedad_model.objects.filter(
            Q(localidad__icontains = queryset) 
            ).distinct().order_by('localidad')
      return render (request,'bd_app/filtros/localidad/localidad_az.html',{'clientes':clientes})
  
  


#LOCALIDAD DE Z A
def localidad_za (request):
  
  
  
      queryset = request.GET.get('buscar')
     
  
      clientes= datos_propiedad_model.objects.all().order_by('-localidad')
    
      if queryset: 
          clientes= datos_propiedad_model.objects.filter(localidad = True)
          clientes= datos_propiedad_model.objects.filter(
            Q(localidad__icontains = queryset) 
            ).distinct().order_by('-localidad')
      return render (request,'bd_app/filtros/localidad/localidad_za.html',{'clientes':clientes})
    
    



#LOCALIDAD
#LOCALIDAD
#LOCALIDAD
#LOCALIDAD


#ESTADO
#ESTADO
#ESTADO
#ESTADO

#ESTADO DE A Z
def estado_az (request):
  
  
  
      queryset = request.GET.get('buscar')
     
  
      clientes= datos_propiedad_model.objects.all().order_by('estado')
    
      if queryset: 
          clientes= datos_propiedad_model.objects.filter(estado = True)
          clientes= datos_propiedad_model.objects.filter(
            Q(estado__icontains = queryset) 
            ).distinct().order_by('estado')
      return render (request,'bd_app/filtros/estado/estado_az.html',{'clientes':clientes})
  
  


#ESTADO DE Z A
def estado_za (request):
  
  
  
      queryset = request.GET.get('buscar')
     
  
      clientes= datos_propiedad_model.objects.all().order_by('-estado')
    
      if queryset: 
          clientes= datos_propiedad_model.objects.filter(estado = True)
          clientes= datos_propiedad_model.objects.filter(
            Q(estado__icontains = queryset) 
            ).distinct().order_by('-estado')
      return render (request,'bd_app/filtros/estado/estado_za.html',{'clientes':clientes})
    


#ESTADO
#ESTADO
#ESTADO
#ESTADO

#PROPIEDAD
#PROPIEDAD
#PROPIEDAD
#PROPIEDAD

#PROPIEDAD DE A Z
def propiedad_az (request):
  
  
  
      queryset = request.GET.get('buscar')
     
  
      clientes= datos_propiedad_model.objects.all().order_by('propiedad')
    
      if queryset: 
          clientes= datos_propiedad_model.objects.filter(propiedad = True)
          clientes= datos_propiedad_model.objects.filter(
            Q(propiedad__icontains = queryset) 
            ).distinct().order_by('propiedad')
      return render (request,'bd_app/filtros/propiedad/propiedad_az.html',{'clientes':clientes})
  
  


#PROPIEDAD DE Z A
def propiedad_za (request):
  
  
  
      queryset = request.GET.get('buscar')
     
  
      clientes= datos_propiedad_model.objects.all().order_by('-propiedad')
    
      if queryset: 
          clientes= datos_propiedad_model.objects.filter(propiedad = True)
          clientes= datos_propiedad_model.objects.filter(
            Q(propiedad__icontains = queryset) 
            ).distinct().order_by('-propiedad')
      return render (request,'bd_app/filtros/propiedad/propiedad_za.html',{'clientes':clientes})

#PROPIEDAD
#PROPIEDAD
#PROPIEDAD
#PROPIEDAD




#TIPO
#TIPO
#TIPO
#TIPO

#TIPO DE A Z
def tipo_az (request):
  
  
  
      queryset = request.GET.get('buscar')
     
  
      clientes= datos_propiedad_model.objects.all().order_by('tipo')
    
      if queryset: 
          clientes= datos_propiedad_model.objects.filter(tipo = True)
          clientes= datos_propiedad_model.objects.filter(
            Q(tipo__icontains = queryset) 
            ).distinct().order_by('tipo')
      return render (request,'bd_app/filtros/tipo/tipo_az.html',{'clientes':clientes})
  
  


#TIPO DE Z A
def tipo_za (request):
  
  
  
      queryset = request.GET.get('buscar')
     
  
      clientes= datos_propiedad_model.objects.all().order_by('-tipo')
    
      if queryset: 
          clientes= datos_propiedad_model.objects.filter(tipo = True)
          clientes= datos_propiedad_model.objects.filter(
            Q(tipo__icontains = queryset) 
            ).distinct().order_by('-tipo')
      return render (request,'bd_app/filtros/tipo/tipo_za.html',{'clientes':clientes})
#TIPO
#TIPO
#TIPO
#TIPO


#PRECIO
#PRECIO
#PRECIO
#PRECIO

#PRECIO DE A Z
def precio_az (request):
  
  
  
      queryset = request.GET.get('buscar')
     
  
      clientes= datos_propiedad_model.objects.all().order_by('precio')
    
      if queryset: 
          clientes= datos_propiedad_model.objects.filter(precio = True)
          clientes= datos_propiedad_model.objects.filter(
            Q(precio__icontains = queryset) 
            ).distinct().order_by('precio')
      return render (request,'bd_app/filtros/precio/precio_az.html',{'clientes':clientes})
  
  


#PRECIO DE Z A
def precio_za (request):
  
  
  
      queryset = request.GET.get('buscar')
     
  
      clientes= datos_propiedad_model.objects.all().order_by('-precio')
    
      if queryset: 
          clientes= datos_propiedad_model.objects.filter(precio = True)
          clientes= datos_propiedad_model.objects.filter(
            Q(precio__icontains = queryset) 
            ).distinct().order_by('-precio')
      return render (request,'bd_app/filtros/precio/precio_za.html',{'clientes':clientes})

#PRECIO
#PRECIO
#PRECIO
#PRECIO

#DESCRIPCION
#DESCRIPCION
#DESCRIPCION
#DESCRIPCION

#DESCRIPCION DE A Z
def descripcion_az (request):
  
  
  
      queryset = request.GET.get('buscar')
     
  
      clientes= datos_propiedad_model.objects.all().order_by('descripcion')
    
      if queryset: 
          clientes= datos_propiedad_model.objects.filter(descripcion = True)
          clientes= datos_propiedad_model.objects.filter(
            Q(descripcion__icontains = queryset) 
            ).distinct().order_by('descripcion')
      return render (request,'bd_app/filtros/descripcion/descripcion_az.html',{'clientes':clientes})
  
  


#DESCRIPCION DE Z A
def descripcion_za (request):
  
  
  
      queryset = request.GET.get('buscar')
     
  
      clientes= datos_propiedad_model.objects.all().order_by('-descripcion')
    
      if queryset: 
          clientes= datos_propiedad_model.objects.filter(descripcion = True)
          clientes= datos_propiedad_model.objects.filter(
            Q(descripcion__icontains = queryset) 
            ).distinct().order_by('-descripcion')
      return render (request,'bd_app/filtros/descripcion/descripcion_za.html',{'clientes':clientes})

#DESCRIPCION
#DESCRIPCION
#DESCRIPCION
#DESCRIPCION

























def inicio_caracteristicas(request):
  
      queryset = request.GET.get('buscar')
      if queryset: 
          clientes= datos_propiedad_model.objects.filter(dueño = True)
          clientes= datos_propiedad_model.objects.filter(
            Q(tipo__icontains = queryset) |
            Q(direccion__icontains = queryset) |
            Q(localidad__icontains = queryset) |
            Q(propiedad__icontains = queryset) |
            Q(estado__icontains = queryset) |
            Q(tipo__icontains = queryset) |
            Q(precio__icontains = queryset) |
            Q(tipo__icontains = queryset) |
            Q(dueño__icontains = queryset)
          ).distinct()
  
  
      clientes = datos_propiedad_model.objects.all()
      return render (request,'bd_app/filtros/inicio_caracteristicas.html',{'clientes':clientes})

def inicio_refresh(request):
  
      clientes = datos_propiedad_model.objects.all()
      return render (request,'bd_app/botones_header/inicio_refresh.html',{'clientes':clientes})
    
   
   
   
   
   
#PROPIEDADES    
#PROPIEDADES    
#PROPIEDADES    
#PROPIEDADES    
    
    
    
    
    
    
    
def inicio_propiedades(request):
  
      queryset = request.GET.get('buscar')
      if queryset: 
          clientes= datos_propiedad_model.objects.filter(dueño = True)
          clientes= datos_propiedad_model.objects.filter(
            Q(tipo__icontains = queryset) |
            Q(direccion__icontains = queryset) |
            Q(localidad__icontains = queryset) |
            Q(propiedad__icontains = queryset) |
            Q(estado__icontains = queryset) |
            Q(tipo__icontains = queryset) |
            Q(precio__icontains = queryset) |
            Q(tipo__icontains = queryset)
          ).distinct()
  
  
      clientes = datos_propiedad_model.objects.all()
      return render (request,'bd_app/filtros/propiedades/inicio_propiedades.html',{'clientes':clientes})
    
    
    
def propiedades_za(request):
  
      queryset = request.GET.get('buscar')
      
      
      clientes = datos_propiedad_model.objects.all().order_by('-propiedad')
      if queryset: 
          clientes= datos_propiedad_model.objects.filter(dueño = True)
          clientes= datos_propiedad_model.objects.filter(
            Q(tipo__icontains = queryset) |
            Q(direccion__icontains = queryset) |
            Q(localidad__icontains = queryset) |
            Q(propiedad__icontains = queryset) |
            Q(estado__icontains = queryset) |
            Q(tipo__icontains = queryset) |
            Q(precio__icontains = queryset) |
            Q(tipo__icontains = queryset) |
            Q(dueño__icontains = queryset)
            ).distinct().order_by('-propiedad')
  
  
      
      return render (request,'bd_app/filtros/propiedades/propiedades_za.html',{'clientes':clientes})    
    
    
    
def inicio_mascaro (request):
  
      queryset = request.GET.get('buscar')
 

  
      clientes = datos_propiedad_model.objects.all().order_by('precio')
    
      if queryset: 
          clientes= datos_propiedad_model.objects.filter(dueño = True)
          clientes= datos_propiedad_model.objects.filter(
            Q(tipo__icontains = queryset) |
            Q(direccion__icontains = queryset) |
            Q(localidad__icontains = queryset) |
            Q(propiedad__icontains = queryset) |
            Q(estado__icontains = queryset) |
            Q(tipo__icontains = queryset) |
            Q(precio__icontains = queryset) |
            Q(tipo__icontains = queryset) |
            Q(dueño__icontains = queryset)
          ).distinct()
  
    
  
      return render (request,'bd_app/filtros/propiedades/inicio_mascaro.html',{'clientes':clientes})

  
def inicio_masbarato (request):
 
      queryset = request.GET.get('buscar')

      clientes = datos_propiedad_model.objects.all().order_by('-precio')
    
      if queryset: 
          clientes= datos_propiedad_model.objects.filter(dueño = True)
          clientes= datos_propiedad_model.objects.filter(
            Q(tipo__icontains = queryset) |
            Q(direccion__icontains = queryset) |
            Q(localidad__icontains = queryset) |
            Q(propiedad__icontains = queryset) |
            Q(estado__icontains = queryset) |
            Q(tipo__icontains = queryset) |
            Q(precio__icontains = queryset) |
            Q(tipo__icontains = queryset) |
            Q(dueño__icontains = queryset)
          ).distinct()

      return render (request,'bd_app/filtros/propiedades/inicio_masbarato.html',{'clientes':clientes})

    
    
    

    

#PROPIEDADES    
#PROPIEDADES    
#PROPIEDADES    
#PROPIEDADES    



def form_edit(request,id):
  propiedad= datos_propiedad_model.objects.get(id=id)
  if request.method == 'POST':
    form = datos_propiedad_form(request.POST)
    if form.is_valid():
      info = form.cleaned_data
      propiedad.dueño=info['dueño']
      propiedad.tipo=info['tipo']
      propiedad.estado=info['estado']
      propiedad.direccion=info['direccion']
      propiedad.pais=info['pais']
      propiedad.provincia=info['provincia']
      propiedad.localidad=info['localidad']
      propiedad.parcela=info['parcela']
      propiedad.lote=info['lote']
      propiedad.tamaño=info['tamaño']
      propiedad.metros2=info['metros2']
      propiedad.clave_c=info['clave_c']
      propiedad.titular=info['titular']
      propiedad.propiedad=info['propiedad']
      propiedad.ambientes=info['ambientes']
      propiedad.baños=info['baños']
      propiedad.dormitorios=info['dormitorios']
      propiedad.cocina=info['cocina']
      propiedad.living=info['living']
      propiedad.comedor=info['comedor']
      propiedad.garage=info['garage']
      propiedad.sotano=info['sotano']
      propiedad.terrasa=info['terrasa']
      propiedad.descripcion=info['descripcion']
      propiedad.precio=info['precio']
      

      propiedad.save()
      clientes=datos_propiedad_model.objects.all()
      return render (request,'bd_app/inicio.html',{'clientes':clientes})
   
            #return redirect ('inicio')
          
          
  form= datos_propiedad_form(initial={'dueño':propiedad.dueño,
                                      'tipo': propiedad.tipo,
                                      'estado': propiedad.estado,
                                      'direccion': propiedad.direccion,
                                      'pais': propiedad.pais,
                                      'provincia' :propiedad.provincia,
                                      'localidad': propiedad.localidad,
                                      'parcela': propiedad.parcela,
                                      'lote': propiedad.lote,
                                      'tamaño' : propiedad.tamaño,
                                      'metros2' : propiedad.metros2,
                                      'clave_c' : propiedad.clave_c, 
                                      
                                      
                                      'titular':propiedad.titular,
                                      'propiedad' : propiedad.propiedad,
                                      'ambientes': propiedad.ambientes,
                                      'baños': propiedad.baños,
                                      'dormitorios' : propiedad.dormitorios,
                                      'cocina' : propiedad.cocina,
                                      'living' : propiedad.living,
                                      'comedor' : propiedad.comedor,
                                      'garage' : propiedad.garage,
                                      'sotano' : propiedad.sotano,
                                      'terrasa' : propiedad.terrasa,
                                      'descripcion' : propiedad.descripcion,
                                      'precio'  : propiedad.precio             
                                      })
      
  return render (request,'bd_app/form_edit.html',{'form':form,'id':id})
      
  

#delet borrar eliminar  delete
def delete(request,id):
  propiedades = datos_propiedad_model.objects.filter(id=id)
  if len(propiedades)!=0:
    propiedad = propiedades[0]
    propiedad.delete()
    
    
    clientes= datos_propiedad_model.objects.all()
    return render (request,'bd_app/inicio.html',{'clientes':clientes})
  
  
  
  
  #form_add
  
def form_add(request):
      if request.method=='POST':
                  formulario = datos_propiedad_form(request.POST)
                  if formulario.is_valid():
                        info=formulario.cleaned_data
                        dueño = info.get("dueño")
                        tipo = info.get("tipo")
                        estado=info.get('estado')
                        direccion=info.get('direccion')
                        descripcion= info.get("descripcion")
                        pais=info.get('pais')
                        provincia=info.get('provincia')
                        localidad=info.get('localidad')
                        parcela=info.get('parcela') 
                        lote=info.get('lote') 
                        tamaño=info.get('tamaño') 
                        metros2=info.get('metros2') 
                        clave_c=info.get('clave_c') 
                        titular=info.get('titular') 
                        propiedad=info.get('propiedad') 
                        ambientes=info.get('ambientes') 
                        baños=info.get('baños') 
                        dormitorios=info.get('dormitorios') 
                        cocina=info.get('cocina') 
                        living=info.get('living') 
                        comedor=info.get('comedor') 
                        garage=info.get('garage') 
                        sotano=info.get('sotano') 
                        terrasa=info.get('terrasa') 
                        descripcion=info.get('descripcion') 
                        precio=info.get('precio') 
                              
                              
                        home_1=datos_propiedad_model(
                              dueño=dueño,
                              tipo = tipo,
                              estado=estado,
                              direccion=direccion,
                              pais=pais,
                              provincia=provincia,
                              localidad=localidad,
                              parcela=parcela,
                              lote=lote,
                              tamaño=tamaño,
                              metros2=metros2,
                              clave_c=clave_c,
                              titular=titular,
                              propiedad=propiedad,
                              ambientes=ambientes,
                              baños=baños,
                              dormitorios=dormitorios,
                              cocina=cocina,
                              living=living,
                              comedor=comedor,
                              garage=garage,
                              sotano=sotano,
                              terrasa=terrasa,
                              descripcion=descripcion,
                              precio=precio,
                              )
                        home_1.save()
                        clientes= datos_propiedad_model.objects.all()
                        return render (request,'bd_app/inicio.html',{'clientes':clientes})

                        
                        
                        
      form= datos_propiedad_form()
      return render (request,'bd_app/form_add.html',{'form':form})

  
