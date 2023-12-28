    
# remove password field from returned qeryset
def RemovePasswordFromList(list_of_users : list) -> list: 
    wanted_data = [] 
    for i in list_of_users:
        user = {}
        
        for j in i.items() : 
            key = j[0]
            val = j[1]
            if key != 'password' :
                user[key] = val
        
        wanted_data.append( user )

    return wanted_data