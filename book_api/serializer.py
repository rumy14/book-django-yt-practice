# from rest_framework import serializers
# from book_api.models import Book

# # Create your models here.
# class BookSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField()
#     number_of_pages = serializers.IntegerField()
#     publish_date = serializers.DateField()
#     quantity = serializers.IntegerField()

#     def create(self, data):
#         return Book.objects.create(**data)
    
#     def update(self, instance, data):
#         instance.title = data.get('title', instance.title)
#         instance.number_of_pages = data.get('number_of_pages', instance.number_of_pages)
#         instance.publish_date = data.get('publish_date', instance.publish_date)
#         instance.quantity = data.get('quantity', instance.quantity)

#         instance.save()
#         return instance

from xml.dom import ValidationErr
from rest_framework import serializers
from book_api.models import Book
from django.forms import ValidationError

class BookSerializer(serializers.ModelSerializer):
    description = serializers.ModelSerializer()
    class Meta:
        model = Book
        fields = "__all__"

    def validate_title(self, value):
        if value == "Diet Coke":
            raise ValidationError("No diet coke please")
        return value
    
    def validate_title(self, data):
        if int(data["number_of_pages"]) > 200 and data["quantity"] > 200:
            raise ValidationError("Too heavy for inventory")
        return data
    
    def get_description(self, data):
        return "This book is called " + data.title + " and it is " + str(data.number_of_pages) + " long"
