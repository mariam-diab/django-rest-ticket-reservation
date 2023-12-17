"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from tickets import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from django.views.generic.base import RedirectView

router = DefaultRouter()
# router.register("customer", views.ViewsetsCustomer)
router.register("movie", views.ViewsetsMovie)
router.register("reservation", views.ViewsetsReservation)

urlpatterns = [
    path('admin', admin.site.urls),
    path('', views.user_login),
    # paths_
    path('customergenerics/', views.GenericsCustomerList.as_view(), name='customerlist'),
    path('customergenerics/<int:pk>', views.GenericsCustomer.as_view()),
    # path('customerviewsets/', include(router.urls)),
    # path('movieviewsets/', include(router.urls)),
    # path('reservationviewsets/', include(router.urls)),
    path('viewsets/', include(router.urls)),
    path('findmovie/', views.find_movie),
    path('newreservation/',views.new_reservation),
    path('api-token-auth/', obtain_auth_token),
    path('movies/create/', views.create_movie),
    path('movies/update/<int:movie_id>', views.update_movie),
    path('movies/delete/<int:movie_id>', views.delete_movie),
    path('reservations/view/<int:reservation_id>', views.view_reservation),
    path('login', views.user_login),

]

