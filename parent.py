import subprocess
import time
import json
import os

with open("./config.json") as configfile:
    config = json.load(configfile)
config = config["background"]

def term_output(cmd):
    proc = subprocess.Popen(str(cmd), shell=True, stdout=subprocess.PIPE,)
    output = proc.communicate()[0].decode("utf-8")
    lines = output.split("\n")
    return lines

def kill_process(pid):
    cmd = config["kill_cmd"] + str(pid)
    os.system(cmd)

def get_pid_data():
    output = {"strout": {"key": "","val": ""}, "clean": {}}

    # get and setup tile for ps command output
    title_cmd = config["get_ps_titles"]
    key = term_output(title_cmd)
    key = str(key[0])
    output["strout"]["key"] = key # store original output
    key = " ".join(key.split())
    key = key.split()

    # get and setup value from ps grep python command output
    daudio_pids = config["get_ps_target"]
    values = term_output(daudio_pids)
    values = str(values[0])
    output["strout"]["val"] = values # store original output
    values = " ".join(values.split())
    values = values.split()

    if config["invalid_ps_out"] in output["strout"]["val"]:
        return None
    else:
        data = {}
        for i in range(len(key)):
            if i == len(key) - 1:
                data[key[i]] = " ".join(values[i:len(values)])
            else:
                data[key[i]] = values[i]
        output["clean"] = data

        return output

# MAIN FUNCTION CALLS
while(True):
    # check if target process is running (config["background"]["get_ps_target"])
    process_loopup = get_pid_data()

    # target process not running, so try to rerun the process
    if process_loopup == None:
        cmd = config["process_cmd"]
        os.system(cmd)

    time.sleep(1)

