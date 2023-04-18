#Manual script to add or delete the Pool Members

# Import the necessary F5 SDK modules
from f5.bigip import ManagementRoot
from f5.utils.responses.handlers import Stats

add_or_remove = input("Press 1 if you want to remove the servers from F5 or Press 2 to add: ")

if add_or_remove == "1":
    # Define the necessary variables
    f5_host = input("Enter the F5 host IP (example 10.0.0.1): ")
    f5_user = input("Enter the F5 user name : ")
    f5_pass = input("Enter the F5 user password : ")
    pool_name = input("Enter the F5 pool name: ")
    # List of server names to remove from the pool
    servers = input("Enter the list of servers separated by space to remove: ")
    list = servers.split()
    #servers_to_remove = ["DA-MF-QSB01:443", "DA-MF-QSB02:443"]

    # Connect to the F5 device
    mgmt = ManagementRoot(f5_host, f5_user, f5_pass)

    # Retrieve the pool object
    pool = mgmt.tm.ltm.pools.pool.load(name=pool_name)

    # Loop through the servers to remove
    for server_name in list:
        # Retrieve the server object
        server = pool.members_s.members.load(name=server_name, partition='Common')
        # Remove the server from the pool
        server.delete()
        print(f"Server {server_name} has been removed from pool {pool_name}")

elif add_or_remove == "2":
    # Define the necessary variables
    f5_host = input("Enter the F5 host IP (example 10.0.0.1): ")
    f5_user = input("Enter the F5 user name : ")
    f5_pass = input("Enter the F5 user password : ")
    pool_name = input("Enter the F5 pool name: ")
    # List of server names to add to the pool
    # Port number of the servers
    #servers_to_add = ["DA-MF-QSB01", "DA-MF-QSB02"]
    servers = input("Enter the list of servers separated by space to add : ")
    list = servers.split()
    
    
    server_port = input("Enter the server port in pool (example 443): ")

    # Connect to the F5 device
    mgmt = ManagementRoot(f5_host, f5_user, f5_pass)

    # Retrieve the pool object
    pool = mgmt.tm.ltm.pools.pool.load(name=pool_name, partition='Common')

    # Loop through the servers to add
    for server_name in list:
        # Create a new member object
        member = pool.members_s.members.create(partition='Common', name=server_name + ":" + server_port)
        # Add the new member to the pool
        pool.update()
        print(f"Server {server_name} has been added to pool {pool_name}")

else:
    print(" Entered the incorrect input type - please try again ")