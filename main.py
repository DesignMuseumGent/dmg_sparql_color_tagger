from src.utils.parsers import populate_database, parse_colors

def fetch_colors():
    _df = populate_database() ## fetch
    #fetch_images_from_manifest(_df)
    return _df

## 1. run harvester (weekly)
#sparql_harvester()

## 2.  fetch colors;
#populate_database()

## 3. parse colors:
parse_colors()


#df.to_csv("src/data/20230212_manifest_data.csv")
#x = parse_colors(df)
#x.to_csv("src/data/20230212_color_data.csv")
#generate_json("src/data/20230212_color_data.csv")