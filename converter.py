
def convert_to_number(ele):
    ele=str(ele)
    if (',' in ele) or ('.' in ele) :
        ele = ele.replace(',','')
        ele = ele.replace('.','')
        
    if('K'in ele) or ('k' in ele) :
            ele = ele.replace('K','')
            ele = ele.replace('k','')
            ele = int(ele)*1000
            
    elif ('M'in ele) or ('m' in ele) :
            ele = ele.replace('M','')
            ele = ele.replace('m','')
            ele = int(ele)*1000000
            
    elif('B'in ele) or ('b' in ele) :
            ele = ele.replace('B','')
            ele = ele.replace('b','')
            ele = int(ele)*1000000000
    
    return ele   