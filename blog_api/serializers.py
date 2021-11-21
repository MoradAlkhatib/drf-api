
## provide a way of serializing and deserializing the snippet instances into representations such as json.


from rest_framework import serializers
from .models import Blog


class BlogSterilizer(serializers.ModelSerializer):
    class Meta:
        model=Blog
        fields=('id' , 'title','author' , 'body', 'created_at', 'updated_at')