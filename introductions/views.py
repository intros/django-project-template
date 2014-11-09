from django.contrib.auth.decorators import login_required

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

class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)

class IntroductionView(LoginRequiredMixin, TemplateView):
    template_name = "introductions/home.html"

class MailboxListView(LoginRequiredMixin, ListView):
    model = Mailbox
    template_name = "introductions/mailbox_list.html"
    paginate_by = 2

class MailboxDetailView(LoginRequiredMixin, DetailView):
    model = Mailbox
    template_name = "introductions/mailbox_detail.html"

class MailboxUpdateView(LoginRequiredMixin, UpdateView):
    model = Mailbox
    template_name = "introductions/mailbox_form.html"

class MailboxCreateView(LoginRequiredMixin, CreateView):
    model = Mailbox
    template_name = "introductions/mailbox_form.html"

class PersonListView(LoginRequiredMixin, ListView):
    model = Person

class PersonDetailView(LoginRequiredMixin, DetailView):
    model = Person

class PersonCreateView(LoginRequiredMixin, CreateView):
    model = Person

class PersonUpdateView(LoginRequiredMixin, UpdateView):
    model = Person

class PersonEmailListView(LoginRequiredMixin, ListView):
    model = PersonEmail

class PersonEmailDetailView(LoginRequiredMixin, DetailView):
    model = PersonEmail

class PersonEmailCreateView(LoginRequiredMixin, CreateView):
    model = PersonEmail

class PersonEmailUpdateView(LoginRequiredMixin, UpdateView):
    model = PersonEmail

class IntroductionListView(LoginRequiredMixin, ListView):
    model = Introduction
    
    def get_queryset(self):
        if self.request.user.is_authenticated():
            try:
                person = self.request.user.person
                return Introduction.objects.filter(person=person)
            except Exception,e:
                return Introduction.objects.none()

        return Introduction.objects.none()

class IntroductionDetailView(LoginRequiredMixin, DetailView):
    model = Introduction

class IntroductionCreateView(LoginRequiredMixin, CreateView):
    model = Introduction

class IntroductionUpdateView(LoginRequiredMixin, UpdateView):
    model = Introduction

class IntroductionEmailListView(LoginRequiredMixin, ListView):
    model = IntroductionEmail

class IntroductionEmailDetailView(LoginRequiredMixin, DetailView):
    model = IntroductionEmail

class IntroductionEmailCreateView(LoginRequiredMixin, CreateView):
    model = IntroductionEmail

class IntroductionEmailUpdateView(LoginRequiredMixin, UpdateView):
    model = IntroductionEmail

class IntroductionReminderListView(LoginRequiredMixin,ListView):
    model = IntroductionReminder

class IntroductionReminderDetailView(LoginRequiredMixin, DetailView):
    model = IntroductionReminder

class IntroductionReminderCreateView(LoginRequiredMixin,CreateView):
    model = IntroductionReminder
