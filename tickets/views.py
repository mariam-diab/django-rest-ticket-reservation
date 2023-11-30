from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Customer, Movie, Reservation
from .serializers import CustomerSerializers, MovieSerializers, ReservationSerializers
from rest_framework.response import Response
from rest_framework import status, filters
from rest_framework.views import APIView
from rest_framework import generics, mixins, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from django.contrib.auth.decorators import permission_required
from django.shortcuts import get_object_or_404
from rest_framework.pagination import PageNumberPagination
from rest_framework.authentication import SessionAuthentication






# Create your views here.

# views_
    
class GenericsCustomerList(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializers
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

class GenericsCustomer(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializers
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

class ViewsetsCustomer(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializers

class ViewsetsMovie(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializers
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

class CustomPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 100

class ViewsetsReservation(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializers
    pagination_class = CustomPagination

@api_view(['GET'])
def find_movie(request):
    movie = Movie.objects.filter(
        # name = request.data["name"],
        # The error arises as of attempting to access the name key 
        # from the request.data dictionary in a GET request, 
        # but request.data does not contain any data for a GET request. 
        # request.query_params should be used to access the parameters passed in a GET request.
        name = request.query_params.get("movie_name"),
        #class object                    key
    )
    # ex:http://127.0.0.1:8000/findmovie/?movie_name=Friends
    serializer = MovieSerializers(movie, many= True)
    return Response(serializer.data)

@api_view(['POST'])
def new_reservation(request):
    try:
        movie = Movie.objects.get(
            name=request.query_params.get("movie_name"),  
            hall=request.query_params.get("hall")
        )
    except Movie.DoesNotExist:
        return Response("Movie does not exist", status=status.HTTP_404_NOT_FOUND)

    # customer = Customer()
    # customer.name = request.query_params.get['customer_name']
    # customer.phone_number = request.query_params.get['phone_number']
    # customer.save()

    customer, created = Customer.objects.get_or_create(
        name=request.query_params.get('customer_name'),
        phone_number=request.query_params.get('phone_number')
    )

    reservation = Reservation()
    reservation.customer_name = customer
    reservation.movie_name = movie
    reservation.save()

    return Response(status=status.HTTP_201_CREATED)

@api_view(['POST']) #done
@permission_required('tickets.add_movie')
@permission_classes([IsAuthenticated])
def create_movie(request):
    serializer = MovieSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@permission_required('tickets.change_movie')
@permission_classes([IsAuthenticated])
def update_movie(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    serializer = MovieSerializers(movie, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_required('tickets.delete_movie')
@permission_classes([IsAuthenticated])
def delete_movie(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    movie.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET']) #done
@permission_required('tickets.view_reservation')
@permission_classes([IsAuthenticated])
def view_reservation(request, reservation_id):
    reservation = get_object_or_404(Reservation, pk=reservation_id)
    serializer = ReservationSerializers(reservation)
    return Response(serializer.data)