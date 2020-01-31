import os
import shutil
import numpy as np
img_folder_path = 'C:/Masterarbeit/No_Score_v2/'
path = img_folder_path
files = []

# AverageAcceleration - Delete Zero Values
AverageAcceleration_list = []
i = 0
for r, d, f in os.walk(path):
    for file in f:
        if 'trips.json' in file:
            import json
            joined_path = os.path.join(r,file)
            with open(joined_path) as read_file:
                datatime = json.load(read_file)
                thingID_list = datatime.get('thingID', None)
                AverageAcceleration = datatime.get('AverageAcceleration', None)
                AverageAcceleration = float(AverageAcceleration)
                if AverageAcceleration > 0.0:
                    AverageAcceleration.append(AverageAcceleration)
                if AverageAcceleration == 0.0:
                    print(str(thingID_list) + " with AverageAcceleration with: " + str(AverageAcceleration))
                    i = i + 1
                    
i = str(i)
print("Count is: " + i)
m1 = np.mean(AverageAcceleration_list, dtype=np.float64)
m1 = str(m1)
print("Mean of AverageAcceleration is: " + m1)

# MaximumAcceleration in G - over 3G it doesn't make sense
MaximumAcceleration_list = []
i = 0
for r, d, f in os.walk(path):
    for file in f:
        if 'trips.json' in file:
            import json
            joined_path = os.path.join(r,file)
            with open(joined_path) as read_file:
                datatime = json.load(read_file)
                thingID_list = datatime.get('thingID', None)
                MaximumAcceleration = datatime.get('MaximumAcceleration', None)
                MaximumAcceleration = float(MaximumAcceleration)
                if MaximumAcceleration < 3.0:
                    MaximumAcceleration.append(MaximumAcceleration)
                if MaximumAcceleration >= 3.0:
                    print(str(thingID_list) + " with MaximumAcceleration with: " + str(MaximumAcceleration))
                    #datatime['MaximumAcceleration'] = '42.0'
                    i = i + 1
                    #with open(joined_path, 'w') as write_file:
                        #string_json = datatime
                        #new_data = json.dump(string_json, write_file)
                    
i = str(i)
print("Count is: " + i)
m2 = np.mean(MaximumAcceleration_list, dtype=np.float64)
m2 = str(m2)
print("Mean of MaximumAcceleration is: " + m2)

#MaximumDeceleration in G - over 3G it doesn't make sense
MaximumDeceleration_list = []
i = 0
for r, d, f in os.walk(path):
    for file in f:
        if 'trips.json' in file:
            import json
            joined_path = os.path.join(r,file)
            with open(joined_path) as read_file:
                datatime = json.load(read_file)
                thingID_list = datatime.get('thingID', None)
                MaximumDeceleration = datatime.get('MaximumDeceleration', None)
                MaximumDeceleration = float(MaximumDeceleration)
                if MaximumDeceleration < 3.0:
                    MaximumDeceleration.append(MaximumDeceleration)
                if MaximumDeceleration >= 3.0:
                    print(str(thingID_list) + " with MaximumDeceleration with: " + str(MaximumDeceleration))
                    #datatime['MaximumDeceleration'] = '42.0'
                    i = i + 1
                    #with open(joined_path, 'w') as write_file:
                        #string_json = datatime
                        #new_data = json.dump(string_json, write_file)
                    
i = str(i)
print("Count is: " + i)
m3 = np.mean(MaximumDeceleration_list, dtype=np.float64)
m3 = str(m3)
print("Mean of MaximumDeceleration is: " + m3)

#AverageSpeed - Delete Zero Values
AverageSpeed_list = []
i = 0
for r, d, f in os.walk(path):
    for file in f:
        if 'trips.json' in file:
            import json
            joined_path = os.path.join(r,file)
            with open(joined_path) as read_file:
                datatime = json.load(read_file)
                thingID_list = datatime.get('thingID', None)
                AverageSpeed = datatime.get('AverageSpeed', None)
                AverageSpeed = float(AverageSpeed)
                if AverageSpeed > 0.0:
                    AverageSpeed.append(AverageSpeed)
                if AverageSpeed == 0.0:
                    print(str(thingID_list) + " with AverageSpeed with: " + str(AverageSpeed))
                    i = i + 1
                    
i = str(i)
print("Count is: " + i)
m4 = np.mean(AverageSpeed_list, dtype=np.float64)
m4 = str(m4)
print("Mean of AverageSpeed is: " + m4)

#MaxSpeed in kmh - over 250
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
                    #datatime['MaxSpeed'] = '176.26079706519926'
                    i = i + 1
                    #with open(joined_path, 'w') as write_file:
                        #string_json = datatime
                        #new_data = json.dump(string_json, write_file)
