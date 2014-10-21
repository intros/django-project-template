import logging
logger = logging.getLogger(__name__)

from introductions.views import (
    IntroductionListView,
    IntroductionDetailView,
    IntroductionCreateView,
)


class EagleDashboard(IntroductionListView):
    template_name = "eagle_design/dashboard.html"
    paginate_by = 25
    pagename = "dashboard"


class EagleIntroductionDetailView(IntroductionDetailView):
    template_name = "eagle_design/introduction_detail.html"


class EagleIntroductionCreateView(IntroductionCreateView):
    template_name = "eagle_design/introduction_create.html"
    #pagename = "invitation"

