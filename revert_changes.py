

import routeros_api

f2 = open("/home/sanket/used_ip.txt", 'r+b')     #file containing list of address that have already been used
search_ip = # Original IP that was replaced

for ip in f2.split('\n'):
  if (ip == search_ip);
    ip.replace(

search_ip = #ip address of the router which is blocked to access the internet
username = #user
password = #password

connection = routeros_api.RouterOsApiPool(search_ip, username ,password)

try: api= connection.get_api()
except: quit()

      
def loop_function(list_pass):
      index = 0
      list = list_pass.get()
      list_new = []
      for index in range(len(list)):           #searching for NAT rules with the old IP address
            for m,n in list[index].iteritems():
                  if(search_ip in n):
                        list_new.append(list[index1]['id']     
                                        
            for o in list_new:
                      list_pass.remove(id=o)    #moving the bloacked IP NAT rules over to the new IP address
                      
list_1 = api.get_resource('/ip/firewall/connection/')   #Flush out connections with old IP address
loop_function(list_1)

list_2 = api.get_resource('/ip/address')   #Remove old IP address from the router
loop_function(list_2)
                                        
list_3 = api.get_resource('/routing/bgp/network/')   #Remove BGP of old address
loop_function(list_3)
                                        
f2.close()
connection.disconnect()            
  
