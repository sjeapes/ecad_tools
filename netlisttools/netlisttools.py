#==============================================================================
# Netlist Tools
# 
# A collection of netlist inspection tools
#
# Author: Steve Jeapes (netlist@arcoarena.co.uk)
# Creation Date: 6th Aug 15
#==============================================================================
import re, netlist_import

def orphan_nets(netlist):
    orphans = []
    for net in netlist:
        if len(net[1]) == 1:
            orphans.append(net[0])
    return orphans
            
def identify_power(netlist):
    power = []
    for net in netlist:
        if re.match(r'^[+-]*[0-9]+[.vV]+[0-9]*',net[0]):
            name_split = re.split('[vV.A-Za-z_]',net[0])
            voltage= name_split[0]
            if name_split[1].isdigit():
                voltage = voltage + '.' + name_split[1]
            power.append((net[0],float(voltage)))
    return power            

def testpoint_only(netlist):
    testpoint=[]
    for net in netlist:
        if len(net[1]) == 2:
            for node in net[1]:
                if re.match(r'[Tt][Pp]',node['refdes']):
                   testpoint.append(net[0])
    return testpoint


#----------------------------
# Debug Code
#---------------------------
netlist = netlist_import.import_netlist('/home/sjeapes/Dropbox/Projects/NetlistTools/example_files/netlist.NET')
#print(netlist)
print identify_power(netlist)
print orphan_nets(netlist)
print testpoint_only(netlist)