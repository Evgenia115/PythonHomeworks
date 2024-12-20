from datetime import datetime
from collections import defaultdict
file_path = 'test_logs.txt'
def parse_log_line(line):
    parts = line.strip().split(', ')
    log_data = {}
    for part in parts:
        key, value = part.split(': ')
        log_data[key] = value
    return log_data

def read_logs(file_path):
    with open(file_path, 'r') as file:
        logs = [parse_log_line(line) for line in file]
    return logs

def get_stat_period(logs):
    dates = [datetime.strptime(log['date_connected'], "%d/%m/%Y %H:%M") for log in logs]
    min_date = min(dates).strftime("%d/%m/%Y")
    max_date = max(dates).strftime("%d/%m/%Y")
    return [min_date, max_date]

def count_unique_users(logs):
    users = {log['username'] for log in logs}
    return len(users)

def count_user_connections(logs):
    connections = defaultdict(int)
    for log in logs:
        connections[log['username']] += 1
    return dict(connections)

def get_user_unique_ips(logs):
    user_ips = defaultdict(set)
    for log in logs:
        user_ips[log['username']].add(log['ip'])
    return {user: list(ips) for user, ips in user_ips.items()}

def count_user_unique_ips(logs):
    user_ips = get_user_unique_ips(logs)
    return {user: len(ips) for user, ips in user_ips.items()}
logs = read_logs(file_path)

# Завдання 1
stat_period = get_stat_period(logs)
print("Період статистики:", stat_period)

# Завдання 2
unique_users_count = count_unique_users(logs)
print("Кількість унікальних користувачів:", unique_users_count)

# Завдання 3
user_connections = count_user_connections(logs)
print("Кількість підключень для кожного користувача:", user_connections)

# Завдання 4
user_unique_ips = get_user_unique_ips(logs)
print("Унікальні IP для кожного користувача:", user_unique_ips)

# Завдання 5
user_unique_ip_counts = count_user_unique_ips(logs)
print("Кількість унікальних IP для кожного користувача:", user_unique_ip_counts)

