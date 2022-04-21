from mongo_handler import MongoHandler
from datetime import datetime

handler = MongoHandler("ecbd")
user_collection = handler.get_collection("users")
channel_collection = handler.get_collection("channels")


def create_channels():
    channel_collection.insert_many([
        {
            "name": "#hr-iasi",
            "type": "public",
            "creation_date": datetime(year=2018, month=4, day=1, hour=10, minute=1, second=15).replace(microsecond=0),
            "meta": {
                "archived": False
            }
        },
        {
            "name": "#python-news",
            "type": "public",
            "creation_date": datetime(year=2018, month=6, day=15, hour=14, minute=26, second=15).replace(microsecond=0),
            "meta": {
                "archived": True
            }
        },
        {
            "name": "#random",
            "type": "public",
            "creation_date": datetime(year=2018, month=4, day=29, hour=10, minute=5, second=54).replace(microsecond=0),
            "meta": {
                "archived": False
            }
        },
        {
            "name": "#securtiy",
            "type": "public",
            "creation_date": datetime(year=2018, month=4, day=1, hour=10, minute=9, second=31).replace(microsecond=0),
            "meta": {
                "archived": False
            }
        },
        {
            "name": "#red-team",
            "type": "private",
            "creation_date": datetime(year=2018, month=4, day=5, hour=13, minute=26, second=21).replace(microsecond=0),
            "meta": {
                "archived": False
            }
        },
        {
            "name": "#blue-team",
            "type": "private",
            "creation_date": datetime(year=2018, month=4, day=5, hour=13, minute=31, second=43).replace(microsecond=0),
            "meta": {
                "archived": False
            }
        },
        {
            "name": "#it-help",
            "type": "public",
            "creation_date": datetime(year=2019, month=1, day=7, hour=10, minute=2, second=59).replace(microsecond=0),
            "meta": {
                "archived": False
            }
        },
        {
            "name": "#infrastructure-team",
            "type": "private",
            "creation_date": datetime(year=2019, month=3, day=1, hour=10, minute=10, second=31).replace(microsecond=0),
            "meta": {
                "archived": False
            }
        },
        {
            "name": "#devops-team",
            "type": "private",
            "creation_date": datetime(year=2019, month=3, day=1, hour=10, minute=31, second=49).replace(microsecond=0),
            "meta": {
                "archived": False
            }
        },
        {
            "name": "#devops-team-help",
            "type": "public",
            "creation_date": datetime(year=2019, month=3, day=2, hour=11, minute=56, second=31).replace(microsecond=0),
            "meta": {
                "archived": False
            }
        },
        {
            "name": "#infrastructure-team-help",
            "type": "public",
            "creation_date": datetime(year=2019, month=3, day=2, hour=12, minute=1, second=29).replace(microsecond=0),
            "meta": {
                "archived": False
            }
        },
        {
            "name": "#shoutouts",
            "type": "public",
            "creation_date": datetime(year=2020, month=1, day=6, hour=10, minute=54, second=39).replace(microsecond=0),
            "meta": {
                "archived": False
            }
        },
        {
            "name": "#tunes",
            "type": "public",
            "creation_date": datetime(year=2020, month=7, day=19, hour=17, minute=5, second=11).replace(microsecond=0),
            "meta": {
                "archived": False
            }
        },
        {
            "name": "#announcements",
            "type": "public",
            "creation_date": datetime(year=2020, month=9, day=5, hour=13, minute=10, second=1).replace(microsecond=0),
            "meta": {
                "archived": False
            }
        },
        {
            "name": "#christmas-2020",
            "type": "public",
            "creation_date": datetime(year=2020, month=12, day=24, hour=10, minute=1, second=15).replace(microsecond=0),
            "meta": {
                "archived": True
            }
        },
        {
            "name": "#easter-2021",
            "type": "public",
            "creation_date": datetime(year=2021, month=5, day=2, hour=8, minute=32, second=58).replace(microsecond=0),
            "meta": {
                "archived": True
            }
        },
        {
            "name": "#teambuilding-2018",
            "type": "public",
            "creation_date": datetime(year=2018, month=8, day=13, hour=8, minute=32, second=58).replace(microsecond=0),
            "meta": {
                "archived": True
            }
        },
        {
            "name": "#teambuilding-2019",
            "type": "public",
            "creation_date": datetime(year=2019, month=7, day=30, hour=8, minute=32, second=58).replace(microsecond=0),
            "meta": {
                "archived": True
            }
        },
        {
            "name": "#teambuilding-2020",
            "type": "public",
            "creation_date": datetime(year=2020, month=7, day=26, hour=8, minute=32, second=58).replace(microsecond=0),
            "meta": {
                "archived": True
            }
        },
    ])


def get_object_id_for_channel(channel: str):
    return channel_collection.find({"name": channel}).limit(1)


print([x for x in get_object_id_for_channel("#hr-iasi")])

#
# user_collection.insert_many([{
#     "first_name": "Ionut",
#     "last_name": "Baltariu",
#     "user_name": "xeno-john",
#     "email": "saltyjohn31@gmail.com",
#     "registration_date": datetime(year=2021, month=5, day=20, hour=14, minute=30, second=49).replace(microsecond=0)
# }])

print([x for x in user_collection.find({})])