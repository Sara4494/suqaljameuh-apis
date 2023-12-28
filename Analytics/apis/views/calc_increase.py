

def calc_increase_percentage (currnet_count , past_count) : 

    result = 0

    if currnet_count == past_count : 
        result = 0
    
    if past_count == 0 : 
        result = 100.0
    else : 
        result = ( currnet_count - past_count ) / past_count
    
    return result