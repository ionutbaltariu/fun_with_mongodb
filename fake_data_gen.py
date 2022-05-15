from faker import Faker
from faker.providers import DynamicProvider
from faker_food import FoodProvider
import datetime
import random

fake = Faker(locale="ro_RO")

zodiac_provider = DynamicProvider(
    provider_name="zodiac",
    elements="Aries, Taurus, Gemini, Cancer, Leo, Virgo, Libra, Scorpio, Sagittarius,"
             " Capricorn, Aquarius, Pisces".split(", "),
)

relationship_status_provider = DynamicProvider(
    provider_name="relationship",
    elements=["single", "married", "divorced", "in a couple"]
)

# then add new provider to faker instance
fake.add_provider(zodiac_provider)
fake.add_provider(relationship_status_provider)
fake.add_provider(FoodProvider)


def get_random_subset_of_channel_ids(channel_ids):
    return random.sample(channel_ids, random.randint(1, len(channel_ids) - 1))


def get_fake_users(channel_ids, number: int = 100):
    Faker.seed(0)
    return [{
        "first_name": (first_name := fake.first_name()),
        "last_name": (last_name := fake.last_name()),
        "user_name": f"{first_name.lower()}.{last_name.lower()}",
        "email": f"{first_name.lower()}.{last_name.lower()}@companie.com",
        "registration_date": datetime.datetime.fromordinal(
            fake.date_between(start_date=datetime.datetime(year=2018, month=1, day=1, hour=0, minute=0, second=0),
                              end_date=datetime.datetime(year=2022, month=1, day=1, hour=0, minute=0,
                                                         second=0)).toordinal()),
        "ex_jobs": [{
            "name": fake.job(),
            "company": fake.company()
        } for _ in range(0, random.randint(1, 6))
        ],
        "current_job": {
            "name": fake.job(),
            "years_of_experience": random.randint(0, 7)
        },
        "personal_information": {
            "relationship_status": fake.relationship(),
            "zodiac": fake.zodiac(),
            "favorite_food": fake.dish()
        },
        "channels": get_random_subset_of_channel_ids(channel_ids)
    } for _ in range(number)]


def get_fake_comments(channels, users, number: int = 15000):
    Faker.seed(0)
    fake_comments_list = []
    for _ in range(0, number):
        random_channel = channels[random.randint(0, len(channels) - 1)]
        random_user = users[random.randint(0, len(users) - 1)]

        fake_comments_list.append({
            "value": fake.text(max_nb_chars=160),
            "channel": random_channel["_id"],
            "user": random_user["_id"],
            "sent_at": datetime.datetime.fromordinal(fake.date_between(start_date=random_user["registration_date"])
                                                     .toordinal()),
            "likes": random.randint(0, len(users))
        })

    return fake_comments_list
