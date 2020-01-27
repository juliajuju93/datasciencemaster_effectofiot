import os
import shutil
import numpy as np
img_folder_path = 'C:/Masterarbeit/No_Score/'
path = img_folder_path
files = []
MaxSpeed_list = []
i = 0
for r, d, f in os.walk(path):
    for file in f:
        if 'trips.json' in file:
            import json
            joined_path = os.path.join(r,file)
            with open(joined_path) as read_file:
                datatime = json.load(read_file)
                thingID_list = datatime.get('thingID', None)
                MaxSpeed = datatime.get('MaxSpeed', None)
                MaxSpeed = MaxSpeed.split('.')
                MaxSpeed = int(MaxSpeed[0])
                if MaxSpeed < 250:
                    MaxSpeed_list.append(MaxSpeed)
                if MaxSpeed >= 250:
                    print(str(thingID_list) + " with MaxSpeed with: " + str(MaxSpeed))
                    datatime['MaxSpeed'] = '176.26079706519926'
                    i = i + 1
                    with open(joined_path, 'w') as write_file:
                        string_json = datatime
                        new_data = json.dump(string_json, write_file)
i = str(i)
print("Count is: " + i)
m1 = np.mean(MaxSpeed_list, dtype=np.float64)
m1 = str(m1)
print("Mean of MaxSpeed is: " + m1)

MaxRPM_list = []
i = 0
for r, d, f in os.walk(path):
    for file in f:
        if 'trips.json' in file:
            import json
            joined_path = os.path.join(r,file)
            with open(joined_path) as read_file:
                datatime = json.load(read_file)
                thingID_list = datatime.get('thingID', None)
                MaxRPM = datatime.get('MaxRPM', None)
                #MaximumAcceleration = MaximumAcceleration.split('.')
                MaxRPM = float(MaxRPM)
                if MaxRPM < 13000:
                    MaxRPM_list.append(MaxRPM)
                if MaxRPM >= 13000:
                    print(str(thingID_list) + " with MaxRPM with: " + str(MaxRPM))
                    datatime['MaxRPM'] = '4533.152107217827'
                    i = i + 1
                    with open(joined_path, 'w') as write_file:
                        string_json = datatime
                        new_data = json.dump(string_json, write_file)
i = str(i)
print("Count is: " + i)
m2 = np.mean(MaxRPM_list, dtype=np.float64)
m2 = str(m2)
print("Mean of MaxRPM is: " + m2)


