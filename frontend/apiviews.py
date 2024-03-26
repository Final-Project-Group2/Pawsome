from django.shortcuts import render
from rest_framework.reverse import reverse
from rest_framework.decorators import action, authentication_classes, permission_classes,api_view
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.generics import ListAPIView 
from django.http import HttpResponseRedirect
from rest_framework.response import Response
from .serializers import PetSerializer, Pet
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated, AND, SAFE_METHODS, IsAuthenticatedOrReadOnly, IsAdminUser,AllowAny
from rest_framework.status import HTTP_202_ACCEPTED,HTTP_404_NOT_FOUND,HTTP_201_CREATED,HTTP_200_OK,HTTP_401_UNAUTHORIZED,HTTP_400_BAD_REQUEST



class PetsSet(GenericViewSet):
      queryset = Pet.objects.all()
      serializer_class = PetSerializer

      @permission_classes(AllowAny)
      @action(detail=False, methods=["GET"],url_path="allpets", url_name="listallpets")
      def allpets(self,request, *args,**kwargs):
            try:
                  data=self.get_queryset()
                  s=self.serializer_class(data=data,many=True)
                  s.is_valid()
                  return Response(s.data, status=HTTP_200_OK )
            except Exception as e:
                  return Response({"Response":f"Error {e} \non load details"},status=HTTP_404_NOT_FOUND)           


      @action(detail=False, methods=["GET","POST"],url_path="addpets/", url_name="addnewpets")
      def allpets(self,request, *args,**kwargs):
            
            data=request.resolver_match.kwargs
            dog={"name":"cC","species":"dog","size":"small","breed":"Bichon","age":1,"gender":"Male","weight":4,"description":"FFF","status":"Available"}
            s=self.serializer_class(data=dog)
            
            s.is_valid()
            s.create(dog)
            s.save()
            return Response(s.data,status=HTTP_200_OK )
            #except Exception as e:
            #      return Response({"Response":f"Error {e} \non load details"},status=HTTP_404_NOT_FOUND)           
