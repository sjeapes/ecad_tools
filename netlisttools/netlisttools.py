#==============================================================================
# Netlist Tools
# 
# A collection of netlist inspection tools
#
# Author: Steve Jeapes (netlist@arcoarena.co.uk)
# Creation Date: 6th Aug 15
#==============================================================================
import re

def orphan_nets(netlist):
    orphans = []
    for net in netlist:
        if len(net[1]) < 2:
            orphans.append(net)
            
def identify_power(netlist):
    power = []
    for net in netlist:
        if re.match(r'[+-]*[0-9.]*[vV][0-9]*',net):
            power.append(net)
            
