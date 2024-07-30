from src.utils.parsers import populate_database, parse_colors, add_media, fetch_objects_that_needed_color_reading

def main():

    update()

    ## fetch only objects that have images (but are missing colors)
    _objects = fetch_objects_that_needed_color_reading()

    ## 2. fetch licences - if no licence --> set to "PERMISSION DENIED".
    #populate_database() #todo: only check for new items. Don't rerun whole thing.

    ## 3. parse colors;
    parse_colors(_objects)

def update():
    add_media()

main(); ## add colors if needed.


