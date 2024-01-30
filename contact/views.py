from django.shortcuts import render
from datetime import datetime

from .utils import send_email_with_html_body
# Create your views here.

def create_view(request, *args, **kwargs):
    """this view help to create and account for testing sending emails"""
    cxt = {}
    if request.method == "POST":
        email = request.POST.get('email')
        username = request.POST.get('username')
        entreprise = request.POST.get('entreprise')
        telephone = request.POST.get('telephone')
        content = request.POST.get('content')
        subjet = "contact d'un utilisateur"
        templates = 'email.html'
        context = {
            'date': datetime.today().date(),
            'entreprise':entreprise,
            'telephone':telephone,
            'username':username,
            'content':content,
            'email':email,
            'confirmation':'vous avez envoye un email à',
        }
        receivers = [email]
        has_send = send_email_with_html_body(
            subject=subjet,
            receivers=receivers,
            template=templates,
            context=context)
        if has_send:
            cxt ={"msg":"mail envoyee avec success."}
        else:
            cxt = {"msg":"mail non envoyee.Echouer"}
        print(has_send)
    return render(request,'index.html',cxt)