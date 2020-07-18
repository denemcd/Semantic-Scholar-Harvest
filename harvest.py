import json
import requests
from datetime import datetime

# Set constants
baseURL = "https://api.semanticscholar.org/v1/paper/"
unKnown = "?include_unknown_references=true" # Includes unknown references

# Build URL
id = input("Semantic Scholar ID: ") # Get ID from user
if id == "":
    id = "d4b651d6a904f69f8fa1dcad4ebe972296af3a9a"
    print("No ID entered. Using test ID d4b651d6a904f69f8fa1dcad4ebe972296af3a9a")

url = baseURL + id + unKnown

# Get Record and convert to JSON
print("Trying: " + url)
response = requests.get(url)
record = json.loads(response.text)
print("Success")
# Identify Citations
try:
    citations = record["citations"]
except:
    print("Error, check Scholar ID")
    exit()

# Write Citations to file
fname = str(id + "_" + datetime.now().strftime('%Y%m%d%H%M')) + ".tsv" # Filename is current time and date
f = open(fname, "a", encoding = "UTF-8")
f.write("doi\ttitle\tauthors\tyear\tpaperId\tintent\tisInfluential\turl\tvenue\tarxivId\n")

for tags in citations:
    #Identfy author names and clean them
    authorslist = ""
    authors = tags["authors"]
    for author in authors:
        authorslist = authorslist + author["name"] + ";"

    #Write all tags to the file
    text = str(tags["doi"]) + "\t" + str(tags["title"]) + "\t" + authorslist + "\t" + str(tags["year"]) + "\t" + str(tags["paperId"]) + "\t" + str(tags["intent"]) + "\t" + str(tags["isInfluential"]) + "\t" + str(tags["url"]) + "\t" + str(tags["venue"]) + "\t" + str(tags["arxivId"]) + "\n"
    f.write(text)

f.close() # close file

exit()
