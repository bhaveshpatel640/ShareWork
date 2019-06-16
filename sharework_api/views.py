# Create your views here.
import logging

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .utils.common_utility import CommonUtility
from .models import Urls
from .serializers import UrlsSerializer


class UrlsDetail(APIView):

    log = logging.getLogger(__name__)

    def get(self, request, short_url):
        response_data = {}
        self.log.info("data recieved" + str(request), short_url)
        try:
            print(short_url)
            url = Urls.objects.get(short_url=short_url)
            url_serializer = UrlsSerializer(url)
            response_data = url_serializer.data
            del url_serializer.data['id']
            print(url_serializer.data)
            self.log.info("data responded" + str(response_data))
        except Exception as e:
            print("doesnotexists", e)
            self.log.error("doesnotexists" + str(e))
        finally:
            return Response(response_data)


class UrlsView(APIView):

    def post(self, request, format=None):

        request.data.update({
            "short_url": CommonUtility.generate_short_url(7)
        })
        print(request.data)
        serializer = UrlsSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            del serializer.data['id']
            print(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
