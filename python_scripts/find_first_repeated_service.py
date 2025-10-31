# Find First Repeated Service
# Find the first repeated service from a list of service names.
# Achieved with O(n) time complexity

def find_first_repeated_service(service_stream):
    service_name_set = set()    # empty set

    for service_name in service_stream:
        if service_name not in service_name_set:
            service_name_set.add(service_name)
        else:
            return service_name     # return first service already in the set


if __name__ == "__main__":
    service_stream = ['nginx', 'mysql', 'api', 'memcached', 'mysql', 'api']
    first_repeat = find_first_repeated_service(service_stream)
    print(f"First repeated service: {first_repeat}")
