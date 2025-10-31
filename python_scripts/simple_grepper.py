# Simple Log Grepper
# A simple log "grepper" that finds the lines in a file that contain a keyword.
# Returns a list of line numbers. Grep is case-insensitive.

def simple_grepper(filepath, keyword):
    line_numbers = []
    keyword_lower = keyword.lower()   # convert keyword (and lines) to lowercase so case-insensitive

    with open(filepath, 'r') as f:
        for index, line in enumerate(f):
            line_lower = line.lower()
            if keyword_lower in line_lower:
                line_numbers.append(index + 1)
    
    return line_numbers


if __name__ == "__main__":
    LOG_FILENAME = 'log.txt'
    LOG_CONTENT = """
2025-10-30 INFO: Starting log file analysis.

2025-10-30 ERROR: Primary API FAILURE detected.
2025-10-30 INFO: Attempting automated restart.
2025-10-30 WARNING: Secondary service Failure imminent.
2025-10-30 CRITICAL: Major FAILURE, rolling back.
    """
    keyword = 'FAILURE'
    with open(LOG_FILENAME, 'w') as f:
        f.write(LOG_CONTENT)
    
    line_numbers = simple_grepper(LOG_FILENAME, keyword)

    print(f"'{keyword}' is found on lines: {line_numbers}")
