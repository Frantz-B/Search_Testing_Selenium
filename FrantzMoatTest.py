def comp(list1, list2):
    for elementText in list1:
        if elementText in list2:
            return True
        else:
            return False
            break
list1 = ["moat.com/advertiser/ffw?report_type=display&creative_md5=9436b5e508dcafb24e7bbf05a8cf1d4b" , "moat.com/advertiser/ffw?report_type=display&creative_md5=e054cb32bd456de456f582577a8b9a85"]
shit2 = [4 , 2]
print(comp(list1 , shit2))
def returnMatches(a, b):
    return list(set(a) & set(b))
print(returnMatches(list1, shit2))