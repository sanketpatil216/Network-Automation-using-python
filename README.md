# routeros_api
Using python and routerOS to automate task.

The code is scripted to switch the IP address of the router to a new one when the old IP address of the router gets blocked due to some reason.
In my case , the IP address was blocked due to a DDOS attack and customers with that public address (all the customers that were NAT behind this public IP) could not access internet, so I had to switch the IP address to a new one.
The application that blocked the IP addess also triggered this python script which passed also passed the parameters into the script.

Code1: ip_address_switch.py
Tasks accomplished 

Adding the new IP address to the router
Change the Firewall NAT rules on old IP address to this new IP address.  
Adding the new address in BGP Networks
Terminating the connections with the old IP address
