# voluntariapp/serializers.py
from django.utils import timezone
from rest_framework import serializers
from . import models
import pytz

utc = pytz.UTC


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserProfile
        fields = ('mobile_phone','days','group')


class UserSerializer(serializers.ModelSerializer):

    email = serializers.CharField(source='username')
    profile = UserProfileSerializer(required=True)

    class Meta:
        model = models.User
        fields = ('first_name', 'last_name', 'password', 'profile', 'email')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        password = validated_data.pop('password')
        user = models.User(**validated_data)
        user.set_password(password)
        user.save()
        models.UserProfile.objects.create(user=user, **profile_data)
        return user

class EventAttendeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.EventAttendee
        fields = ("id", "event","user")


    def create(self, validated_data):
        eventattendee = models.EventAttendee(**validated_data)
        eventattendee.save()
        return eventattendee


class EventSerializer(serializers.ModelSerializer):
    attendance = serializers.SerializerMethodField()
    attending = serializers.SerializerMethodField()
    finished = serializers.SerializerMethodField()

    def get_attendance(self, obj):
        return models.EventAttendee.objects.filter(event=obj).count()


    def get_attending(self, obj):
        return models.EventAttendee.objects.filter(event=obj, user=self.context['request'].user).exists()

    def get_finished(self, obj):
        return obj.start_date < timezone.now()

    class Meta:
        model = models.Event
        fields = ('id', 'creator', 'title', 'group', 'start_date', 'end_date', 'description', 'attendance', 'week','attending', 'finished')


# FALTA ATTENDING!
class EventPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Event
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Comment
        fields = ("id", "author", "content", "created_date", "forumtheme")


class ForumThemeGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ForumTheme
        fields = ("id", "title", "creator", "description", "finished", "created_date", "group")


class ForumThemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ForumTheme
        fields = ("id", "title", "creator", "description", "finished", "created_date", "group")


class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Rate
        fields = ("event", "comments", "snack_rate", "line_rate", "circle_rate", "respect_rate", "activity_rate")





class CoursSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Cours
        fields = '__all__'


class QuarterSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Quarter
        fields = '__all__'


class WeekSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Week
        fields = '__all__'


class CentreInteresSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CentreInteres
        fields = '__all__'


class ObjectiuSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Objectiu
        fields = '__all__'


class ExplicacioSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Explicacio
        fields = '__all__'


class ExplicacioGetFromCentreInteresSerializer(serializers.ModelSerializer):
    finished = serializers.SerializerMethodField()

    def get_finished(self, obj):
        if obj.date == None:
            return False
        else:
            now = timezone.now()
            return obj.date < now

    class Meta:
        model = models.Explicacio
        fields = ('id', 'date', 'description', 'centreinteres', 'finished')
