from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = "home.html"  # TemplateView에서는 필수 오버라이딩
