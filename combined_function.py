import routeros_api

f1 = open("/home/sanket/ip_list.txt", 'rt')     #file containing list of available IP address
f2 = open("/home/sanket/used_ip.txt", 'rt')     #file containing list of address that have already been used


search_ip = #ip address of the router which is blocked to access the internet passed by the application
username = #user
password = #password

connection = routeros_api.RouterOsApiPool(search_ip, username ,password)

try: api= connection.get_api()
except: quit()


def function_list(list_pass):    #Funcation to loop through the list
    index = 0
    list = list_pass.get()
    list_new = []
    for index in range(len(list)):           
        for m,n in list[index].iteritems():
            if(search_ip in n):
                list_new.append(list[index]['id']     
    return list_new      
          
def function_remove(list_new,list_pass)  #Function to remove parameters
    
    for o in list_new:
        
        try: list_pass.remove(id=o)  
        except: continue


if { #ban           #Loop will run if IP address is banned


    for line_f1 in f1:                #Comparing the file to get a unique IP address from the ip_list.txt file

        for line_f2 in f2:
    
            x= line_f1.split('\n')[0]
            y = line_f2.split('\n')[0]
    
            if(x != y):
                f2.write(line_f1)
                break
      
            else: 
                continue   
        break
        
    list_1 = api.get_resource('/ip/firewall/nat/')   #Getting NAT rules
    list_2 = funcation_list(list_1)
    
    parameters = {'to-addresses': x }
    for each_rule in list_2:
        list_1.set(id=o, **parameters)     #changing NAT rules
     
    list_3 = api.get_resource('/ip/firewall/connection/')   #Flush out connections with old IP address
    function_remove(function_list,list_3)

    list_4 =  api.get_resource('/ip/address/')      #adding address in the router
    list_4.add(address =x, interface = bridge1)

    list_5 = api.get_resource('/routing/bgp/network/')    #adding address in BGP routing
    list_5.add(network = x, synchronize='no')

    f1.close()
    }
    
if { #unban            #It would loop if the previously banned IP is now unbanned

    list_1 =  api.get_resource('/ip/address/')    #Remove address from the router
    function_remove(funcation_list,list_1)
    
    list_2 = api.get_resource('/ip/firewall/nat/')  #Flush out connections with old IP address
    function_remove(funcation_list,list_2)
    
    list_3 = api.get_resource('/routing/bgp/network/')  #Remove address from BGP routing
    function_remove(funcation_list,list_3)
    
    data = f2.read()
    f2.close()
    
    data = data.replace(nat_ip, '')
    
    f2.open('/home/sanket/used_ip.txt','wt')
    f2.write(data)        #Erasing the IP so it can be used again
    
    f2.close()
    
    }

connection.disconnect()    
