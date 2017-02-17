"""
Netlist Tools

A collection of netlist inspection tools

Author: Steve Jeapes (netlist@arcoarena.co.uk)
Creation Date: 6th Aug 15
"""
from __future__ import division, print_function

import netlistparser
import netlisttools as nlt

class testability():
    def __init__(self, test_conns, netlist):
        """
        Sets up class

        Takes a list of REFDES of connections which can be used during test

        """

        self.netlist = netlist
        # self.num_components =
        self.test_conns = test_conns
        self.nets_testable()

    def nets_testable(self):
        testable = []
        untestable = []
        # All nets with a test point or a designated test connector on assumed
        # to be testable
        for net in self.netlist:
            istestable = False
            for node in net[1]:
                if (nlt.is_testpoint(node['refdes']) or
                   node['refdes'] in self.test_conns):
                        istestable = True
            if istestable:
                testable.append(net)
            else:
                untestable.append(net)
        self.testable_nets = testable
        self.untestable_nets = untestable
        self.net_testability = len(testable) / len(self.netlist)


# Debug Code
# netlist = netlistparser.parse('../example_files/netlist.NET')
# print(netlist)

if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser(description='Get testability data from netlist')
    ap.add_argument('--netlist', help='PADS netlist file')
    ap.add_argument('--conn', help='Testable connections', nargs='*')

    class argnamespace:
        pass

    arg = argnamespace()
    args = ap.parse_args(namespace=arg)
    netlist = netlistparser.parse(arg.netlist)

    test = testability(arg.conn, netlist)

    print("Testable Nets : ")
    for net in test.testable_nets:
        print(net[0])
    print("Un-testable Nets : ")
    for net in test.untestable_nets:
        print(net[0])

    print("Testability : ", "{:6.2f}".format(test.net_testability * 100), "%")