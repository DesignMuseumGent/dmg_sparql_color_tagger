from src.utils.parsers import populate_database, parse_colors
from src.utils.sparql_harvester import sparql_harvester
from crontab import CronTab
def main():
    ## 1. run harvester (weekly)
    sparql_harvester() #todo: make that it only puts in new versions if already existent

    ## 2.  fetch colors;
    populate_database() #todo: only check for new items. Don't rerun whole thing.

    ## 3. parse colors:
    parse_colors()


main()

