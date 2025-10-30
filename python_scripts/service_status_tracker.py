# Service Status Tracker:
# Counts the number of UP/DOWN/UNKNOWN statuses and number of unique service names
# from a list of SERVICE_NAME:STATUS strings

def track_service_status(data):
    status_count_dict = {}  # empty dictionarty
    service_names_set = set()   # empty set

    for report in data:
        name, status = report.split(":")
        
        service_names_set.add(name) # .add() to add to sets

        # .get(key, default_value) returns default_value if the key isn't found
        status_count_dict[status] = status_count_dict.get(status, 0) + 1

    return (status_count_dict, len(service_names_set))

if __name__ == "__main__": 
    reports = [
        "API_Gateway:UP",
        "DB_Replica:DOWN",
        "Load_Balancer:UP",
        "API_Gateway:UP", # Duplicate service name, UP status
        "Auth_Service:DOWN",
        "DB_Master:UNKNOWN",
        "Auth_Service:DOWN"
    ]

    status_counts, unique_services = track_service_status(reports)

    print(f"Status Counts: {status_counts}")
    # Expected: {'UP': 3, 'DOWN': 3, 'UNKNOWN': 1}
    print(f"Unique Services: {unique_services}")
    # Expected: 5 (API_Gateway, DB_Replica, Load_Balancer, Auth_Service, DB_Master)