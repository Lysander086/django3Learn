from rest_framework import serializers
from .models import Ebook, Review, Quote


class ReviewSerializer(serializers.ModelSerializer):
    review_author = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Review
        exclude = ("ebook",)
        # fields = "__all__"


# equals to java dto
class EbookSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Ebook
        fields = "__all__"

class QuoteSerializer(serializers.ModelSerializer):

    quote_author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Quote
        fields = "__all__"
