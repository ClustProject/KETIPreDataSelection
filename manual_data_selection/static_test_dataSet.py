
def set_integratedDataInfo(start, end):
    intDataInfo = {"db_info":
                   [{"db_name":"INNER_AIR","measurement":"HS1","domain":"farm","subdomain":"airQuality","start":str(start),"end":str(end)},
                 {"db_name":"OUTDOOR_AIR","measurement":"sangju","domain":"city","subdomain":"airQuality","start":str(start),"end":str(end)},
                 {"db_name":"OUTDOOR_WEATHER","measurement":"sangju","domain":"city","subdomain":"weather","start":str(start),"end":str(end)}]}
    return intDataInfo