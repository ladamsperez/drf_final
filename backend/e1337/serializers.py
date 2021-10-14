from django.contrib.auth.models import E1337
from rest_framework import serializers 
from models import E1337
 
 
class E1337Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = E1337
        fields = ['url', 'description', 'published']

        # need to overwrite default view_name='user-detail' because app_name
        # NOTE: if you use serializer.HyperlinkedIdentityField outside of meta,
        # it will assign to wrong user and instead index the user correlating to task id.
        extra_kwargs = {
            'url': {'view_name': 'users:user-detail', 'lookup_field': 'username'},
        }