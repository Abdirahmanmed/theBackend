import logging
from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import send_mass_mail

logger = logging.getLogger(__name__)

def send_email_with_html_body(subject: str, receivers: list, template: str, context: dict):
    """Cette fonction aide à envoyer un courriel personnalisé à un utilisateur spécifique ou à un ensemble d'utilisateurs."""
    try:
        # Charger le corps du message HTML depuis le modèle
        html_message = render_to_string(template, context)
        # Envoyer un courriel de confirmation à l'expéditeur
        confirmation_message = render_to_string('confirmation.html', context)
        
        message1 = (
           subject,
           html_message,
           settings.EMAIL_HOST_USER,
           ['abdirahmanneymar3533@gmail.com'],#l'Email du recepteur des informations du contact envoyer par l'utlisateur 
          )
        message2 = (
          "Confirmation",
          confirmation_message,
          settings.EMAIL_HOST_USER,
          receivers,
          
          )
        send_mass_mail((message1,message2),fail_silently=False)



        return True
    except Exception as e:
        logger.error(e)
        return False
