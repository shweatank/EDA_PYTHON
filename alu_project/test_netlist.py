import json

def validate_netlist(filepath):
    with open(filepath, 'r') as f:
        netlist = json.load(f)

    issues = []

    # Check top-level structure
    if 'modules' not in netlist:
        issues.append("Missing 'modules' section in netlist.")
        return issues

    modules = netlist['modules']
    if not isinstance(modules, dict):
        issues.append("'modules' should be a dictionary.")
        return issues

    for module_name, module_data in modules.items():
        if 'cells' not in module_data:
            issues.append(f"Module '{module_name}' missing 'cells' section.")
            continue

        if 'netnames' not in module_data:
            issues.append(f"Module '{module_name}' missing 'netnames' section.")
            continue

        cells = module_data['cells']
        netnames = module_data['netnames']

        for cell_name, cell_info in cells.items():
            if 'type' not in cell_info:
                issues.append(f"Cell '{cell_name}' in module '{module_name}' missing 'type'.")
            if 'connections' not in cell_info:
                issues.append(f"Cell '{cell_name}' in module '{module_name}' missing 'connections'.")
            else:
                for port, nets in cell_info['connections'].items():
                    if not isinstance(nets, list) or len(nets) == 0:
                        issues.append(f"Connection for port '{port}' in cell '{cell_name}' is invalid.")

        # Validate net names
        for netname, netinfo in netnames.items():
            if 'bits' not in netinfo or not isinstance(netinfo['bits'], list):
                issues.append(f"Net '{netname}' in module '{module_name}' has no valid 'bits' list.")

    return issues

def test_validate_netlist():
    errors = validate_netlist('verilog/netlist_alu.json')
    assert not errors, f"Netlist validation failed with errors: {errors}"
