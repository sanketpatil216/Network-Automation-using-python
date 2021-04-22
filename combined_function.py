                             
import routeros_api
import sys

f1 = open("ip_list.txt", 'rt')     #file containing list of available IP address
f2 = open("used_ip.txt", 'rt')     #file containing list of address that have already been used

file2 = f2.read()

search_ip = #ip address of the router which is blocked to access the internet passed by the application
username = 'python' #user
password = '12345 #password
action = 
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
                list_new.append(list[index]['id'])   
    return list_new      
          
def function_remove(list_new,list_pass):  #Function to remove parameters
    
    for o in list_new:
        
        try: list_pass.remove(id=o)  
        except: continue


if action == 'ban':       #Loop will run if IP address is banned


    for line_f1 in f1:                #Comparing the file to get a unique IP address from the ip_list.txt file
  
        x= line_f1.split('\n')[0]
   
        if x not in file2:
            f2.write(x)
            f2.write('\t')
            f2.write(search_ip)
            f2.write('\n')
            break
        
        else: 
            continue   
        
    list_1 = api.get_resource('/ip/firewall/nat/')   #Getting NAT rules
    list_2 = function_list(list_1)
    
    parameters = {'to-addresses': y }
   
    for each_rule in list_2:
        list_1.set(id=each_rule, **parameters)     #changing NAT rules
     
    list_3 = api.get_resource('/ip/firewall/connection/')   #Flush out connections with old IP address
    function_remove(function_list(list_3),list_3)

    list_4 =  api.get_resource('/ip/address/')      #adding address in the router
    list_4.add(address =x, interface = 'bridge1')

    list_5 = api.get_resource('/routing/bgp/network/')    #adding address in BGP routing
    list_5.add(network = x, synchronize='no')

    f1.close()
    
    
if action == 'unban':            #It would loop if the previously banned IP is now unbanned

    f2 = open('used_ip.txt','r')
    data = f2.readlines()
                 
    op = []
                                      
    for lines in data:
        try:
            x = lines.split('\t')[0]
            y = lines.split('\t')[1]
    
            y = y.strip()
    
            if y!= search_ip:
                op.append(a)
        
            else:
                search_ip =x
                      
        except: continue
                         
    f2 = open('used_ip.txt','w')

    f2.writelines(op)
    f2.close()
      
    
    
    list_1 =  api.get_resource('/ip/address/')    #Remove address from the router
    function_remove(function_list(list_1),list_1)
    
    list_2 =  api.get_resource('/ip/firewall/nat')
    list_3 = function_list(list_2)
    
    parameters_2 = {'to-addresses': search_ip }   #Change NAT rules
    for each_rule_2 in list_3:
        list_1.set(id=each_rule_2, **parameters_2)
    
    list_3 = api.get_resource('/routing/bgp/network/')  #Remove address from BGP routing
    function_remove(function_list(list_3),list_3)
    

connection.disconnect()   
