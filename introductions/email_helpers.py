import re
from email.Header import decode_header
from email.utils import getaddresses

from django.core.validators import validate_email
from django.core.exceptions import ValidationError

def is_fwd(msg):
    if msg.get("subject").lstrip().rstrip().lower().startswith("fwd"):
        return True
    return False

def get_delivered_to(msg):
    return getaddresses(msg.get_all('delivered-to',[]))

def get_delivered_to_addr(msg):
    recipients = get_delivered_to(msg)
    return recipients[0][1].lower().lstrip().rstrip()

def get_from(msg):
    return getaddresses(msg.get_all('from',[]))

def get_from_addr(msg):
    recipients = get_from(msg)
    return recipients[0][1].lower().lstrip().rstrip()

def get_to_recipients(msg):
    return getaddresses(msg.get_all('to',[]))

def get_to_addrs(msg):
    return [y.lower().lstrip().rstrip() for x,y in get_to_recipients(msg)]

def get_cc_recipients(msg):
    return getaddresses(msg.get_all('cc',[]))

def get_cc_addrs(msg):
    return [y.lower().lstrip().rstrip() for x,y in get_cc_recipients(msg)]

def get_all_recipients(msg):
    tos = msg.get_all('to', [])
    ccs = msg.get_all('cc', [])
    resent_tos = msg.get_all('resent-to', [])
    resent_ccs = msg.get_all('resent-cc', [])
    return getaddresses(tos + ccs + resent_tos + resent_ccs)

def get_all_recipient_addrs(msg):
    recipients = get_all_recipients(msg)
    return [y.lower().lstrip().rstrip() for x,y in recipients]



def get_header(msg, header_name):
    header_content = decode_header(msg.get(header_name, ''))
    return_content = u''
    for line in header_content:
        str, enc = line
        if enc:
            content = str.decode(enc)
        else:
            content = str.encode('utf-8')
        return_content = u'%s%s' % (return_content, content)
    return return_content.lstrip().rstrip().replace('\n','')

def isolate_email(address):
    """Apply several regular expressions to detect
    common email addresses and
    return the isolated address
    """
    matches = [
        "(?P<name>[^<].*)<(?P<email>.*)>",
        "<(?P<email>.*)>",
        "(?P<email>.*)",
        "(?P<name>[^<].*?)<(?P<email>[^<].*?)<mailto.*",
        "[<(](?P<email>.*[^<])<mailto:.*",
    ]
    for regex in matches:
        #print "checking %s with %s" % (address, regex)
        m = re.match(r"%s" % regex, address)
        if m:
            likely_addr = m.group('email').lstrip().rstrip()
            if len(likely_addr.lstrip().rstrip()) > 0:
                try:
                    validate_email(likely_addr)
                    return likely_addr
                except ValidationError:
                    pass
                    #print "Couldn't validate %s" % likely_addr
    return ''
    #return None

def isolate_email_list(field):
        some = [isolate_email(x).lstrip().rstrip() for x in field.split(',') if x != '']
        more = [isolate_email(x).lstrip().rstrip() for x in field.split(' ') if x.find('@') > 0]
        return [x for x in set(some).union(set(more)) if x !='']

def isolate_name(address):
    m = re.match("(?P<name>[^<].*)<(?P<email>.*)>", address)
    if m:
        return m.group('name').lstrip().rstrip().lstrip('"').rstrip('"')
    return None

