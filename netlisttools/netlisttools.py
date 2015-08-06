#==============================================================================
# Netlist Tools
# 
# A collection of netlist inspection tools
#
# Author: Steve Jeapes (netlist@arcoarena.co.uk)
# Creation Date: 6th Aug 15
#==============================================================================

def orphan_nets(netlist):
    orphans = []
    for net in netlist:
        if len(net[1]) < 2:
            orphans.append(net)
            
