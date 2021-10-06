def get_protocol(url:str)->str:
    parsed_url = url.split('/')
    protocol = parsed_url[0].replace(":",'')
    return protocol

def get_domain(url:str)->str:
    parsed_url = url.split('/')   
    return parsed_url[2]

url = "http://www.kite.com/python/answers/how-to-truncate-a-string-in-python"
print(get_domain(url))
#print(url)