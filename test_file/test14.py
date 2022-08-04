import socket

devices_dictionary = [{'IP': '192.168.43.1', 'MAC': '0a:c5:e1:b8:a5:74'}, {'IP': '192.168.43.73', 'MAC': 'b4:b0:24:95:df:ea'}, {'IP': '192.168.43.132', 'MAC': 'ec:2e:98:61:61:8d'}, {'IP': '192.168.43.112', 'MAC': '4c:03:4f:e3:8c:df'}, {'IP': '192.168.43.208', 'MAC': 'e4:5e:37:4f:25:cc'}, {'IP': '192.168.43.27', 'MAC': '76:5c:d5:c2:8a:dc'}, {'IP': '192.168.43.38', 'MAC': '14:7d:da:6a:4d:63'}, {'IP': '192.168.43.47', 'MAC': '12:f3:ac:63:c7:0c'}]
for x in range(len(devices_dictionary)):
    print(devices_dictionary[x]['IP'])
    host_name_value = socket.gethostbyaddr(devices_dictionary[x]['IP'])
    print(host_name_value)
    devices_dictionary[x]['hostname'] = host_name