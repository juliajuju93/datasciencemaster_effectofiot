import os
import pandas as pd
import numpy as np
import statistics

def extract_element_from_json(obj, path):
    def extract(obj, path, ind, arr):
        key = path[ind]
        if ind + 1 < len(path):
            if isinstance(obj, dict):
                if key in obj.keys():
                    extract(obj.get(key), path, ind + 1, arr)
                else:
                    arr.append(None)
            elif isinstance(obj, list):
                if not obj:
                    arr.append(None)
                else:
                    for item in obj:
                        extract(item, path, ind, arr)
            else:
                arr.append(None)
        if ind + 1 == len(path):
            if isinstance(obj, list):
                if not obj:
                    arr.append(None)
                else:
                    for item in obj:
                        arr.append(item.get(key, None))
            elif isinstance(obj, dict):
                arr.append(obj.get(key, None))
            else:
                arr.append(None)
        return arr
    if isinstance(obj, dict):
        return extract(obj, path, 0, [])
    elif isinstance(obj, list):
        outer_arr = []
        for item in obj:
            outer_arr.append(extract(item, path, 0, []))
        return outer_arr

img_folder_path = 'C:/Masterarbeit/No_Score/'
path = img_folder_path
files = []
for r, d, f in os.walk(path):
    for file in f:
        
        if 'timelines.json' in file:
            import json
            joined_path = os.path.join(r,file)
            with open(joined_path) as read_file:
                datatime = json.load(read_file)
            #Output - General
                #thingId
                thingId = str(datatime[0]['thingId'])
                                                
            #Output - Acceleration behavior
                #AverageAcceleration
                AverageAcceleration_list = extract_element_from_json(datatime, ['maxAccelerationG'])
                df1 = pd.DataFrame(AverageAcceleration_list)
                df1 = np.nan_to_num(df1)
                m1 = np.mean(df1, dtype=np.float64)
                AverageAcceleration = str(m1)
                #MaximumAcceleration
                MaximumAcceleration_list = extract_element_from_json(datatime, ['maxAccelerationG'])
                df2 = pd.DataFrame(MaximumAcceleration_list)
                df2 = np.nan_to_num(df2)
                m2 = np.max(df2)
                MaximumAcceleration = str(m2)
                #PercentileAcceleration
                PercentileAcceleration_list = extract_element_from_json(datatime, ['maxAccelerationG'])
                df3 = pd.DataFrame(PercentileAcceleration_list)
                df3 = np.nan_to_num(df3)
                m3 = np.percentile(df3, 95)
                PercentileAcceleration = str(m3)
                #VarianceAcceleration
                VarianceAcceleration_list = extract_element_from_json(datatime, ['maxAccelerationG'])
                df4 = pd.DataFrame(VarianceAcceleration_list)
                df4 = np.nan_to_num(df4)
                m4 = np.var(df4, dtype=np.float64)
                VarianceAcceleration = str(m4)
                #AverageDeceleration
                AverageDeceleration_list = extract_element_from_json(datatime, ['maxDecelerationG'])
                df5 = pd.DataFrame(AverageDeceleration_list)
                df5 = np.nan_to_num(df5)
                m5 = np.mean(df5, dtype=np.float64)
                AverageDeceleration = str(m5)
                #MaximumDeceleration
                MaximumDeceleration_list = extract_element_from_json(datatime, ['maxDecelerationG'])
                df6 = pd.DataFrame(MaximumDeceleration_list)
                df6 = np.nan_to_num(df6)
                m6 = np.max(df6)
                MaximumDeceleration = str(m6)
                #PercentileDeceleration
                PercentileDeceleration_list = extract_element_from_json(datatime, ['maxDecelerationG'])
                df7 = pd.DataFrame(PercentileDeceleration_list)
                df7 = np.nan_to_num(df7)
                m7 = np.percentile(df7, 95)
                PercentileDeceleration = str(m7)
                #VarianceDeceleration
                VarianceDeceleration_list = extract_element_from_json(datatime, ['maxDecelerationG'])
                df8 = pd.DataFrame(VarianceDeceleration_list)
                df8 = np.nan_to_num(df8)
                m8 = np.var(df8, dtype=np.float64)
                VarianceDeceleration = str(m8)
                
            #Output - Speed behavior
                #AverageSpeedTrips -> from trips.json
                #AverageSpeed
                AverageSpeed_list = extract_element_from_json(datatime, ['averageSpeedKmH'])
                df9 = pd.DataFrame(AverageSpeed_list)
                df9 = np.nan_to_num(df9)
                m9 = np.mean(df9, dtype=np.float64)
                AverageSpeed = str(m9)
                #AverageSpeedZero
                AverageSpeedZero_list = extract_element_from_json(datatime, ['averageSpeedKmH'])
                df10 = pd.DataFrame(AverageSpeedZero_list)
                df10 = np.nan_to_num(df10)
                df10 = np.trim_zeros(df10)
                m10 = np.mean(df10, dtype=np.float64)
                AverageSpeedZero = str(m10)
                #MaxSpeed
                MaxSpeed_list = extract_element_from_json(datatime, ['averageSpeedKmH'])
                df11 = pd.DataFrame(MaxSpeed_list)
                df11 = np.nan_to_num(df11)
                m11 = np.max(df11)
                MaxSpeed = str(m11)
                #VarianceSpeed
                VarianceSpeed_list = extract_element_from_json(datatime, ['averageSpeedKmH'])
                df12 = pd.DataFrame(VarianceSpeed_list)
                df12 = np.nan_to_num(df12)
                m12 = np.var(df12, dtype=np.float64)
                VarianceSpeed = str(m12)
                
            #Output - Extreme acceleration behavior
                #CountHardAccelerations
                CountHardAccelerations_list = extract_element_from_json(datatime, ['countOfHardAccelerations'])
                df13 = pd.DataFrame(CountHardAccelerations_list)
                df13 = np.nan_to_num(df13)
                m13 = np.sum(df13)
                CountHardAccelerations = str(m13)
                #HardAccelerationsKM
                HardAccelerationsKM_list = extract_element_from_json(datatime, ['maxAccelerationG'])
                distanceM_list = extract_element_from_json(datatime, ['distanceM'])
                df14_1 = pd.DataFrame(HardAccelerationsKM_list)
                df14_1 = np.nan_to_num(df14_1)
                m14_1 = np.sum(df14_1)
                m14_1 = int(m14_1)
                df14_2 = pd.DataFrame(distanceM_list)
                df14_2 = np.nan_to_num(df14_2)
                m14_2 = np.sum(df14_2)
                m14_2 = int(m14_2)
                m14_3 = m14_1/m14_2
                HardAccelerationsKM = str(m14_3)
                #CountHardDecelerations
                CountHardDecelerations_list = extract_element_from_json(datatime, ['countOfHardDecelerations'])
                df15 = pd.DataFrame(CountHardDecelerations_list)
                df15 = np.nan_to_num(df15)
                m15 = np.sum(df15)
                CountHardDecelerations = str(m15)
                #HardDecelerationsKM
                HardDecelerationsKM_list = extract_element_from_json(datatime, ['maxDecelerationG'])
                distanceM_list = extract_element_from_json(datatime, ['distanceM'])
                df16_1 = pd.DataFrame(HardDecelerationsKM_list)
                df16_1 = np.nan_to_num(df16_1)
                m16_1 = np.sum(df16_1)
                m16_1 = int(m16_1)
                df16_2 = pd.DataFrame(distanceM_list)
                df16_2 = np.nan_to_num(df16_2)
                m16_2 = np.sum(df16_2)
                m16_2 = int(m16_2)
                m16_3 = m16_1/m16_2
                HardDecelerationsKM = str(m16_3)
                
            #Output - RPM behavior
                #AverageRPM
                AverageRPM_list = extract_element_from_json(datatime, ['maxRpm'])
                df17 = pd.DataFrame(AverageRPM_list)
                df17 = np.nan_to_num(df17)
                m17 = np.mean(df17, dtype=np.float64)
                AverageRPM = str(m17)
                #MaximumRPM
                MaxRPM_list = extract_element_from_json(datatime, ['maxRpm'])
                df18 = pd.DataFrame(MaxRPM_list)
                df18 = np.nan_to_num(df18)
                m18 = np.max(df18)
                MaxRPM = str(m18)
                #VarianceRPM
                VarianceRPM_list = extract_element_from_json(datatime, ['maxRpm'])
                df19 = pd.DataFrame(VarianceRPM_list)
                df19 = np.nan_to_num(df19)
                m19 = np.var(df19, dtype=np.float64)
                VarianceRPM = str(m19)
                
                #new_data = [{k: v for k, v in d.items() if (k != 'durationS' 
                                                            #and k != 'maxThrottlePercent'
                                                            #and k != 'thingId'
                                                            #and k != 'countOfCorners'
                                                            #and k != 'countOfStops'
                                                            #and k != 'gpsDeclineM'
                                                            #and k != 'gpsClimbM'
                                                            #and k != 'nightDrivingDurationS'
                                                            #and k != 'dayDrivingDurationS'
                                                            #and k != 'standingDurationS'
                                                            #and k != 'drivingDurationS'
                                                            #and k != 'nightDistanceM'
                                                            #and k != 'dayDistanceM'
                                                            #and k != 'timestamp'
                                                            #and k != 'dayDistanceM'
                                                            #and k != 'maxObdSpdKmH'
                                                            #and k != 'maxEngineCoolantTempC'
                                                            #and k != 'type'
                                                            #and k != 'reason'
                                                            #and k != 'currentSpeedKmH'
                                                            #and k != 'currentRPM')} for d in datatime]
            with open(joined_path, 'w') as write_file:
                string_json = {'thingID': thingId, 'AverageAcceleration': AverageAcceleration, 'MaximumAcceleration': MaximumAcceleration, 'PercentileAcceleration': PercentileAcceleration, 'VarianceAcceleration': VarianceAcceleration, 'AverageDeceleration': AverageDeceleration, 'MaximumDeceleration': MaximumDeceleration, 'PercentileDeceleration': PercentileDeceleration, 'VarianceDeceleration': VarianceDeceleration, 'AverageSpeed': AverageSpeed, 'AverageSpeedZero': AverageSpeedZero, 'MaxSpeed': MaxSpeed, 'VarianceSpeed': VarianceSpeed, 'CountHardAccelerations': CountHardAccelerations, 'HardAccelerationsKM': HardAccelerationsKM, 'CountHardDecelerations': CountHardDecelerations, 'HardDecelerationsKM': HardDecelerationsKM, 'AverageRPM': AverageRPM, 'MaxRPM': MaxRPM, 'VarianceRPM': VarianceRPM}
                new_data = json.dump(string_json, write_file)
                

        if 'trips.json' in file:
            import json
            import pandas as pd
            import numpy as np
            import dictor
            import statistics
            joined_path = os.path.join(r,file)
            with open(joined_path) as read_file:
                datatrips = json.load(read_file)
            #Output
                #AverageSpeedTrip
                AverageSpeedTrip_list = extract_element_from_json(datatrips, ['tripStats','averageSpeedKMH'])
                df20 = pd.DataFrame(AverageSpeedTrip_list)
                df20 = np.nan_to_num(df20)
                m20 = np.mean(df20, dtype=np.float64)
                AverageSpeedTrip = str(m20)
                
                #new_data = [{k: v for k, v in d.items() if (k != 'badTrip' 
                                                            #and k != 'accountId'
                                                            #and k != 'thingId'
                                                            #and k != 'tripId'
                                                            #and k != 'endLocationBestEffort'
                                                            #and k != 'startLocationBestEffort'
                                                            #and k != 'parkingTimeS'
                                                            #and k != 'endTime'
                                                            #and k != 'ttOdometerStampM'
                                                            #and k != 'dateCreated'
                                                            #and k != 'tripStats'
                                                            #and k != 'drivingScore'
                                                            #and k != 'distanceScore'
                                                            #and k != 'ecoScore')} for d in data]
                
            with open(joined_path, 'w') as write_file:
                new_data2 = {'thingID': thingId, 'AverageAcceleration': AverageAcceleration, 'MaximumAcceleration': MaximumAcceleration, 'PercentileAcceleration': PercentileAcceleration, 'VarianceAcceleration': VarianceAcceleration, 'AverageDeceleration': AverageDeceleration, 'MaximumDeceleration': MaximumDeceleration, 'PercentileDeceleration': PercentileDeceleration, 'VarianceDeceleration': VarianceDeceleration, 'AverageSpeed': AverageSpeed, 'AverageSpeedZero': AverageSpeedZero, 'MaxSpeed': MaxSpeed, 'VarianceSpeed': VarianceSpeed, 'CountHardAccelerations': CountHardAccelerations, 'HardAccelerationsKM': HardAccelerationsKM, 'CountHardDecelerations': CountHardDecelerations, 'HardDecelerationsKM': HardDecelerationsKM, 'AverageRPM': AverageRPM, 'MaxRPM': MaxRPM, 'VarianceRPM': VarianceRPM, 'AverageSpeedTrip': AverageSpeedTrip}
                new_data2 = json.dump(new_data2, write_file)
            
