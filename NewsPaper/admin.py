from django.contrib import admin
from .models import (
    DistributionCenter, Agent, Journalist, JournalistInformation, NewsPaper, Advertisement,
    Subscriber, SubscriptionPlan, Subscription, Article, NewspaperSale, SystemSetup
)

@admin.register(DistributionCenter)
class DistributionCenterAdmin(admin.ModelAdmin):
    list_display = ['name', 'contact']
    search_fields = ['name', 'contact']


@admin.register(Agent)
class AgentAdmin(admin.ModelAdmin):
    list_display = ['name', 'center', 'phone']
    search_fields = ['name']
    list_filter = ['center']


@admin.register(Journalist)
class JournalistAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone']
    search_fields = ['name', 'email']


@admin.register(JournalistInformation)
class JournalistInformationAdmin(admin.ModelAdmin):
    list_display = ['journalist']
    search_fields = ['journalist__name']


@admin.register(NewsPaper)
class NewsPaperAdmin(admin.ModelAdmin):
    list_display = ['title', 'issue_date', 'edition']
    list_filter = ['issue_date']
    search_fields = ['title']


@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['client_name', 'newspaper', 'published_on', 'price']
    list_filter = ['published_on']
    search_fields = ['client_name']


@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone']
    search_fields = ['name', 'email']


@admin.register(SubscriptionPlan)
class SubscriptionPlanAdmin(admin.ModelAdmin):
    list_display = ['name', 'duration_days', 'price']


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ['subscriber', 'plan', 'start_date', 'end_date']
    list_filter = ['start_date', 'end_date']
    search_fields = ['subscriber__name']


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'journalist', 'published_on']
    list_filter = ['published_on']
    search_fields = ['title', 'journalist__name']


@admin.register(NewspaperSale)
class NewspaperSaleAdmin(admin.ModelAdmin):
    list_display = ['agent', 'newspaper', 'quantity', 'sale_date']
    list_filter = ['sale_date']


@admin.register(SystemSetup)
class SystemSetupAdmin(admin.ModelAdmin):
    list_display = ['key']
    search_fields = ['key']
