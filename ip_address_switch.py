#code start

import routeros_api

f1 = open("/home/sanket/ip_list.txt", 'r+b')     #file containing list of available IP address
f2 = open("/home/sanket/used_ip.txt", 'r+b')     #file containing list of address that have already been used

for line_f1 in f1:                #Comparing the file to get a unique IP address from the ip_list.txt file
  for line_f2 in f2:
    if(line_f1 != line_f2):
      print(line_f1.split('\n'))
      x = line_f1.split('\n')[0]
      break
  break

host = #ip address of the router which is blocked to access the internet
username = #user
password = #password

connection = routeros_api.RouterOsApiPool(host, username ,password)

try: api= connection.get_api()
except: quit()

list_1 = api.get_resource('/ip/firewall/nat/')

parameters_1 = {'chain':'srcnat','action':'src-nat','to-addresses':'10.101.127.25'}
parameters_2 = {'to-addresses': x }

try : list_2 = list_1.get(**parameters_1)[0]["id"]
except: quit()

list_1.set(id=list_2,**parameters_2)

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
  
  
  
  
