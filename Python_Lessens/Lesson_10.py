person = {
	'user_1': {
		 'name': 'Bob',
		 'age': 23,
		 'adress': ('г. Москва', 'ул. Какая-то'),
		 'grades': {
			 'math': 5,
			 'phythics': 4
		 }
    },

    'user_2': {
        'name': 'Joy'
    }
}
print (person['user_1']['adress'][0:2])

person1 = dict(user_2=
               dict(name='Joy', age=23),
               user_3=person)
print (person1['user_2']['name'])

for key, value in person1.items():
    print(key, end= " ")


country = {'code': ['RU', 'BY'], 'name': 'Russia', 'population': 234}

print('\n', country.get('code'))
# country.clear()
country.popitem()
print('\n', country)
print(country.keys())
print(country.values())
print(country.items())
country.update({'V': '34543 м^2'})
print('\n', country)

