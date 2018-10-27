from rest_framework import serializers
from .models import Noticelist

class NoticeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Noticelist
        fields = ('id', 'title', 'notice_text', 'date_expiry', 'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')
