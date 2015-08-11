# ecad_tools
A set of scripts for electronic CAD outputs (Bill of Materials and Netlist) to identify errors/improvemets

Schematic data produces 2 end outputs BoM and Netlist which are fed into either printed circuit board layout or manufacturers
The aim of this set of tools is to create automated checking of the schematic output to 
  - Spot common error
  - Suggest possible improvements
  - Produce processed output to aid completion of analysis (e.g. automated calculation of component voltage stress)

Currently the netlist is read in in PADS format (which can be output from many CAD packages)

Current Features are:
- Detection of single-Node nets
- Detection of nets with only 2 nodes (one of which being a testpoint)
- Automated guessing of voltage rails based upon netname


Short-term Planned Features:
- Output of voltage and current stress for passive components
- Detection of shorted passive components
- Output of connector pin-out table (pin #, net name)
- Checking of netlist file prior to sending for layout (all components have footprint names, no spaces in net name or footprint name)
