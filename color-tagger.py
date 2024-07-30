from src.utils.parsers import parse_colors, add_media, fetch_objects_that_needed_color_reading

def main():

    update()

    ## fetch only objects that have images (but are missing colors)
    _objects = fetch_objects_that_needed_color_reading()

    ## 3. parse colors;
    parse_colors(_objects)

def update():
    add_media()

main(); ## add colors if needed.


