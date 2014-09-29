from django.views.generic import (CreateView,
    DetailView,
    ListView,
    RedirectView,
    TemplateView,
    UpdateView,
)

from introductions.models import ( Introduction,
    IntroductionEmail,
    IntroductionReminder,
    Person,
    PersonEmail
)

from django_mailbox.models import (
    Mailbox,
)

class MailboxListView(ListView):
    model = Mailbox
    template_name = "introductions/mailbox_list.html"
    paginate_by = 2

class MailboxDetailView(DetailView):
    model = Mailbox
    template_name = "introductions/mailbox_detail.html"

class MailboxUpdateView(UpdateView):
    model = Mailbox
    template_name = "introductions/mailbox_form.html"

class MailboxCreateView(CreateView):
    model = Mailbox
    template_name = "introductions/mailbox_form.html"

class PersonListView(ListView):
    model = Person

class PersonDetailView(DetailView):
    model = Person

class PersonCreateView(CreateView):
    model = Person

class PersonUpdateView(UpdateView):
    model = Person

class PersonEmailListView(ListView):
    model = PersonEmail

class PersonEmailDetailView(DetailView):
    model = PersonEmail

class PersonEmailCreateView(CreateView):
    model = PersonEmail

class PersonEmailUpdateView(UpdateView):
    model = PersonEmail

class IntroductionListView(ListView):
    model = Introduction

class IntroductionDetailView(DetailView):
    model = Introduction

class IntroductionCreateView(CreateView):
    model = Introduction

class IntroductionUpdateView(UpdateView):
    model = Introduction

class IntroductionEmailListView(ListView):
    model = IntroductionEmail

class IntroductionEmailDetailView(DetailView):
    model = IntroductionEmail

class IntroductionEmailCreateView(CreateView):
    model = IntroductionEmail

class IntroductionEmailUpdateView(UpdateView):
    model = IntroductionEmail

class IntroductionReminderListView(ListView):
    model = IntroductionReminder

class IntroductionReminderDetailView(DetailView):
    model = IntroductionReminder

class IntroductionReminderCreateView(CreateView):
    model = IntroductionReminder
