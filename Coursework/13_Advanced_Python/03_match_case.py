def http_status(status):
    match status:
        case 200:
            return "OK"
        case 404:
            return "Error: not found"
        case 500:
            return "Internal Server error"
        case _:
            return "Unkown Status"
        
print(http_status(200))
print(http_status(404))
print(http_status(500))
print(http_status(2570))