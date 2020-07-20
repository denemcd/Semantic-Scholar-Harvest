import json
import requests
from datetime import datetime

# Set constants and default values
baseURL = "https://api.semanticscholar.org/v1/paper/"
unKnown = "?include_unknown_references=true" # Includes unknown references
count = 0

# Get Semantic Scholar ID
id = input("Semantic Scholar ID: ") # Get ID from user
if id == "":
    id = "f2c85749099eeefbd0b36d9fb8868dfa827628b4" # If the user doen't enter an ID use default (makes testing easier)
    print("No ID entered. Using test ID f2c85749099eeefbd0b36d9fb8868dfa827628b4")

url = baseURL + id + unKnown # Build URL

# Query API and convert to JSON
print("Trying: " + url)
response = requests.get(url)
record = json.loads(response.text)

# Identify Citations
try:
    citations = record["citations"]
    print("Success")
except:
    print("Error:", record["error"])
    exit()

# Write Citations to file
fname = str(id + "_" + datetime.now().strftime('%Y%m%d%H%M')) + ".csv" # Filename is current time and date

with open(fname, "w", encoding="UTF-8") as f:
    f.write("doi\ttitle\tauthors\tyear\tpaperId\tintent\tisInfluential\turl\tvenue\tarxivId")

    for tags in citations:
        
        #Identfy author names and clean them
        authorslist = ""
        authors = tags["authors"]
        for author in authors:
            authorslist = authorslist + author["name"] + ";"
        
        #Identfy intent field and clean
        intentlist = ""
        intent = tags["intent"]
        for intentField in intent:
            intentlist = intentlist + intentField + ";"

        #Write all tags to the TSV file
        text = "\n" + str(tags["doi"]) + "\t" + str(tags["title"]) + "\t" + authorslist + "\t" + str(tags["year"]) + "\t" + str(tags["paperId"]) + "\t" + str(intentlist) + "\t" + str(tags["isInfluential"]) + "\t" + str(tags["url"]) + "\t" + str(tags["venue"]) + "\t" + str(tags["arxivId"])
        f.write(text)
        count+=1

print(str(count), " citation(s) written to file")
exit()
