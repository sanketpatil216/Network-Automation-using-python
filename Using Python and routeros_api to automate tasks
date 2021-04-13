#code start


import routeros_api
import sys
  '''
f1 = open("/home/sanket/ip_list.txt", 'r+b')
f2 = open("/home/sanket/used_ip.txt", 'r+b')
print f1,f2
for line_f1 in f1:
  for line_f2 in f2:
    if(line_f1 != line_f2):
      print(line_f1.split('\n'))
      x = line_f1.split('\n')[0]
      f2.write(line_f1)
      break
  break
  print(x)
  '''
  z = '10.101.127.1'
  connection = routeros_api.RouterOsApiPool(z,'python','aV9GymDzUZK3VmBcK7sxa7RY4J')
  try: api= connection.get_api()
  except: quit()
  '''
  list_1 = api.get_resource('/ip/firewall/nat/')
  parameters_1 = {'chain':'srcnat','action':'src-nat','to-addresses':'10.101.127.25'}
  parameters_2 = {'to-addresses': x }
  try : list_2 = list_1.get(**parameters_1)[0]["id"]
  except: quit()
  list_1.set(id=list_2,**parameters_2)
  f1.close()
  f2.close()
  '''
  list_2 = api.get_resource('/ip/firewall/connection/')
  list_3 = list_2.get()
  search_ip ='75.159.219.7'
  search_name ='reply-dst-address'
  search_id = 'id'
  list_id = []
  index = 0
  for index in  range(len(list_3)):
  for a,b in list_3[index].iteritems():
  if search_ip in b and search_name in a:
  g = (list_3[index]["id"])
  
  list_id.append(list_3[index]['id'])
  print list_id
  '''
  print list_3[2]
  list_id =[]
  for a,b in list_3[2].iteritems():
  if search_ip in b and search_name in a: 
  list_id.append(list_3[2]["id"])
  '''
  for c  in  list_id:
  parameters_4 = {'id' : c } 
  list_4 = list_2.get(**parameters_4)
  print list_4
  connection.disconnect()            
  
  
  
  
