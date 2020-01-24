import os
img_folder_path = 'C:/Masterarbeit/No_Score/'
path = img_folder_path
dirListing = os.listdir(img_folder_path)
print(len(dirListing))
files = []
for r, d, f in os.walk(path):
    for file in f:
        if '.json' in file:
            #print(os.path.join(r, file))
            way1 = os.path.join(r,file)
            a = os.path.getsize(way1)
        if a == 2:
            #print(os.path.getsize(way1))
            os.remove(os.path.join(r, file))

        if 'thing.json' in file:
            os.remove(os.path.join(r, file))

    for file in d:
        #print(os.path.join(r, file))
        b = os.path.join(r, file)
        if not os.listdir(b):
            os.rmdir(b)
dirListing = os.listdir(img_folder_path)
print(len(dirListing))
