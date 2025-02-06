from src.utils.parsers import parse_colors, add_media, fetch_objects_that_needed_color_reading

def main():

    try:
        print("start")
        #update()
    except Exception as e:
        print(f"failed to update: {e}")

    try:
        ## fetch only objects that have images (but are missing colors)
        _objects = fetch_objects_that_needed_color_reading()
        ## 3. parse colors;
        parse_colors(_objects)
    except Exception as e:
        print(f"failed to parse colors: {e}")

def update():
    add_media()

#main()
main()