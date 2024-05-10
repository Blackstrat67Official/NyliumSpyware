from nylium import device
from nylium import network
from nylium import position
import os

class Nylium:
    def __init__(self, folder_name):
        self.folder_name = folder_name
        os.makedirs(self.folder_name, exist_ok=True)
        
        self.device_info = device.GetGeneralInfo()
        self.battery_info = device.GetBatteryInfo()
        self.hardware_info = device.GetHardwareInfo()
        self.external_disks_info = device.GetExternalDisksInfo()
        self.installed_packages = device.GetInstalledPackages()
        self.location_info = position.GetLocationInfo()
        self.network_interfaces_info = network.GetNetworkInterfacesInfo()
        self.network_connectivity_info = network.GetNetworkConnectivityInfo()
        self.network_connections_info = network.get_network_connections_info()
        self.network_protocol_info = network.get_network_protocol_info('tcp')
        self.network_traffic_info = network.get_network_traffic_info()

        self.WriteIntoFiles()

    def Print(self):
        print("""
NNNNNNNN        NNNNNNNN                        lllllll   iiii                                            
N:::::::N       N::::::N                        l:::::l  i::::i                                           
N::::::::N      N::::::N                        l:::::l   iiii                                            
N:::::::::N     N::::::N                        l:::::l                                                   
N::::::::::N    N::::::Nyyyyyyy           yyyyyyyl::::l iiiiiii uuuuuu    uuuuuu     mmmmmmm    mmmmmmm   
N:::::::::::N   N::::::N y:::::y         y:::::y l::::l i:::::i u::::u    u::::u   mm:::::::m  m:::::::mm 
N:::::::N::::N  N::::::N  y:::::y       y:::::y  l::::l  i::::i u::::u    u::::u  m::::::::::mm::::::::::m
N::::::N N::::N N::::::N   y:::::y     y:::::y   l::::l  i::::i u::::u    u::::u  m::::::::::::::::::::::m
N::::::N  N::::N:::::::N    y:::::y   y:::::y    l::::l  i::::i u::::u    u::::u  m:::::mmm::::::mmm:::::m
N::::::N   N:::::::::::N     y:::::y y:::::y     l::::l  i::::i u::::u    u::::u  m::::m   m::::m   m::::m
N::::::N    N::::::::::N      y:::::y:::::y      l::::l  i::::i u::::u    u::::u  m::::m   m::::m   m::::m
N::::::N     N:::::::::N       y:::::::::y       l::::l  i::::i u:::::uuuu:::::u  m::::m   m::::m   m::::m
N::::::N      N::::::::N        y:::::::y       l::::::li::::::iu:::::::::::::::uum::::m   m::::m   m::::m
N::::::N       N:::::::N         y:::::y        l::::::li::::::i u:::::::::::::::um::::m   m::::m   m::::m
N::::::N        N::::::N        y:::::y         l::::::li::::::i  uu::::::::uu:::um::::m   m::::m   m::::m
NNNNNNNN         NNNNNNN       y:::::y          lllllllliiiiiiii    uuuuuuuu  uuuummmmmm   mmmmmm   mmmmmm
                              y:::::y                                                                     
                             y:::::y                                                                      
                            y:::::y                                                                       
                           y:::::y                                                                        
                          yyyyyyy                                                                         

                                            Developed by Blackstrat67
                                                Nylium v1.0.0
        """)

    def WriteIntoFiles(self):
        with open(os.path.join(self.folder_name, 'general_info.txt'), 'w') as f:
            for key, value in self.device_info.items():
                f.write(f"{key}: {value}\n")

        with open(os.path.join(self.folder_name, 'battery_info.txt'), 'w') as f:
            for key, value in self.battery_info.items():
                f.write(f"{key}: {value}\n")

        with open(os.path.join(self.folder_name, 'hardware_info.txt'), 'w') as f:
            for key, value in self.hardware_info.items():
                f.write(f"{key}: {value}\n")

        with open(os.path.join(self.folder_name, 'external_disks_info.txt'), 'w') as f:
            for disk_info in self.external_disks_info:
                f.write(f"{disk_info}\n")

        with open(os.path.join(self.folder_name, 'installed_packages.txt'), 'w') as f:
            f.write(self.installed_packages)

        with open(os.path.join(self.folder_name, 'location_info.txt'), 'w') as f:
            for key, value in self.location_info.items():
                f.write(f"{key}: {value}\n")

        with open(os.path.join(self.folder_name, 'network_interfaces_info.txt'), 'w') as f:
            f.write(str(self.network_interfaces_info))

        with open(os.path.join(self.folder_name, 'network_connectivity_info.txt'), 'w') as f:
            f.write(str(self.network_connectivity_info))

        with open(os.path.join(self.folder_name, 'network_connections_info.txt'), 'w') as f:
            f.write(str(self.network_connections_info))

        with open(os.path.join(self.folder_name, 'network_protocol_info.txt'), 'w') as f:
            f.write(str(self.network_protocol_info))

        with open(os.path.join(self.folder_name, 'network_traffic_info.txt'), 'w') as f:
            f.write(str(self.network_traffic_info))
        
NyliumRoot = Nylium("data")
NyliumRoot.Print()