i = str(i)
print("Count is: " + i)
m5 = np.mean(MaxSpeed_list, dtype=np.float64)
m5 = str(m5)
print("Mean of MaxSpeed is: " + m5)

#CountHardAccelerations - over 800 doesn't make sense
CountHardAccelerations_list = []
i = 0
for r, d, f in os.walk(path):
    for file in f:
        if 'trips.json' in file:
            import json
            joined_path = os.path.join(r,file)
            with open(joined_path) as read_file:
                datatime = json.load(read_file)
                thingID_list = datatime.get('thingID', None)
                CountHardAccelerations = datatime.get('CountHardAccelerations', None)
                CountHardAccelerations = float(CountHardAccelerations)
                if CountHardAccelerations < 800.0:
                    CountHardAccelerations.append(CountHardAccelerations)
                if CountHardAccelerations >= 800.0:
                    print(str(thingID_list) + " with CountHardAccelerations with: " + str(CountHardAccelerations))
                    #datatime['CountHardAccelerations'] = '42.0'
                    i = i + 1
                    #with open(joined_path, 'w') as write_file:
                        #string_json = datatime
                        #new_data = json.dump(string_json, write_file)
i = str(i)
print("Count is: " + i)
m6 = np.mean(CountHardAccelerations_list, dtype=np.float64)
m6 = str(m6)
print("Mean of CountHardAccelerations is: " + m6)

#CountHardDecelerations - over 600 doesn't make sense
CountHardDecelerations_list = []
i = 0
for r, d, f in os.walk(path):
    for file in f:
        if 'trips.json' in file:
            import json
            joined_path = os.path.join(r,file)
            with open(joined_path) as read_file:
                datatime = json.load(read_file)
                thingID_list = datatime.get('thingID', None)
                CountHardDecelerations = datatime.get('CountHardDecelerations', None)
                CountHardDecelerations = float(CountHardDecelerations)
                if CountHardDecelerations < 600.0:
                    CountHardDecelerations.append(CountHardDecelerations)
                if CountHardDecelerations >= 600.0:
                    print(str(thingID_list) + " with CountHardDecelerations with: " + str(CountHardDecelerations))
                    #datatime['CountHardDecelerations'] = '42.0'
                    i = i + 1
                    #with open(joined_path, 'w') as write_file:
                        #string_json = datatime
                        #new_data = json.dump(string_json, write_file)
i = str(i)
print("Count is: " + i)
m7 = np.mean(CountHardDecelerations_list, dtype=np.float64)
m7 = str(m7)
print("Mean of CountHardDecelerations is: " + m7)

#zu kleine Zahl für SmartPLS 56cdb1c3404c63bf1fb43391 bei HardDecelerationsKM
#delete AverageRPM = 0
#AverageRPM lower than 1000.0 doesn't make sense
AverageRPM_list = []
i = 0
for r, d, f in os.walk(path):
    for file in f:
        if 'trips.json' in file:
            import json
            joined_path = os.path.join(r,file)
            with open(joined_path) as read_file:
                datatime = json.load(read_file)
                thingID_list = datatime.get('thingID', None)
                AverageRPM = datatime.get('AverageRPM', None)
                AverageRPM = float(AverageRPM)
                if AverageRPM >= 1000.0:
                    AverageRPM.append(AverageRPM)
                if (AverageRPM < 1000.0 and AverageRPM > 0.0):
                    print(str(thingID_list) + " with AverageRPM with: " + str(AverageRPM))
                    #datatime['AverageRPM'] = '42.0'
                    i = i + 1
                    #with open(joined_path, 'w') as write_file:
                        #string_json = datatime
                        #new_data = json.dump(string_json, write_file)
i = str(i)
print("Count is: " + i)
m8 = np.mean(AverageRPM_list, dtype=np.float64)
m8 = str(m8)
print("Mean of AverageRPM is: " + m8)

#MaxRPM higher than 12000
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
                MaxRPM = float(MaxRPM)
                if MaxRPM < 12000.0:
                    MaxRPM.append(MaxRPM)
                if MaxRPM >= 12000.0:
                    print(str(thingID_list) + " with MaxRPM with: " + str(MaxRPM))
                    #datatime['MaxRPM'] = '42.0'
                    i = i + 1
                    #with open(joined_path, 'w') as write_file:
                        #string_json = datatime
                        #new_data = json.dump(string_json, write_file)
i = str(i)
print("Count is: " + i)
m9 = np.mean(MaxRPM_list, dtype=np.float64)
m9 = str(m9)
print("Mean of MaxRPM is: " + m9)

#AverageSpeedTrip
