#dictionary in a dictionary
'''
{
    key:[list],
    key:{dictionary}
}
'''
capitals = {
"Russia" : "Moscow",
"United Kingdom" : "London",
"Germany" : "Berlin",
}

#Nesting a list in a dictionary
travel_log = {
    "France":["paris","Little","Dijon"],
    "Germany":["Berlin","Hamburg"],
}

#list with in a list
# ["A","B","C",["D","F"]]

#Nesting Dictionary in a Dictionary
travel_log = {
    "France":{"cities_visited":["paris","Little","Dijon"],
              "total_visits":12},
    "Germany":{"cities":["Berlin","Hamburg","Stuttgart"],
               "total_visits":5},
}

#dictionaries in a list
'''
[{
    key:[list],
    key:{dictionary}
},
{
    key:Value,
    key:Value,
}]
'''
travel_log =[
    {
   "country":"France",
   "cities_visited":["paris","Little","Dijon"],
   "total_visits":12
   },
    
    {
    "country":"Germany",
    "cities":["Berlin","Hamburg","Stuttgart"],
    "total_visits":5
    },

]
