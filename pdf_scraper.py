import tabula

#read the pdf detailing vaccination availability into a csv table
file = "https://dshs.texas.gov/news/updates/COVIDVaccineAllocation-Week11.pdf"
tables = tabula.read_pdf(file, pages="all", multiple_tables=True)
tabula.convert_into(file, "allTables.csv", pages='all')

# make a allTables - Copy.csv to make the following changes
# manually clean the data to compensate for rows that are not correctly sorted into columns
# delete the columns 'County', 'Pfizer', and 'Moderna'
# delete the first row
# manually enter phone numbers for each location