from rest_framework import serializers
from .models import DistributionCenter, Agent, Journalist, JournalistInformation, NewsPaper, Advertisement, Subscriber, SubscriptionPlan, Subscription, Article, NewspaperSale, SystemSetup


class DistributionCenterSerializer(serializers.ModelSerializer):
    class Meta:
        model = DistributionCenter
        fields = '__all__'


class AgentSerializer(serializers.ModelSerializer):
    center = DistributionCenterSerializer()

    class Meta:
        model = Agent
        fields = '__all__'


class JournalistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Journalist
        fields = '__all__'


class JournalistInformationSerializer(serializers.ModelSerializer):
    journalist = JournalistSerializer()

    class Meta:
        model = JournalistInformation
        fields = '__all__'


class NewsPaperSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsPaper
        fields = '__all__'


class AdvertisementSerializer(serializers.ModelSerializer):
    newspaper = NewsPaperSerializer()

    class Meta:
        model = Advertisement
        fields = '__all__'


class SubscriberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriber
        fields = '__all__'


class SubscriptionPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubscriptionPlan
        fields = '__all__'


class SubscriptionSerializer(serializers.ModelSerializer):
    subscriber = SubscriberSerializer()
    plan = SubscriptionPlanSerializer()

    class Meta:
        model = Subscription
        fields = '__all__'


class ArticleSerializer(serializers.ModelSerializer):
    newspaper = NewsPaperSerializer()
    journalist = JournalistSerializer()

    class Meta:
        model = Article
        fields = '__all__'


class NewspaperSaleSerializer(serializers.ModelSerializer):
    agent = AgentSerializer()
    newspaper = NewsPaperSerializer()

    class Meta:
        model = NewspaperSale
        fields = '__all__'


class SystemSetupSerializer(serializers.ModelSerializer):
    class Meta:
        model = SystemSetup
        fields = '__all__'
