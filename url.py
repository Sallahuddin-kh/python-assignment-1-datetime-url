def get_protocol(url:str)->str: 
    """
    Gets the protocol specified in the url
    """                        
    parsed_url = url.split("?")
    protocol = parsed_url[0].split("://")
    if(len(protocol) == 1):
        return None
    return protocol[0]

def get_domain(url:str)->str: 
    """
    Gets the domain in the url
    """                          
    parsed_url = url.split("?") 
    protocol = parsed_url[0].split("://")
    if(len(protocol) == 1): 
        domain = protocol[0].split("/")
        domain = domain[0].split(":")
        return domain[0]
    else:
        domain = protocol[1].split("/")
        domain = domain[0].split(":")
        return domain[0]

def get_path(url:str)->str:
    """
    Gets the Path of the resource
    """                             
    parsed_url = url.split("?") 
    protocol = parsed_url[0].split("://")
    if(len(protocol) == 1): 
        domain = protocol[0].split("/",1)
        return_string = "/"+domain[1]
        return return_string
    else:
        domain = protocol[1].split("/",1)
        return_string = "/"+domain[1]
        return return_string
    
def get_query_string_params(url:str)->dict: 
    """
    Returns the query arguments in form of a dictionary
    """            
    path_and_query = url.split("?")  
    if(len(path_and_query)>1):
        split_query = path_and_query[1].split("&")
        dict = {}
        for param in split_query:
            temp = param.split("=")
            dict[temp[0]] = temp[1]
        return dict
    return {}


print(get_path("www.google.com/dfdsf/fdsf/ds/fds/fd/sf"))