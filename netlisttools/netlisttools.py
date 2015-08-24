#==============================================================================
# Netlist Tools
# 
# A collection of netlist inspection tools
#
# Author: Steve Jeapes (netlist@arcoarena.co.uk)
# Creation Date: 6th Aug 15
#==============================================================================

import re, netlistparser, sqlite3

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
                if re.match(r'[Tt][PpHhVv]',node['refdes']):
                   testpoint.append(net[0])
    return testpoint

db = sqlite3.connect(':memory:')
def init_db(cursor):
    cursor.execute('''
    CREATE TABLE components(
        Row INTEGER,
        RefDes TEXT,
        Pin TEXT)
    '''))
cursor = db.cursor()
init_db(cursor)

def component_connections(netlist):
    ref_des_list = []
    per_pin_list = []
    #Get list of unique components ref_Des    
    for net in netlist:
        for component in net[1]:       
            per_pin_list.append(component)
            if not(component['refdes'] in ref_des_list):
                ref_des_list.append(component['refdes'])
    
    #For each component ref des create  list of [refdes, 
    for refdes in ref_des_list:
        

        return ref_des_list

#----------------------------
# Debug Code
#---------------------------
netlist = netlistparser.parse('../example_files/netlist.NET')
#print(netlist)
power = identify_power(netlist)
orphans= orphan_nets(netlist)
testpoints= testpoint_only(netlist)
components = component_connections(netlist)

print power
print orphans
print testpoints
print components