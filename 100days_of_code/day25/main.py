# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)
    
# import csv

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)   #create a csv object
#     tempertures = []
#     for row in data :
#         if row[1] != "temp":
#             tempertures.append(int(row[1])  )
        
#     print(tempertures)
    
    
import pandas

data = pandas.read_csv("weather_data.csv")
# # print(data)
# print(data["temp"])

# dict_data =data.to_dict() # Dataframe to dictionary
# print(dict_data)

# temp_list = data["temp"].to_list() #Series to list
# print(temp_list)

# len_temp = (len(temp_list))
# total_temp = 0
# for temp in temp_list:
#     total_temp+=temp
# avg_temp = total_temp/len_temp
# print(avg_temp)

# average_temp = sum(temp_list)/len(temp_list)
# print(average_temp)

# temp_mean = data["temp"].mean()
# print(temp_mean)

# temp_max = data["temp"].max()
# print(temp_max)

#Get Data in Columns
# print(data["condition"])
# print(data.condition)

#Get Data in row
# print(data[data.day == "Monday"])

#get the row which have highest temperture
# print(data[data.temp == temp_max])

# monday = data[data.day == 'Monday']
# print(monday.condition)
# mon_temp = monday.temp
# mon_temp_fahren =(mon_temp*9/5)+32
# print(mon_temp_fahren)


#Create a dataframe from scratch
data_dict_mark = {
    "student":["subham","sipu","ajit","nikhil","chiku"],
    "scores":[67,78,89,87,76]
}

mark_data = pandas.DataFrame(data_dict_mark)
print(mark_data)
#save into a csv file
mark_data.to_csv("new_mark_data.csv")
