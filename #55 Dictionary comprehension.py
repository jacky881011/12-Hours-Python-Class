#55 Dictionary comprehension
# Dictionary comprehension = create dicitonaries using an expression 
#                            can replace for loops and certain lamda funciton 
#                            dictionary = {key : expression for ( key , value ) in iterable}
#                            dictionary = {key : expression for ( key , value ) in iterable if conditional}


# 1 type
cities_in_F = { 'New York': 32, 
           'Bosion': 75, 
           'Los Angeles': 100, 
           'Chicago': 50}

cities_in_c = { key : round(((value-32)*(5/9))) for (key,value) in cities_in_F.items()}         # use round because we want to let the values be clrealy

print(cities_in_c)

# 2 type
weather = {'New York': 'snowing', 'Boston': "sunny", "Los Angeles" : "sunny", "Chicago" : "cloudy" }

cities_sunny = {key : value for (key,value) in weather.items() if value=="sunny"}

print(cities_sunny)

# 3 type 
cities_in_F = { 'New York': 32, 
           'Bosion': 75, 
           'Los Angeles': 100, 
           'Chicago': 50}

cities_select = {key : ("Warm "if value >= 40 else "Cloud") for (key,value) in cities_in_F.items() }
print(cities_select)


# 4 type 
def check_tem(value):
    if value >=40 :
        return "Warm"
    elif value >=30 and value <40:
        return "Cloud"
    else:
        return "Cold"

cities_in_F = { 'New York': 32, 
           'Bosion': 75, 
           'Los Angeles': 100, 
           'Chicago': 20}

cities_choice = {key : check_tem(value) for (key,value) in cities_in_F.items()}
print(cities_choice)

