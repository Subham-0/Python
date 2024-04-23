weather_c = {"Monday":12,"Thesday":14,"Wednesday":15,"Thursday":14,"friday":21,"Saturday":22,"Sunday":24}

weather_f = {day:cel*9/5+32 for (day,cel) in weather_c.items()}

print(weather_f)