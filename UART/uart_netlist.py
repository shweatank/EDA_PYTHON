import json

def validate_netlist(filepath):
    try:
        with open(filepath, 'r') as file:
            netlist = json.load(file)
    except json.JSONDecodeError as e:
        return False, f"Invalid JSON format: {e}"
    except FileNotFoundError:
        return False, "Netlist file not found."

    # Basic structure check
    if "modules" not in netlist or not isinstance(netlist["modules"], dict):
        return False, "Missing or invalid 'modules' section in netlist."

    for module_name, module_data in netlist["modules"].items():
        if "ports" not in module_data or "cells" not in module_data or "netnames" not in module_data:
            return False, f"Module '{module_name}' missing 'ports', 'cells', or 'netnames'."

        if not isinstance(module_data["ports"], dict):
            return False, f"Module '{module_name}' ports must be a dictionary."

        if not isinstance(module_data["cells"], dict):
            return False, f"Module '{module_name}' cells must be a dictionary."

        if not isinstance(module_data["netnames"], dict):
            return False, f"Module '{module_name}' netnames must be a dictionary."

    return True, "Netlist Validation Done."

# Example usage
file_path = "results/netlist.json"
is_valid, message = validate_netlist(file_path)
print(message)