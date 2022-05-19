from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from upload.serializers import UserSerializer,UploadMegazineSerializer,MagazinedetailSerializer,MagazineCategorySerializer
from rest_framework.parsers import MultiPartParser

# Create your views here.
class RegisterAPI(APIView):
    def post(self,request):
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'msg':'Registration Successful'},status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class MagazineDetailSet(APIView):
    def post(self, request):
        serializer=MagazinedetailSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'msg':'Registration Successful'},status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)   
  
class MultipleImageViewSet(APIView):
    def post(self, request):
        get_serializer = UploadMegazineSerializer
        try: 
            if get_serializer.is_valid:
                
                files = request.FILES.getlist('Files')
                idd=request.data['magazine_id']
                print("Files : ",files)
                print("magazine_id :",idd)
                li =[]
                dic ={}
                for value in files:
                    print(value,"======")
                    dic['File'] = value
                    dic['magazine_id']= idd
                    # print(key,values)
                    serializer = UploadMegazineSerializer(data=dic)
                    if serializer.is_valid(raise_exception=True):
                        serializer.save()
                        li.append(serializer.data)
                return Response({'msg': 'Data Success Fully Saved.', 'data':serializer.data},status=status.HTTP_200_OK)     
        except:
            return Response(get_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class MagazineViewSet(APIView):
    def post(self, request):
        serializer=MagazineCategorySerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'msg':'Registration Successful'},status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)   
    
