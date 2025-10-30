# Configuration File Parser
# Create and parse a simple configuration file and output configuration 
# key-value pairs

def parse_config(filename):
    config_dict = {}

    try:
        with open(filename, 'r') as file:
            for line in file:
                clean_line = line.strip()
                
                # ignore empty lines or lines that start with '#'
                if not clean_line or clean_line.startswith('#'):
                    continue

                try:
                    key, value = line.split("=", 1) # .split("=", 1) means only split on the first "="
                except ValueError:
                    print(f"Warning: Skipping line with improper format: {clean_line}")
                
                config_dict[key.strip()] = value.strip()

    except FileNotFoundError:
        print(f"Error: Configuration file '{filename}' not found.")
        return None

    return config_dict


if __name__ == "__main__":
    CONFIG_FILENAME = 'config.txt'
    CONFIG_CONTENT = """
# System Configuration
port = 8080
threads= 16
monitor_level = CRITICAL

# End of file
"""

    with open(CONFIG_FILENAME, 'w') as f:
        f.write(CONFIG_CONTENT)

    parsed_settings = parse_config(CONFIG_FILENAME)
    print(f"Parsed Configuration: {parsed_settings}")
    # Expected Output: {'port': '8080', 'threads': '16', 'monitor_level': 'CRITICAL'}
