from pymongo import DESCENDING
from mongo_handler import MongoHandler
from datetime import datetime

handler = MongoHandler("ecbd")
user_collection = handler.get_collection("users")
channel_collection = handler.get_collection("channels")
comment_collection = handler.get_collection("comments")


def print_output_separator():
    print("\n\n#####################################")


# toate comentariile trimise mai tarziu de 01.01.2020
print(list(comment_collection.find(
    {
        "sent_at": {"$lt": datetime(year=2020, month=1, day=1, hour=0, minute=0, second=0).replace(microsecond=0)}
    }
).limit(5)))

# toate comentariile cu cel putin 300 like-uri (limita de 5 pt a fi citite rezultate partiale)
print_output_separator()
print(list(comment_collection.find({"likes": {"$gte": 300}}, {"value": 1})))

# toti angajatii cu zodia gemeni (limita de 5 pt a fi citite rezultate partiale)
print_output_separator()
print(list(user_collection.find({"personal_information.zodiac": "Gemini"}, {"first_name": 1, "last_name": 1})))

# toti angajatii care sunt divortati si sunt pe canalul #hr-iasi
print_output_separator()
hr_iasi_id = channel_collection.find_one({"name": "#hr-iasi"})["_id"]

print(list(user_collection.find(
    {
        "personal_information.relationship_status": "divorced",
        "channels": hr_iasi_id
    },
    {
        "first_name": 1,
        "last_name": 1,
        "personal_information.zodiac": 1
    }
)))

# toti angajatii al caror prenume incepe cu "An" si si al caror nume incepe cu 'I'
print_output_separator()
print(list(user_collection.find({"first_name": {"$regex": r"An\w+"}, "last_name": {"$regex": r"I\w+"}})))

# toate canalele arhivate
print_output_separator()
print(list(channel_collection.find({"meta.archived": True})))

# cautare + index
print_output_separator()
print(list(user_collection.find({"$text": {"$search": "Adrian"}})))

# primele 100 comentarii dupa nr like-uri
print_output_separator()
print(list(comment_collection.find({})
                             .sort("likes", DESCENDING)
                             .limit(100)))

# comentariul cu cel mai mare nr de like-uri
print_output_separator()
print(list(comment_collection.find({}, {"value": 1, "likes": 1})
                             .sort("likes", DESCENDING)
                             .limit(1)))

# comentariile de la 100 la 200 (posibila utilizare in paginare)
print_output_separator()
print(list(comment_collection.find({})
                             .skip(100)
                             .limit(100)))

# angajatii care au avut functia de: Proiectant Sisteme De Securitate
print_output_separator()
print(list(user_collection.find(
    {
        "ex_jobs.name": {"$regex": "Sisteme De Securitate"}
    },
    {
        "first_name": 1,
        "last_name": 1
    }
)))

