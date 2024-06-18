from django.shortcuts import render

def home(request):
    context={}
    return render(request, "myApp/home.html",context)
from rest_framework import viewsets
from .models import User, Coupon, Transaction, Swap
from .serializers import UserSerializer, CouponSerializer, TransactionSerializer, SwapSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CouponViewSet(viewsets.ModelViewSet):
    queryset = Coupon.objects.all()
    serializer_class = CouponSerializer
    permission_classes = [IsAuthenticated]

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]

class SwapViewSet(viewsets.ModelViewSet):
    queryset = Swap.objects.all()
    serializer_class = SwapSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['post'])
    def accept(self, request, pk=None):
        swap = self.get_object()
        swap.status = 'accepted'
        swap.save()
        return Response({'status': 'swap accepted'})

    @action(detail=True, methods=['post'])
    def decline(self, request, pk=None):
        swap = self.get_object()
        swap.status = 'declined'
        swap.save()
        return Response({'status': 'swap declined'})

