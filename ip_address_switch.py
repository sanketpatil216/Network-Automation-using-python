#code start

import routeros_api

f1 = open("/home/sanket/ip_list.txt", 'r+b')     #file containing list of available IP address
f2 = open("/home/sanket/used_ip.txt", 'r+b')     #file containing list of address that have already been used

for line_f1 in f1:                #Comparing the file to get a unique IP address from the ip_list.txt file
  
  for line_f2 in f2:
    
    x= line_f2.split('\n')[0]
    y = line_f1.split('\n')[0]
    
    if(x != y):
      f2.write(line_f1)
      break
      
    else: 
      continue   
  break

search_ip  #ip address of the router which is blocked to access the internet
username = #user
password = #password

connection = routeros_api.RouterOsApiPool(search_ip, username ,password)

try: api= connection.get_api()
except: quit()

list_1 = api.get_resource('/ip/firewall/nat/')
list_6 = list_1.get()
index1 = 0

for index1 in range(len(list_5)):
  for m,n in list_5[index1].iteritems():
    if('to-addresses' in m and search_ip in n):
      list_nat.append(list_5[index1]['id']
                      
parameters_2 = {'to-addresses': x }
                      
for o in nat_list:
                      list_1.set(id=o, **parameters_2)


list_2 = api.get_resource('/ip/firewall/connection/')
list_3 = list_2.get()

list_4 =  api.get_resource('/ip/address/')
list_4.add(address =x, interface = bridge1)

list_5 = api.get_resource('/routing/bgp/network/')
list_5.add(network = x, synchronize='no')

search_ip = host
search_name ='reply-dst-address'
search_id = 'id'
list_id = []
index = 0

for index in  range(len(list_3)):
  for a,b in list_3[index].iteritems():
    if search_ip in b and search_name in a:
      list_id.append(list_3[index]['id'])

      
for c  in  list_id:
  parameters_4 = {'id' : c } 
  list_4 = list_2.get(**parameters_4)


f2.write(line_f1)
f2.close()
f1.close()
connection.disconnect()            
  
  
