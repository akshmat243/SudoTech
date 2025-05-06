from django.contrib import admin
from .models import (
    Account, Contact, Opportunity, Quote, SalesInvoice,
    SalesOrder, Case, Stream, SalesDocument, Call,
    Meeting, SalesReport, SalesSystemSetup
)


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ("name", "industry", "website", "created_at")
    search_fields = ("name", "industry")


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone", "account")
    search_fields = ("name", "email")
    autocomplete_fields = ("account",)


@admin.register(Opportunity)
class OpportunityAdmin(admin.ModelAdmin):
    list_display = ("title", "account", "value", "stage", "close_date")
    search_fields = ("title", "account__name")
    autocomplete_fields = ("account",)


@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display = ("quote_number", "opportunity", "amount", "created_at")
    search_fields = ("quote_number",)
    autocomplete_fields = ("opportunity",)


@admin.register(SalesOrder)
class SalesOrderAdmin(admin.ModelAdmin):
    list_display = ("order_number", "quote", "order_date", "status")
    search_fields = ("order_number",)
    autocomplete_fields = ("quote",)


@admin.register(SalesInvoice)
class SalesInvoiceAdmin(admin.ModelAdmin):
    list_display = ("invoice_number", "sales_order", "amount_due", "due_date")
    search_fields = ("invoice_number",)
    autocomplete_fields = ("sales_order",)


@admin.register(Case)
class CaseAdmin(admin.ModelAdmin):
    list_display = ("title", "account", "status", "created_at")
    search_fields = ("title",)
    autocomplete_fields = ("account",)


@admin.register(Stream)
class StreamAdmin(admin.ModelAdmin):
    list_display = ("related_to", "message", "timestamp")
    search_fields = ("related_to", "message")


@admin.register(SalesDocument)
class SalesDocumentAdmin(admin.ModelAdmin):
    list_display = ("title", "account", "uploaded_at")
    search_fields = ("title",)
    autocomplete_fields = ("account",)


@admin.register(Call)
class CallAdmin(admin.ModelAdmin):
    list_display = ("subject", "contact", "call_time")
    search_fields = ("subject", "contact__name")
    autocomplete_fields = ("contact",)


@admin.register(Meeting)
class MeetingAdmin(admin.ModelAdmin):
    list_display = ("subject", "contact", "meeting_time", "location")
    search_fields = ("subject", "contact__name")
    autocomplete_fields = ("contact",)


@admin.register(SalesReport)
class SalesReportAdmin(admin.ModelAdmin):
    list_display = ("report_date", "total_opportunities", "total_quotes", "total_orders", "total_invoices")
    list_filter = ("report_date",)


@admin.register(SalesSystemSetup)
class SalesSystemSetupAdmin(admin.ModelAdmin):
    list_display = ("key", "value")
    search_fields = ("key",)
