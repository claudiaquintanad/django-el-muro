from django.contrib import messages
from django.shortcuts import redirect, render
import bcrypt
from .decorators import login_required,admin_requerido
from app.models import User, Message, Comment
from time import strftime, localtime

@login_required
def index(request):
    context = {'mens' : Message.objects.all(),
            'comen': Comment.objects.all(),
            'usuarios': User.objects.all(),
            'tiempo': strftime(" %H:%M ", localtime())
    }
    print(context)
    return render(request, 'index.html', context)

@admin_requerido
def administrador(request):

    context = {
        'saludo': 'ADMINISTRADOR'
    }
    return render(request, 'admin.html', context)

def postmessage(request):
    mensajes = Message.objects.create(message=request.POST['mensaje'], 
                user_id= User.objects.get(id=request.session['usuario']['id']))
    return redirect("/")

def postcomment(request):
    print(request.session['usuario']['id'])
    comentarios = Comment.objects.create(comment= request.POST['comentario'],
                user_id = User.objects.get(id=request.session['usuario']['id']),
                message_id = Message.objects.get(id=request.POST['message_id']))
    return redirect("/")

def borrar(request, id):
    d = Comment.objects.get(id=id)
    d.delete()
    messages.success(request,"Your comment has been successfully deleted")
    return redirect("/")

"""en def post:  todo lo que está dentro del create message, id, user_id debe ser IGUAL al models """