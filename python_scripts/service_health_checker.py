# Service Health Check Automation
# Automation script to check if a service is active and report either 
# 'UP' or 'DOWN'

import subprocess
from collections import namedtuple

# namedtuple to mock the result of systemctl
MockResult = namedtuple('MockResult', ['stdout', 'returncode'])

def check_service_health(service_name):

    # Simulate a running service's output
    if service_name == 'API_GW':
        mock_output = "Active: active (running) since..."
        mock_code = 0
    elif service_name == 'DB_MASTER':
        mock_output = "Active: inactive (dead) since..."
        mock_code = 3
    else:
        # Actual systemctl call for non-simulated services
        result = subprocess.run(
            ['systemctl', 'status', service_name],
            capture_output=True,
            text=True,  # Decode output as text
            check=False # Don't raise error on non-zero exit code
        )
        return 'UP' if result.returncode == 0 and "(running)" in result.stdout else 'DOWN'
    
    result = MockResult(stdout=mock_output, returncode=mock_code)

    if result.returncode == 0 and "(running)" in result.stdout:
        return 'UP'
    else:
        return 'DOWN'

if __name__ == "__main__":
    print(f"API_GW status: {check_service_health('API_GW')}")
    print(f"DB_MASTER status: {check_service_health('DB_MASTER')}")
