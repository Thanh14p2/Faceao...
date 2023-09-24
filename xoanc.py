processed_ip_ports = []

# Đọc dữ liệu từ tệp đầu vào và chia thành từng dòng
with open('kk.txt', 'r') as file:
    input_data = file.readlines()

# Xử lý từng dòng trong danh sách
for line in input_data:
    parts = line.strip().split(':')
    if len(parts) >= 2:
        processed_ip_ports.append(f"{parts[0]}:{parts[1]}")

# In danh sách đã xử lý
# Các bước xử lý dữ liệu ở trên

# Ghi danh sách đã xử lý vào tệp 'proxies.txt'
with open('proxies.txt', 'a') as output_file:
    for item in processed_ip_ports:
        output_file.write(item + '\n')
