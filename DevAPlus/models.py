from django.db import models


class HeroSection(models.Model):
    heading = models.CharField(max_length=200, null=True, blank=True)
    picture = models.ImageField(upload_to="images/", null=True, blank=True)

    class Meta:
        verbose_name = "Hero Section"
        verbose_name_plural = "Hero Section"

    def __str__(self):
        return self.heading


class AboutUsSection(models.Model):
    short_description = models.TextField(max_length=500, null=True, blank=True)
    long_description = models.TextField(max_length=1000, null=True, blank=True)

    class Meta:
        verbose_name = "About Us Section"
        verbose_name_plural = "About Us Section"

    def __str__(self):
        return self.short_description


class WhyUsSection(models.Model):
    heading_1 = models.CharField(max_length=100, null=True, blank=True)
    description_1 = models.TextField(max_length=500, null=True, blank=True)
    heading_2 = models.CharField(max_length=100, null=True, blank=True)
    description_2 = models.TextField(max_length=500, null=True, blank=True)
    heading_3 = models.CharField(max_length=100, null=True, blank=True)
    description_3 = models.TextField(max_length=500, null=True, blank=True)

    clients = models.IntegerField(null=True, blank=True)
    projects = models.IntegerField(null=True, blank=True)
    hours_of_support = models.IntegerField(null=True, blank=True)
    hard_workers = models.IntegerField(null=True, blank=True)

    class Meta:
        verbose_name = "Why Us Section"
        verbose_name_plural = "Why Us Section"

    def __str__(self):
        return self.heading_1


class ServicesSection(models.Model):
    svg_icon = models.CharField(max_length=3000, null=True, blank=True)
    heading = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(max_length=500, null=True, blank=True)

    class Meta:
        verbose_name = "Services Section"
        verbose_name_plural = "Services Section"

    def __str__(self):
        return self.heading


class PortfolioSection(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    type = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to="images/portfolio/", null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    budget = models.IntegerField(null=True, blank=True)

    class Meta:
        verbose_name = "Portfolio Section"
        verbose_name_plural = "Portfolio Section"

    def __str__(self):
        return self.title


class TestimonialSection(models.Model):
    client_name = models.CharField(max_length=100, null=True, blank=True)
    designation = models.CharField(max_length=50, null=True, blank=True)
    image = models.ImageField(upload_to="images/testimonial/", null=True, blank=True)
    comment = models.TextField(max_length=500, null=True, blank=True)

    class Meta:
        verbose_name = "Testimonial Section"
        verbose_name_plural = "Testimonial Section"

    def __str__(self):
        return self.client_name


class TeamSection(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    designation = models.CharField(max_length=25, null=True, blank=True)
    image = models.ImageField(upload_to="images/team/", null=True, blank=True)
    twitter = models.URLField(null=True, blank=True)
    facebook = models.URLField(null=True, blank=True)
    github = models.URLField(null=True, blank=True)
    linkedIn = models.URLField(null=True, blank=True)

    class Meta:
        verbose_name = "Team Section"
        verbose_name_plural = "Team Section"

    def __str__(self):
        return self.name


class ClientSection(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    logo = models.ImageField(upload_to="images/clients/", null=True, blank=True)

    class Meta:
        verbose_name = "Client Section"
        verbose_name_plural = "Client Section"

    def __str__(self):
        return self.name


class CompanyInfoSection(models.Model):
    street = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    country = models.CharField(max_length=50, null=True, blank=True)
    phone_number = models.CharField(max_length=50, null=True, blank=True)
    email_address = models.EmailField(null=True, blank=True)

    twitter = models.URLField(null=True, blank=True)
    facebook = models.URLField(null=True, blank=True)
    instagram = models.URLField(null=True, blank=True)
    github = models.URLField(null=True, blank=True)
    linkedIn = models.URLField(null=True, blank=True)

    iframe = models.CharField(max_length=1000, null=True, blank=True)

    class Meta:
        verbose_name = "Company Info Section"
        verbose_name_plural = "Company Info Section"

    def __str__(self):
        return self.street
