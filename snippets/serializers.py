# 1.Serializers 1.0

# from django.forms import widgets
# from rest_framework import serializers
# from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
# 
# 
# class SnippetSerializer(serializers.Serializer):
#     pk = serializers.Field()  # Note: `Field` is an untyped read-only field.
#     title = serializers.CharField(required=False,
#                                   max_length=100)
#     code = serializers.CharField(widget=widgets.Textarea,
#                                  max_length=100000)
#     linenos = serializers.BooleanField(required=False)
#     language = serializers.ChoiceField(choices=LANGUAGE_CHOICES,
#                                        default='python')
#     style = serializers.ChoiceField(choices=STYLE_CHOICES,
#                                     default='friendly')
# 
#     def restore_object(self, attrs, instance=None):
#         """
#         Create or update a new snippet instance, given a dictionary
#         of deserialized field values.
# 
#         Note that if we don't define this method, then deserializing
#         data will simply return a dictionary of items.
#         """
#         if instance:
#             # Update existing instance
#             instance.title = attrs.get('title', instance.title)
#             instance.code = attrs.get('code', instance.code)
#             instance.linenos = attrs.get('linenos', instance.linenos)
#             instance.language = attrs.get('language', instance.language)
#             instance.style = attrs.get('style', instance.style)
#             return instance
# 
#         # Create new instance
#         return Snippet(**attrs)

#-------------------------------------------------------------------------------

# 2.Serializers 2.0
#
# class SnippetSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Snippet
#         fields = ('id', 'title', 'code', 'linenos', 'language', 'style')
        
#-------------------------------------------------------------------------------               

# 4.Serializers 4.0 
# The HyperlinkedModelSerializer has the following differences from ModelSerializer:
# 
# - It does not include the pk field by default.
# - It includes a url field, using HyperlinkedIdentityField.
# - Relationships use HyperlinkedRelatedField, instead of PrimaryKeyRelatedField.
#
from rest_framework import serializers
from snippets.models import Snippet
from django.contrib.auth.models import User


class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.Field(source='owner.username') # Associating with the user
    highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')

    class Meta:
        model = Snippet
        fields = ('url', 'highlight', 'owner',
                  'title', 'code', 'linenos', 'language', 'style')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(view_name='snippet-detail', many=True)

    class Meta:
        model = User
        fields = ('url', 'username', 'snippets')

#-------------------------------------------------------------------------------