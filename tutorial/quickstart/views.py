from django.shortcuts import render

from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import *
from .serializers import *

from rest_framework import viewsets
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from .serializers import UserSerializer

# Create your views here.
User = get_user_model()

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]  # Only admin can manage users
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']

    @action(detail=True, methods=['post'])
    def activate(self, request, pk=None):
        user = self.get_object()
        user.status = 'active'
        user.save()
        return Response({'status': 'user activated'})

    @action(detail=True, methods=['post'])
    def deactivate(self, request, pk=None):
        user = self.get_object()
        user.is_active = False
        user.save()
        return Response({'status': 'user deactivated'})
    
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    @action(detail=True, methods=['post'])
    def rate(self, request, pk=None):
        product = self.get_object()
        serializer = FeedbackSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user, product=product)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()  # Add this
    serializer_class = CartSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)

    @action(detail=True, methods=['post'])
    def checkout(self, request, pk=None):
        cart = self.get_object()
        # Implement checkout logic here
        return Response({'status': 'checkout initiated'})

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()  # Add this
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)

    
class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()  # Add this
    serializer_class = PaymentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return super().get_queryset().filter(order__user=self.request.user)

class FeedbackViewSet(viewsets.ModelViewSet):
   queryset = Feedback.objects.all()
   serializer_class = FeedbackSerializer
   permission_classes = [permissions.IsAuthenticatedOrReadOnly]

   def get_queryset(self):
        return Feedback.objects.all()