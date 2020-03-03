from rest_framework import serializers

from articles.models import *

class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SectionModel
        fields = ('id', 'title', 'pablish')


class ThemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ThemeModel
        fields = ('title',
                  'section',
                  'pablish',
                  'create',
                  'update'
        )


class PablicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PablicationModel
        fields = ('theme',
                  'title',
                  'content',
                  'image_content',
                  'pablish',
                  'create',
                  'update',
                  'slug',
        )
