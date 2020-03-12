import django


def seed():
    django.setup()
    from django.contrib.auth.models import User
    from splitbackend.models import Profile
    User.objects.all().delete()

    user_1 = User(username='azab', email='azablan@gmail.com')
    user_1.set_password('promenade')
    user_1.save()
    Profile.objects.create(user=user_1)

    user_2 = User(username='pdfernan', email='pdfernan@gmail.com')
    user_2.set_password('hailhydra')
    user_2.save()
    Profile.objects.create(user=user_2)
