import json

with open("../karabiner-windows-mode/windows_shortcuts.json", "r") as read_file:
    data = json.load(read_file)

for rule in data["rules"]:
    for manipulator in rule["manipulators"]:
        if manipulator.get("conditions"):
            for condition in manipulator["conditions"]:
                condition["bundle_identifiers"].append("^com\\.jetbrains\\.pycharm$")
#                for ident in condition["bundle_identifiers"]:
#                    ident.append("foo")

with open("data_file.json", "w") as write_file:
    json.dump(data, write_file, indent=2)
