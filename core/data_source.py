from collections import defaultdict
from pymongo import MongoClient
from core.country_code_convertor import country_codes

# Connect to database.
client = MongoClient()
db = client.world_bank

# Take all projects from data.
projects = db.world.find()

# Creating of structure of needed data to pass it on DataMaps. It includes name and cost of projects for each country 
#    and summary projects costs by countries.
projects_by_countries = defaultdict(lambda: {'projects':[], 'summary': 0})

for project in projects:
    if project['countrycode'] in country_codes.keys(): 
        three_char_country_code = country_codes[project['countrycode']]
        current_contry_code = projects_by_countries[three_char_country_code]
        current_contry_code['projects'].append(
            {'project_name': project['project_name'],
             'lendprojectcost': project['lendprojectcost']})
        current_contry_code['summary'] += project['lendprojectcost']