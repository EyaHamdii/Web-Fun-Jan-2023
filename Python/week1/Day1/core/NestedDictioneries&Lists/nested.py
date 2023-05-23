#1
x = [ [5,2,3], [10,8,9] ] 
x[1][0]=5
print(x)
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
students[0]['last_name'] = 'Bryant'
print(students)
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
sports_directory['soccer'][0]='Andres'
print(sports_directory)
z = [ {'x': 10, 'y': 20} ]
z[0]['y']=30
print(z)
#2
def iterateDictionary(students):
    for dictionary in students:
        for key, value in dictionary.items():
            print(f"{key}: {value}")
students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
iterateDictionary(students)



#3
def iterateDictionary2(first_name, students):
    for dictionary in students:
        if first_name in dictionary:
            print(dictionary[first_name])
def iterateDictionary2(last_name, students):
    for dictionary in students:
        if last_name in dictionary:
            print(dictionary[last_name])

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
iterateDictionary2('first_name',students)
iterateDictionary2('last_name',students)

#4
def printInfo(dojo):
    for key, value in dojo.items():
        print(f"{key} - {len(value)}")
        for item in value:
            print(item)
        print()


dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
printInfo(dojo) 





