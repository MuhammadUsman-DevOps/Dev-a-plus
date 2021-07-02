from django.contrib import admin

from DevAPlus.models import HeroSection, AboutUsSection, WhyUsSection, ServicesSection, TeamSection, CompanyInfoSection, \
    PortfolioSection, TestimonialSection, ClientSection

admin.site.site_header = "DevA+ Administration Panel"
admin.site.index_title = "DevA+ Administration"


class HeroSectionAdmin(admin.ModelAdmin):
    list_display = ['heading', 'picture']

    def has_add_permission(self, request):
        return not HeroSection.objects.exists()


class AboutUsSectionAdmin(admin.ModelAdmin):
    list_display = ['short_description']

    def has_add_permission(self, request):
        return not AboutUsSection.objects.exists()


class WhyUsSectionAdmin(admin.ModelAdmin):
    list_display = ['heading_1', 'heading_2', 'heading_3', 'clients', 'projects', 'hours_of_support', 'hard_workers']

    def has_add_permission(self, request):
        return not WhyUsSection.objects.exists()


class ServicesSectionAdmin(admin.ModelAdmin):
    list_display = ['heading']


class PortfolioSectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'type', 'url']


class TestimonialSectionAdmin(admin.ModelAdmin):
    list_display = ['client_name', 'designation']


class TeamSectionAdmin(admin.ModelAdmin):
    list_display = ['name', 'designation']


class ClientSectionAdmin(admin.ModelAdmin):
    list_display = ['name', 'logo']


class CompanyInfoSectionAdmin(admin.ModelAdmin):
    list_display = ['street', 'city', 'country', 'phone_number', 'email_address']

    def has_add_permission(self, request):
        return not CompanyInfoSection.objects.exists()


admin.site.register(HeroSection, HeroSectionAdmin)
admin.site.register(AboutUsSection, AboutUsSectionAdmin)
admin.site.register(WhyUsSection, WhyUsSectionAdmin)
admin.site.register(ServicesSection, ServicesSectionAdmin)
admin.site.register(PortfolioSection, PortfolioSectionAdmin)
admin.site.register(TestimonialSection, TestimonialSectionAdmin)
admin.site.register(TeamSection, TeamSectionAdmin)
admin.site.register(ClientSection, ClientSectionAdmin)
admin.site.register(CompanyInfoSection, CompanyInfoSectionAdmin)
