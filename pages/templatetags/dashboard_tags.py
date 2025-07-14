from django import template
from django.db.models import Q

from sales.models import Invoice, Offer


register = template.Library()


@register.inclusion_tag("pages/dashboard/total_earnings.html")
def total_earnings():
    invoices_from_db = list(Invoice.objects.all())
    total_earnings_by_invoice = round(
        sum(invoice.total_sum for invoice in invoices_from_db), 2
    )
    return {"total_earnings_by_invoice": total_earnings_by_invoice}


@register.inclusion_tag("pages/dashboard/paid_earnings.html")
def paid_earnings():
    paid_invoices_from_db = list(Invoice.objects.filter(status="paid"))
    paid_earnings_by_invoice = round(
        sum(invoice.total_sum for invoice in paid_invoices_from_db), 2
    )
    return {"paid_earnings_by_invoice": paid_earnings_by_invoice}


@register.inclusion_tag("pages/dashboard/total_planned_earnings.html")
def total_planed_earnings():
    offers_from_db = list(Offer.objects.all())
    total_earnings_by_offers = round(
        sum(offer.total_sum for offer in offers_from_db), 2
    )
    return {"total_earnings_by_offers": total_earnings_by_offers}


@register.inclusion_tag("pages/dashboard/canceled_failed_offers.html")
def total_canceled_failed_offers():
    offers_from_db = list(
        Offer.objects.filter(Q(status="canceled") | Q(status="failed"))
    )
    canceled_failed_offers = round(sum(offer.total_sum for offer in offers_from_db), 2)
    return {"canceled_failed_offers": canceled_failed_offers}
