import time

# Path to the SSH log file
ssh_log_path = "/var/log/auth.log"

# Path to the custom log file
custom_log_path = "ssh_custom_log.txt"

# Function to read new entries from the SSH log
def read_ssh_log():
    with open(ssh_log_path, "r") as ssh_log_file:
        # Move the file pointer to the end of the file
        ssh_log_file.seek(0, 2)
        
        while True:
            # Read new lines as they are added to the file
            new_line = ssh_log_file.readline()
            if new_line:
                yield new_line
            else:
                time.sleep(0.1)  # Sleep for a short time to avoid high CPU usage

# Function to write new SSH log entries to the custom log file
def write_custom_log(new_entry):
    with open(custom_log_path, "a") as custom_log_file:
        custom_log_file.write(new_entry)

# Main function to monitor the SSH log for a minute
def monitor_ssh_log(duration):
    print("Monitoring SSH log...")
    start_time = time.time()
    end_time = start_time + duration
    
    ssh_log_generator = read_ssh_log()
    
    try:
        while time.time() < end_time:
            new_entry = next(ssh_log_generator)
            # You can add additional filtering logic here if needed
            write_custom_log(new_entry)
    except KeyboardInterrupt:
        pass

    print("Monitoring stopped.")


# Run for 60 seconds (1 minute)
monitor_ssh_log(60)
