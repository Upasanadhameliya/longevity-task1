# https://simpleisbetterthancomplex.com/tutorial/2018/08/27/how-to-create-custom-django-management-commands.html

import os

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

from market_api.models import WelltorySubscription, LongevitySubscription


class Command(BaseCommand):
    help = "Seeding a database is a process in which an initial set of data is provided to a database when it is being installed."
    demo_emails = {"user1@gmail.com":[WelltorySubscription],"user2@gmail.com":[LongevitySubscription],"user3@gmail.com":[]}
    demo_pwd = "user@123"

    def __init__(self):
        self.user_class = get_user_model()

        super(Command, self).__init__()


    def handle(self, *args, **options):
        self.create_super_user()
        if os.getenv("POPULATE_DEMO_USERS","False").lower() == "true":
            self.create_users()


    def create_super_user(self):
        if not os.getenv("ADMIN_EMAIL") or not os.getenv("ADMIN_PASSWORD"):
            self.stdout.write(
                self.style.HTTP_BAD_REQUEST("Environment variable is not set.")
            )
            return False

        if self.user_class.objects.filter(email=os.getenv("ADMIN_EMAIL")).exists():
            self.stdout.write(self.style.HTTP_INFO("Admin : Already created."))
            return False

        self.user_class.objects.create_superuser(
            email=os.getenv("ADMIN_EMAIL"),
            password=os.getenv("ADMIN_PASSWORD"),
        )

        self.stdout.write(
            self.style.SUCCESS(
                "Created {} admin account.".format(os.getenv("ADMIN_EMAIL"))
            )
        )
        self.user_class.objects.subscribe(os.getenv("ADMIN_EMAIL"),LongevitySubscription)
        self.user_class.objects.subscribe(os.getenv("ADMIN_EMAIL"),WelltorySubscription)

        self.stdout.write(
            self.style.SUCCESS(
                f"{os.getenv('ADMIN_EMAIL')} subscribed to Longevity and Welltory."
            )
        )

    def create_users(self):
        for email,subscriptions in self.demo_emails.items():
            if self.user_class.objects.find(email):
                self.stdout.write(self.style.HTTP_INFO(f"User : {email} Already created."))
                continue
            self.user_class.objects.create_user(
                email=email,
                password=self.demo_pwd,
            )
            self.stdout.write(
                self.style.SUCCESS(
                    f"{email} user created!"
                )
            )
            if subscriptions:
                for subscription in subscriptions:
                    self.user_class.objects.subscribe(email,subscription)


