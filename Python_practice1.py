counties = ["Arapahoe", "Denver", "Jefferson"]
if counties[1] == "Denver":
    print(counties[1])
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not in the list of counties.")
if "Arapahoe" in counties and "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties.")
else:
    print("Arapahoe or El Paso is not in the list of counties.")
if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties.")
else:
    print("Arapahoe or El Paso is not in the list of counties.")
if "Arapahoe" in counties and "El Paso" not in counties:
    print("Only Arapahoe is in the list of counties.")
else:
    print("Arapahoe is in the list of counties and El Paso is not in the list of counties.")
for county in counties:
    print(county)
numbers = [0,1,2,3,4]
for num in numbers:
    print(num)
for num in range(5):
     print(num)  
for i in range(len(counties)):
    print(counties[i]) 
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county in counties_dict:
    print(county)
for county in counties_dict.keys():
    print(county)
for voters in counties_dict.values():
    print(voters)
for county in counties_dict:
    print(counties_dict[county])
for county in counties_dict:
    print(counties_dict.get(county))
voting_data = [{"county":"Arapahoe", "registered voters": 422829},
                {"county":"Denver", "registered voters": 463353},
                 {"county":"Jefferson","registered voters": 432438}]
for county_dict in voting_data:
    print(county_dict)
for i in range(len(voting_data)):
    print(voting_data[i]['county'])
for county_dict in voting_data:
    for value in county_dict.values():
        print(value)
for county_dict in voting_data:
    print(county_dict.values())
for county_dict in voting_data:
    print(county_dict["registered voters"])
for county_dict in voting_data:
    print(county_dict['county'])
for county, voters in counties_dict.items():
    print(county + " county has" + str( voters) + " registered voters.")
for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")
candidate_votes = int(3345)(input("How many votes did the candidate get in the election?"))
total_votes = int(23123)(input("What is the total number of votes in the election?"))
message_to_candidate = (
    f"You recieved {candidate_votes} number of votes."
    f"The total number of votes in the election was {total_votes}."
    f"You recieved {candidate_votes / total_votes * 100}% of the total votes.")
print(message_to_candidate)