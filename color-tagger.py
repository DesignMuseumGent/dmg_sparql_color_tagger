from src.utils.parsers import parse_colors, add_media, fetch_objects_that_needed_color_reading
from concurrent.futures import ThreadPoolExecutor
import logging

def main():

    try:
        logging.info("fetching objects")
        _objects = fetch_objects_that_needed_color_reading()
        ## 3. parse colors;
        logging.info("parsing colors")
        parse_colors(_objects)

        #update()
    except Exception as e:
        logging.error(f"failed to update: {e}")


def update():
    add_media()

#main()
update()
main()