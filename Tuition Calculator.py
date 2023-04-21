#This program will calculate the amount of tuition that increases by 3% for 5 years
#Pedro Ayala

tuition = 16000      #Initialize semester tuition
multiplier = 1      #Initialize multiplier to 1

#Loop to calculate tuition for the next 5 years for each semester
for i in range(1, 5):
    print ("year: ", i, "Estimated tuition: $", tuition)   #display semester and tuition
    multiplier = tuition * 0.03             #multiplier by 3%
    tuition = tuition + multiplier          #yearly tuition calculator
