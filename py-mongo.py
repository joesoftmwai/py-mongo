
import pymongo
from pymongo import MongoClient

client  = MongoClient('mongodb+srv://test:test@cluster0-9iade.mongodb.net/test?retryWrites=true&w=majority')
db      = client.get_database('play_station_db')
records = db.player_details

# count number of documents
countDoc =  records.count_documents({})
# print(str(countDoc) + ' records found')


# CREATE document
player_1 = {
    'pd_name': 'Mwas',
    'pd_position': 'Midfielder',
    'pd_jersey_no': 23
}

# records.insert_one(player_1)

# create multiple documents
players = [
    {
    'pd_name': 'Archaf',
    'pd_position': 'right-back',
    'pd_jersey_no': 5
    },
    {
    'pd_name': 'Ziyech',
    'pd_position': 'Midfielder',
    'pd_jersey_no': 10
    }
]

# records.insert(players)

# READ document(s)
# print(list(records.find()))

# read specific document
# print(list(records.find({'pd_name': 'Archaf'})))

# UPDATE document
player_update = {
    'pd_name': 'Upamencano',
    'pd_position': 'center-back',
    'pd_jersey_no': 5
}

# records.update({'pd_jersey_no': 7}, {'$set': player_update})

# DELETE document
_del = records.delete_one({'pd_name':'Mwas'})

# if _del :
#     print('Deleted successfully')
# else :
#     print('Error occurred')

_records = list(records.find({'pd_name': 'Ziyech'}))
print(_records)





