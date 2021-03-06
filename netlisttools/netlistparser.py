"""
Netlist Import Tool

Imports PADs netlists and returns netlist datastructure for use elsewhere

Author: Steve Jeapes (netlist@arcoarena.co.uk)
Creation Date: 6th Aug 15
"""
import re


def parse(netlist_file):
    """Takes a filename of a PADS netlist
    Returns a netlist as a list of tuples of (Netname, List of (RefDes, Pin#))
    """
    try:
        f = open(netlist_file, 'r')
        # Check first line of Netlist indicates that we have a PADS netlist
        if f.readline()[:10] != '*PADS-PCB*':
            raise ValueError('Netlist not in PADs format')

        if f.readline()[:5] != '*NET*':
            raise ValueError('File is not a netlist file')

    except IOError:
        print "Invalid input file name"

    # Strip line endings and create single string
    lines = ''
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
        # Check for Space in Netname
        net_split = re.split(r'[A-Z|a-z|0-9|_|-]+[.][A-Z|a-z|0-9|_|-]+', net)
        net_split = re.split(r'[ ]', net_split[0])
        if re.split(r'[ ]', net_split[0]) > 1:
            if not net_split[1] == '':
                raise ValueError(
                    'Netlist has spaces or other invalid characters in name '
                    + str(net_split))
        net_split = re.split(r'[ .]', net)
        nodes = []
        for i in range(1, len(net_split) - 1, 2):
            nodes.append({'refdes': net_split[i], 'pin': net_split[i + 1]})
        netlist.append((net_split[0], nodes))

    return netlist
