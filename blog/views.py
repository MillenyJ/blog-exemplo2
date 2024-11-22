from django.shortcuts import render , redirect , get_list_or_404 
from .models import Post,Blog,Mensagem

def index(request):
    context = {
        "posts": Post.objects.all() ,
        "blog": Blog.objects.first(),
    }
    return render(request, "index.html", context)

def post(request, post_id):
    context = {
        "post": Post.objects.get(pk=post_id),
        "blog": Blog.objects.first(),
    }
    return render(request, "post.html", context)
    
def about(request):
    context = {
        "blog": Blog.objects.first(),
    }
    return render(request, "about.html", context)

def contact(request): 
    context = {
        "blog": Blog.objects.first(),
    }



    if request.method == "POST":
        context["erro"]= {}
        if not request.POST['nome']:
            context['erro']['nome'] = True
        if not request.POST['email']:
            context['erro']['email'] = True
        if not request.POST['telefone']:
            context['erro']['telefone'] = True
        if not request.POST['cidade']:
            context['erro']['cidade'] = True
        if not request.POST['comentario']:
            context['erro']['comentario'] = True
        if context['erro']:
            return render(request,"contact.html", context)
            
        mensagem= Mensagem(nome= request.POST['nome'],
                           email= request.POST['email'],
                           telefone= request.POST['telefone'],
                           cidade= request.POST['cidade'],
                           comentario= request.POST['comentario'],)
        mensagem.save()
        
        return render(request, "contact.html", context)
    else:
        return render(request, "contact.html", context)
    
def mensagem(request):
    context = {
        "mensagens": Mensagem.objects.all(),
        "blog": Blog.objects.first(),
    }
    return render(request, "mensagem.html", context)

def editar_mensagem(request, mensagem_id):
    context = {
        "blog": Blog.objects.first(),
        "mensagem": Mensagem.objects.get(pk=mensagem_id),
        
    }
    if request.method == "POST":
        context["erro"]= {}
        if not request.POST['nome']:
            context['erro']['nome'] = True
        if not request.POST['email']:
            context['erro']['email'] = True
        if not request.POST['telefone']:
            context['erro']['telefone'] = True
        if not request.POST['cidade']:
            context['erro']['cidade'] = True
        if not request.POST['comentario']:
            context['erro']['comentario'] = True
        if context['erro']:
            return render(request,"edit_contact.html", context)
        
        mensagem = context ["mensagem"]
        mensagem.nome = request.POST['nome']
        mensagem.email = request.POST['email']
        mensagem.telefone = request.POST['telefone']
        mensagem.cidade = request.POST['cidade']
        mensagem.comentario = request.POST['comentario']
        mensagem.save()
        
    return render(request, "edit_contact.html", context)

def deletar_mensagem(request, mensagem_id):
    context = {
        "blog": Blog.objects.first(),
        "mensagem": get_list_or_404 (Mensagem ,pk=mensagem_id),
    }
    
    if request.method == "POST":
        context["mensagem"].delete()
        return redirect('mensagem')
    else:
        return render(request, "deletar_contact.html", context)
    
    
