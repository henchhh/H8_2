MLB_team = {
    'Colorado': 'Rockies', 
    'Boston': 'Red Sox', 
    'Minnesota': 'Twins',
    }
print(MLB_team['Minnesota'])
#Adding an entry to an existing dictionary
MLB_team['Kansas City'] = 'Royals'
print(MLB_team['Kansas City'])
print(MLB_team)
print(list(MLB_team))
del MLB_team['Kansas City']
print(MLB_team)

for key,value in MLB_team.items():
    print(key,value)