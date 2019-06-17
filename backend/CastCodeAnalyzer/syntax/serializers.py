from rest_framework import serializers

from .models import Syntax

class SyntaxSerializers(serializers.ModelSerializer):
    class Meta:
        model = Syntax
        fields = ('user', 'tested_on', 'result')