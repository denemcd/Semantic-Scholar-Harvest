import json
import requests
from datetime import datetime
import pandas as pd

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
filename = id + ".xlsx" # Set output filename to the Semantic Scholar ID

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

# Wite Citations to Dataframe

citationdata = pd.DataFrame(columns=["DOI","Title","Authors","Year","PaperID","Intent","IsInfluential","URL","Venue","arxivID"])

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

    #Write all tags to the Dataframe
    citationdata.loc[len(citationdata)] = str(tags["doi"]),str(tags["title"]),authorslist,str(tags["year"]),str(tags["paperId"]),str(intentlist),str(tags["isInfluential"]),str(tags["url"]),str(tags["venue"]),str(tags["arxivId"])
    count+=1

citationdata.to_excel(filename, sheet_name="Scite Data", index=False) # Write Dataframe to Excel File
print(str(count), " citation(s) written to file")

exit()
