import json


def validate_netlist(file_path):
    with open(file_path, 'r') as f:
        netlist = json.load(f)

    modules = netlist.get("modules", {})
    errors = []

    for module_name, module in modules.items():
        ports = module.get("ports", {})     #input/Output
        cells = module.get("cells", {})     #all gates/Flipflops
        netnames = module.get("netnames", {})   #wires declared n the module

        print(f"\nModule: {module_name}")
        print(f"  Ports: {list(ports.keys())}")
        print(f"  Cells: {list(cells.keys())}")

        # Check if all ports are connected
        for port, details in ports.items():
            bits = details.get("bits", [])    #check if each port has associated bit.if not then add error message.
            if not bits:
                errors.append(f"Port '{port}' has no bits.")

        # Check if each cell has type and connections
        for cell_name, cell in cells.items():
            if "type" not in cell:
                errors.append(f"Cell '{cell_name}' missing 'type'.")
            if "connections" not in cell:
                errors.append(f"Cell '{cell_name}' missing 'connections'.")

        # Check for unconnected nets (optional)
        used_nets = set()          #collect used nets
        for cell in cells.values():
            for conns in cell["connections"].values():
                used_nets.update(conns)
        declared_nets = set(netnames.keys())
        unused_nets = declared_nets - used_nets   #compared with declared nets
        if unused_nets:
            print(f"  Unused nets: {unused_nets}")

    if errors:
        print("\nValidation Errors:")
        for err in errors:
            print("  -", err)
    else:
        print("\n✅ Netlist validation passed with no errors.")


# Example usage
validate_netlist("spi_master.json")