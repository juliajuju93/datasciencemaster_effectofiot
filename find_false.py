import os
import json
img_folder_path = 'C:/Masterarbeit/No_Score/'
path = img_folder_path
files = []
i = 0

for r, d, f in os.walk(path):
    for file in f:
        if 'trips.json' in file:
            import json
            joined_path = os.path.join(r,file)
            with open(joined_path) as read_file:
                data = json.load(read_file)
                ID = data.get('thingID', None)
                if ID:
                    print(f'thingID is {ID}')
                else:
                    print('thingID is unknown.')
                                
