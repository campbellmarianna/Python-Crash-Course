transport = ['ferry', 'scooter', 'bike', 'walk', 'run', 'electric car']
ferry_message = 'I would like to take the '+ transport[0] + ' regularly during my work week, particularly during the end and beginning of my work days.'
scooter_message = transport[1].title() + 's' + ' are useful for trips to the store and longer distant computes still within the area.'
bike_message = transport[2].title() + 's' + ' are useful for traveling with the city.'
walk_message = transport[3].title() + 'ing' + ' is good for seeing the city and when traveling shorter distances.'
run_message = transport[4].title() + 'ning' + ' is good for exercise and can make getting somewhere that is a short distance away faster.'
car_message = "If an " + transport[5] + " doesn't negatively impacts the environment I will use it for long distance traveling."
print(ferry_message)
print(scooter_message)
print(bike_message)
print(walk_message)
print(run_message)
print(car_message)
