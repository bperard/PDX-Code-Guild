'''
lab 29 road trippin'
'''
# dict with keys as possible cities, values are a set of cities connected with roads to key city
city_to_accessible_cities = {
  'Boston': {'New York', 'Albany', 'Portland'},
  'New York': {'Boston', 'Albany', 'Philadelphia'},
  'Albany': {'Boston', 'New York', 'Portland'},
  'Portland': {'Boston', 'Albany'},
  'Philadelphia': {'New York'}
}

# prompt user and convert user text to title for proper match with keys
print('Choose a city, and I will tell you which cities are directly accessible by road.')
hub = input('Choose "Boston", "New York", "Albany", "Portland", or "Philadelphia":').title()
if hub in city_to_accessible_cities:    # if user input is a key, print values for one hop
    print('You can jump to the following cities in one hop:\n'
          + str(city_to_accessible_cities[hub]))
    two_hops = city_to_accessible_cities[hub]
    for city in city_to_accessible_cities[hub]:    # iterate through values in linked to hub city key, set values as key and add unique values to two_hops dict
        two_hops = two_hops | city_to_accessible_cities[city]
    print('You can jump to the following cities in two hops:\n'
          + str(two_hops))
else:    # user fail
    print(hub + ' is not a valid choice.\n'
                'You have now been added to the No Fly List.')