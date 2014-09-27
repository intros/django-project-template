from django_mailbox.models import Mailbox

def save_mailbox(backend, user, response, *args,**kwargs):
    """
    saving the mailbox. 
    based on google oauth imap.
    """
    emails_response = response.get('emails', [])
    if len(emails_response) > 0:
        email = emails_response[0]['value']
    else:
        raise Exception("Email not found")

    imap_addrs = "gmail+ssl://%s:pass@imap.gmail.com" % email
    mailbox = Mailbox.objects.create(name=email, uri=imap_addrs)
    
    
