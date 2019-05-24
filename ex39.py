# create a mapping of state to abbreviation
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

# create a basic set of states amd some cities in them
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

# add some more cities
# Created variables to turn abbreviation into full words
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
# This will print out a hyphen 10 times
print('-' * 10)
# Print out Cities of that state
print("NY State has: ", cities['NY'])
print("OR State has: ", cities['OR'])

# print some states 
print('-' * 10)
# This will print out the abbreviation
print("Michigan's abbreviation is: ", states['Michigan'])
print("Florida's abbreviation is: ", states['Florida'])

# do it by using the states then cities dict
print('-' * 10)
# This will print out the City of the state the City is in
print("Michigan has: ", cities[states['Michigan']])
print("Florida has: ", cities[states['Florida']])

# print every state abbreviation
print('-' * 10)
# This will list the state and the abbreviation of the state
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")
    
# print every city in state
print('-' * 10)
# List the abbreviation of the state and it will list the cities next to it
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")
    
# now do both at the same time
print('-' * 10)
# It will list the abbreviation of the state, the state, and it will list the cities in the state
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and has city {cities[abbrev]}")
    
print('-' * 10)
# safely get a abbreviation by state that might not be there
state = states.get('Texas')

if not state:
    print("Sorry, no Texas.")
    
# get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print(f"The city for the states 'TX' is: {city}")
