#Problem-2: fill letter teplate with name and date.
name = "Kartik"
date = "27-07-2025"

print(f"Dear {name}\n You are selected! \n {date}\n")


# USING REPLACE

letter = ''' Dear (Name),
You are selected!
(Date)
'''
print(letter.replace("Name","Kartik").replace("Date","27-07-2025"))
