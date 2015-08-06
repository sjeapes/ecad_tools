#==============================================================================
# Netlist Import Tool
# 
# Imports PADs netlists and returns netlist datastructure for use elsewhere
#
# Author: Steve Jeapes (netlist@arcoarena.co.uk)
# Creation Date: 6th Aug 15
#==============================================================================

def import_netlist(netlist_file):
    """Takes a filename of a PADS netlist
    Returns a netlist as a list of tuples of (Netname, List of Connections)
    """
    try:
        f = open(netlist_file,'r')
            #Check first line of Netlist indicates that we have a PADS netlist
        if f.readline()[:10] != '*PADS-PCB*':
            raise ValueError('Netlist not in PADs format')
        
        if f.readline()[:5] != '*NET*':
            raise ValueError('File is not a netlist file')
                      
    except IOError:
        print "Invalid input file name"
     
    #Strip line endings and create single string
    lines= ''
    for line in f:
        line = line.rstrip("\n\r")
        lines += line

    if lines[-5:] == '*END*':
        lines = lines[:-5]
    else:
        raise ValueError('Unexpected final line in file, should be *END*')

    list_of_nets = lines.split('*SIGNAL* ')
    
    netlist = []
    for net in list_of_nets[1:]:
        net_split = net.split(' ')
        netlist.append((net_split[0],net_split[1:]))
        
    return netlist
    
#import_netlist('/home/sjeapes/Dropbox/Projects/NetlistTools/example_files/XA-021448-DG Low Resolution FPC ver 2.NET')