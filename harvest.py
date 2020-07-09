import json
import requests
from datetime import datetime

# Set constants
fname = str(datetime.now().strftime('%Y%m%d%H%M')) + ".tsv" # Filename is current time and date
baseURL = "https://api.semanticscholar.org/v1/paper/"
unKnown = "?include_unknown_references=true" # Includes unknown references

# Build URL
id = input("Semantic Scholar ID: ") # Get ID from user
url = baseURL + id + unKnown

# Get Record and convert to JSON
response = requests.get(url)
record = json.loads(response.text)

# Identify Citations
citations = record["citations"]

# Write Citations to file
f = open(fname, "a", encoding="utf-8")
f.write("Data for Semantic Scholar ID " + id + " produced on " + str(datetime.now().strftime('%Y%m%d%H%M')) + "\n")
f.write("doi\ttitle\tauthors\tyear\tpaperId\tintent\tisInfluential\turl\tvenue\tarxivId\n")

for cite in citations:
    text = str(cite["doi"]) + "\t" + str(cite["title"]) + "\t" + str(cite["authors"]) + "\t" + str(cite["year"]) + "\t" + str(cite["paperId"]) + "\t" + str(cite["intent"]) + "\t" + str(cite["isInfluential"]) + "\t" + str(cite["url"]) + "\t" + str(cite["venue"]) + "\t" + str(cite["arxivId"]) + "\n"
    f.write(text)

f.close() # close file

exit()
