def remove_last_slash(url:str)->str:                    #Removes the last forward slash that is redundant to the url
    if(url[-1]=='/'):
        return(url[:-1])
    else: 
        return url 
def get_protocol(url:str)->str:                         #Gets the protocol specified in the url
    parsed_url = url.split('/')
    protocol = parsed_url[0].replace(":",'')
    return protocol

def get_domain(url:str)->str:                           #Gets the domain in the url
    parsed_url = url.split('/')   
    return parsed_url[2]

def get_path(url:str)->str:                             #Gets the server directory path
    parsed_url = url.split('/',3)  
    path = parsed_url[3].split('?')
    return path[0]
def get_query_string_params(url:str)->dict:             #Returns the query arguments in form of a dictionary
    url = remove_last_slash(url)
    parsed_url = url.split('/',3)  
    path_and_query = parsed_url[3].split('?')
    split_query = path_and_query[1].split('&')
    dict = {}
    for param in split_query:
        temp = param.split('=')
        dict[temp[0]] = temp[1]
    return dict
