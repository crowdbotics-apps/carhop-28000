from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import (
    PaymentTransactionViewSet,
    PaymentMethodViewSet,
    TaskerWalletViewSet,
    TaskerPaymentAccountViewSet,
    CustomerWalletViewSet,
)

router = DefaultRouter()
router.register("taskerpaymentaccount", TaskerPaymentAccountViewSet)
router.register("paymenttransaction", PaymentTransactionViewSet)
router.register("customerwallet", CustomerWalletViewSet)
router.register("taskerwallet", TaskerWalletViewSet)
router.register("paymentmethod", PaymentMethodViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
