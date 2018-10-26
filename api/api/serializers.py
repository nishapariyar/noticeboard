from rest_framework import serializers
from .models import Notices

class NoticesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Notices
        fields = ('id', 'title', 'notice', 'date_expiry', 'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')
