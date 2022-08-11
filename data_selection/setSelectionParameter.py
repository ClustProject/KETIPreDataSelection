
def set_integratedDataInfo(start, end, partial_dataset_type):
    if partial_dataset_type =='VIBES':
        intDataInfo = {"db_info":
                       [{"db_name":"INNER_AIR","measurement":"HS1","start":str(start),"end":str(end)},
                     {"db_name":"OUTDOOR_AIR","measurement":"sangju","start":str(start),"end":str(end)},
                     {"db_name":"OUTDOOR_WEATHER","measurement":"sangju","start":str(start),"end":str(end)}]}
    elif partial_dataset_type =='KWeather':
        intDataInfo = {"db_info":
                       [{"db_name":"air_indoor_유치원","measurement":"ICW0W2000132","start":str(start),"end":str(end)},
                     {"db_name":"OUTDOOR_AIR","measurement":"seoul","start":str(start),"end":str(end)}]}
        
    return intDataInfo

def set_integratedDataInfoByDBSet(start, end, db_set):
    for db_index, db_one in enumerate(db_set):
        db_set[db_index]['start'] = start
        db_set[db_index]['end'] = end
    intDataInfo ={}
    intDataInfo["db_info"] = db_set
    return intDataInfo


def makeIntDataInfoSet(dataInfo, start, end):
    intDataInfo ={}
    db_info=[]
    
    for db_index, db_one in enumerate(dataInfo):
        db_set={}
        db_set['start'] = start
        db_set['end'] = end
        db_set['db_name'] = db_one[0]
        db_set['measurement'] = db_one[1]
        if len(db_one)>2:
            db_set ['tag_key']= db_one[2]
            db_set ['tag_value']= db_one[3]
        db_info.append(db_set)

    intDataInfo["db_info"] = db_info
    return intDataInfo


