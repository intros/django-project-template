from django_mailbox.models import Mailbox

def save_mailbox(backend, user, response, *args,**kwargs):
    """
    saving the mailbox. 
    based on google oauth imap.
    """
    emails_response = response.get('emails', [])

    #raise an exception if email not found in response from python.auth.
    if len(emails_response) > 0:
        email = emails_response[0]['value']
    else:
        raise Exception("Email not found")
    
    imap_addrs = "gmail+ssl://%s:pass@imap.gmail.com" % email
    
    current_mailbox_count = Mailbox.objects.filter(uri=imap_addrs).count()

    #do not create a mailbox if uril already exists.
    if current_mailbox_count == 0:
        mailbox = Mailbox.objects.create(name=email, uri=imap_addrs)
    
    
