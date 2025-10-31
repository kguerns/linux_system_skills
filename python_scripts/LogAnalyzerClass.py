# Log Error Count Analyzer
# A simple class to track how many errors are in a log file

class LogAnalyzer:
    def __init__(self):
        self.log_entries = []

    def add_entry(self, log_line):
        self.log_entries.append(log_line)
    
    def count_errors(self):
        count = 0
        for log in self.log_entries:
            if "ERROR" in log:
                count += 1
        return count

if __name__ == "__main__":
    analyzer = LogAnalyzer()
    analyzer.add_entry("2025-10-29 INFO: System startup complete.")
    analyzer.add_entry("2025-10-29 WARNING: High memory usage detected.")
    analyzer.add_entry("2025-10-29 ERROR: Disk failure on /dev/sdb.")
    analyzer.add_entry("2025-10-29 ERROR: Connection timed out.")
    analyzer.add_entry("2025-10-29 CRITICAL: Service stopped.")

    error_count = analyzer.count_errors()
    print(f"Total error count: {error_count}") # Output should be 2