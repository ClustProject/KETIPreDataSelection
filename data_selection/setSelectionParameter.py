
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

