from src.utils.parsers import populate_database, parse_colors, add_media, fetch_objects_that_needed_color_reading
from src.utils.sparql_harvester import sparql_harvester
from crontab import CronTab

# define objects to parse and extract colors here.
#_objects = ["1987-0885", "1987-0887_0-2", "1987-0970_00-12", "1987-0971", "1987-0838", "1987-0839", "1987-0842", "1987-0881", "1987-1015", "1987-1068", "1987-1012", "1987-0958", "1987-1033", "1987-1024", "1983-0055", "2007-0004_1-4", "2007-0012", "2007-0013", "2008-0027", "DES.1995.25", "1992-0069", "1992-0071", "1992-0074", "1992-0076", "1992-0101", "1992-0143", "1992-0148", "1992-0158", "1414", "1432", "1987-1477", "FH-0071", "FH-0085", "FH-0086", "1987-1199", "2001-0004_0-2", "2001-0004_1-2", "2001-0004_2-2", "2005-0047", "3228", "0019", "0829", "1933", "1984-0025", "1988-0004", "1994-0040", "2017-0107", "3162", "3190_1-2", "3191", "3291_0-2", "3295_0-2", "3322", "3938"]

def main():

    ## fetch only objects that have images (but are missing colors)
    _objects = fetch_objects_that_needed_color_reading()

    ## 2. fetch licences - if no licence --> set to "PERMISSION DENIED".
    #populate_database(_objects) #todo: only check for new items. Don't rerun whole thing.

    ## 3. parse colors;
    parse_colors(_objects)

def update():
    add_media()

main();
#update();

