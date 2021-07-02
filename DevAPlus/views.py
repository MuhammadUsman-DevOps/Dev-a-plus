from django.contrib import messages
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect

from DevAPlus.models import HeroSection, AboutUsSection, WhyUsSection, ServicesSection, PortfolioSection, \
    TestimonialSection, TeamSection, ClientSection, CompanyInfoSection


def index_view(request):
    hero_section = ""
    about_section = ""
    whyus_section = ""
    services_section = ""
    portfolio_section = ""
    testimonial_section = ""
    team_section = ""
    client_section = ""
    company_section = ""
    try:
        hero_section = HeroSection.objects.first()
        about_section = AboutUsSection.objects.first()
        whyus_section = WhyUsSection.objects.first()
        services_section = ServicesSection.objects.all()
        portfolio_section = PortfolioSection.objects.all()
        testimonial_section = TestimonialSection.objects.all()
        team_section = TeamSection.objects.all()
        client_section = ClientSection.objects.all()
        company_section = CompanyInfoSection.objects.first()
    except:
        print("Something went wrong!")

    context = {
        'hero_section': hero_section,
        'about_section': about_section,
        'whyus_section': whyus_section,
        'services_section': services_section,
        'portfolio_section': portfolio_section,
        'testimonial_section': testimonial_section,
        'team_section': team_section,
        'client_section': client_section,
        'company_section': company_section,
    }
    return render(request, template_name="index.html", context=context)



def contact_via_email(request):
    if request.method == "POST":
        sent = send_mail(
            request.POST.get("subject"),
            'Name: ' + request.POST.get("name") + '\n'
            'From Email: ' +request.POST.get("email")+ '\n'
             'Message: '+request.POST.get("message")+'.',
            'from@example.com',
            ['osmanamin689@gmail.com'],
            fail_silently=False,
        )
        print("sent", sent)
        if sent:
            messages.success(request, "Your message has been sent. Thank you!")
            return HttpResponse("OK")