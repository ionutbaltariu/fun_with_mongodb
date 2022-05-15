from datetime import datetime

from faker import Faker
from pymongo import TEXT

from fake_data_gen import get_fake_users, get_fake_comments
from mongo_handler import MongoHandler

handler = MongoHandler("ecbd")

handler.database.create_collection("users")

handler.database.command('collMod', 'users', validator={
    "$jsonSchema": {
        "bsonType": "object",
        "required": ["first_name", "last_name", "user_name", "email", "ex_jobs",
                     "current_job", "registration_date",
                     "personal_information", "channels"],
        "properties": {
            "first_name": {
                "bsonType": "string",
                "description": "must be a string and is required"
            },
            "last_name": {
                "bsonType": "string",
                "description": "must be a string and is required"
            },
            "user_name": {
                "bsonType": "string",
                "description": "must be a string and is required"
            },
            "email": {
                "bsonType": "string",
                "description": "must be a string and is required"
            },
            "registration_date": {
                "bsonType": "date",
                "description": "must be a date and is required"
            },
            "ex_jobs": {
                "bsonType": "array",
                "items": {
                    "bsonType": "object",
                    "required": ["name", "company"],
                    "properties": {
                        "name": {
                            "bsonType": "string",
                            "description": "must be a string and is required"
                        },
                        "company": {
                            "bsonType": "string",
                            "description": "must be a string and is required"
                        }
                    }
                },
                "description": "must be a array of objects containing name and company"
            },
            "current_job": {
                "bsonType": "object",
                "required": ["name", "years_of_experience"],
                "properties": {
                    "relationship_status": {
                        "bsonType": "string",
                        "description": "must be a string and is required"
                    },
                    "years_of_experience": {
                        "bsonType": "int",
                        "description": "must be an int and is required"
                    }
                }
            },
            "personal_information": {
                "bsonType": "object",
                "required": ["relationship_status", "zodiac", "favorite_food"],
                "properties": {
                    "relationship_status": {
                        "bsonType": "string",
                        "description": "must be a string and is required"
                    },
                    "zodiac": {
                        "bsonType": "string",
                        "description": "must be a string and is required"
                    },
                    "favorite_food": {
                        "bsonType": "string",
                        "description": "must be a string and is required"
                    }
                }
            },
            "channels": {
                "bsonType": "array",
                "items": {
                    "bsonType": "objectId",
                },
                "description": "must be a array of objectid's"
            }
        }
    }
})

handler.database.create_collection("channels")

handler.database.command('collMod', 'channels', validator={
    "$jsonSchema": {
        "bsonType": "object",
        "required": ["name", "type", "meta", "creation_date"],
        "properties": {
            "name": {
                "bsonType": "string",
                "description": "must be a string and is required"
            },
            "type": {
                "bsonType": "string",
                "description": "must be a string and is required"
            },
            "creation_date": {
                "bsonType": "date",
                "description": "must be a date and is required"
            },
            "meta": {
                "bsonType": "object",
                "required": ["archived"],
                "properties": {
                    "archived": {
                        "bsonType": "bool",
                        "description": "must be a boolean and is required"
                    }
                }
            }
        }
    }
})

handler.database.create_collection("comments")

handler.database.command('collMod', 'comments', validator={
    "$jsonSchema": {
        "bsonType": "object",
        "required": ["value", "channel", "user", "likes", "sent_at"],
        "properties": {
            "value": {
                "bsonType": "string",
                "description": "must be a string and is required"
            },
            "channel": {
                "bsonType": "objectId",
                "description": "must be a objectid and is required"
            },
            "user": {
                "bsonType": "objectId",
                "description": "must be a objectid and is required"
            },
            "sent_at": {
                "bsonType": "date",
                "description": "must be a date and is required"
            },
            "likes": {
                "bsonType": "int",
                "description": "must be an int and is required"
            }
        }
    }
})


user_collection = handler.get_collection("users")
channel_collection = handler.get_collection("channels")
comment_collection = handler.get_collection("comments")


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


faker = Faker()

create_channels()

channel_ids = [x["_id"] for x in channel_collection.find({})]
user_collection.insert_many(get_fake_users(channel_ids, 500))

users = [x for x in user_collection.find({})]
channels = [x for x in channel_collection.find({})]

comment_collection.insert_many(get_fake_comments(channels, users))

user_collection.create_index([('ex_jobs.name', TEXT), ('first_name', TEXT)])
