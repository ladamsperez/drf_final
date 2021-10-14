from rest_framework import serializers 
from e1337.models import E1337
 
 
class E1337Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = E1337
        fields = ('id',
                  'title',
                  'description',
                  'published')