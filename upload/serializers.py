from rest_framework import serializers
from upload.models import User,magazine_Upload,magazine_details,magazine_category
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['email','is_verified']
        
class VerifyAccountSerializer(serializers.Serializer):
    email=serializers.EmailField()
    otp=serializers.CharField()
         
class DetailAccountSerializer(serializers.Serializer):
    age=serializers.IntegerField()
    email=serializers.EmailField()
    otp=serializers.CharField()
    class Meta:
        model=User
        fields=['email','age','otp']

class MagazineCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = magazine_category
        fields = ['category_id','category_name','category_discription']
 
        
class MagazinedetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = magazine_details
        fields = ['magazine_id', 'cover_image', 'file_name','discription','issue_date','rent_price','buy_price','rating','category_id']


class UploadMegazineSerializer(serializers.ModelSerializer):
    class Meta:
        model=magazine_Upload
        fields=['magazine_id','File']                                                         
