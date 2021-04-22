# routeros_api
Using python and routerOS to automate task.

The code is scripted to switch the IP address of the router to a new one when the old IP address of the router gets blocked due to some reason.
In my case , the IP address was blocked due to a DDOS attack and customers with that public address (all the customers that were NAT behind this public IP) could not access internet, so I had to switch the IP address to a new one.
The application that blocked the IP addess also triggered this python script which passed the ip that is blocked nto the script.
The IP address that was blocked by the application unblocks it after 30min so the 2ND code is to revert back the changes made by the first code.


Code: Combining both the codes in one python code

Code1: ip_address_switch.py
Tasks accomplished 

Adding the new IP address to the router
Change the Firewall NAT rules on old IP address to this new IP address.  
Adding the new address in BGP Networks
Terminating the connections with the old IP address


Code2:revert_changes.py
Task accomplished


Remove the IP address from the router.
Remove the address from BGP networks
Change the Firewall NAT rules to the original IP
Terminate the connections with the replaced IP
