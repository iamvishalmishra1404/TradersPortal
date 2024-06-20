from django.shortcuts import render,get_object_or_404
from django.contrib.auth.decorators import login_required
from rest_framework import generics,status
from rest_framework.permissions import IsAuthenticated
from .models import Company, Watchlist,Price
from .serializers import CompanySerializer, WatchlistSerializer , PriceSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
# from django.shortcuts import get_object_or_404


# Create your views here.

def login(request):
    return render(request,'Userapp/login.html')

@login_required
def home(request):
    return render(request,'Userapp/home.html')

# class CompanyList(generics.ListAPIView):
#     queryset = Company.objects.all()
#     serializer_class = CompanySerializer

#     def get_queryset(self):
#         query = self.request.query_params.get('q', '')
#         return Company.objects.filter(company_name__icontains=query)

class CompanySearchAPIView(generics.ListAPIView):
    serializer_class = CompanySerializer

    def get_queryset(self):
        queryset = Company.objects.all()
        query = self.request.query_params.get('q', None)
        if query:
            queryset = queryset.filter(company_name__icontains=query)
        return queryset

class AddToWatchlistAPIView(APIView):
    def post(self, request):
        company_name = request.data.get('company_name')
        user_id = request.data.get('user_id')

        user = get_object_or_404(User, id=user_id)
        company = get_object_or_404(Company, name=company_name)

        watchlist, created = Watchlist.objects.get_or_create(user=user)
        watchlist.companies.add(company)
        watchlist.save()

        return Response({'status': 'Company added to watchlist'}, status=status.HTTP_200_OK)
    
class GetPriceAPIView(generics.ListAPIView):
    serializer_class = PriceSerializer

    def get_queryset(self):
        queryset = Price.objects.all()
        query = self.request.query_params.get('q', None)
        if query:
            queryset = Price.objects.filter(symbol__icontains=query).values('price')
        return queryset