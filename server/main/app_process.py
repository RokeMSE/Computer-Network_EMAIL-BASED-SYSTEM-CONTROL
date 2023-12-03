import psutil
import os
import re
from AppOpener import open
from AppOpener import close


def list_apps():
    app_name = list()
    app_id = list()
    app_thread = list()

    cmd = 'powershell "gps | where {$_.mainWindowTitle} | select Description, ID, @{Name=\'ThreadCount\';Expression ={$_.Threads.Count}}'
    proc = os.popen(cmd).read().split('\n')
    tmp = list()
    for line in proc:
        if not line.isspace():
            tmp.append(line)
    tmp = tmp[3:]
    for line in tmp:
        try:
            arr = line.split(" ")
            if len(arr) < 3:
                continue
            if arr[0] == '' or arr[0] == ' ':
                continue

            name = arr[0]
            threads = arr[-1]
            ID = 0
            # iteration
            cur = len(arr) - 2
            for i in range(cur, -1, -1):
                if len(arr[i]) != 0:
                    ID = arr[i]
                    cur = i
                    break
            for i in range(1, cur, 1):
                if len(arr[i]) != 0:
                    name += ' ' + arr[i]
            app_name.append(name)
            app_id.append(ID)
            app_thread.append(threads)
        except:
            pass

    result = ''
    for item in [(id, name, thread)for id, name, thread in zip(app_id, app_name, app_thread)]:
        result += ' - '.join(str(i) for i in item) + '\n'

    return result


def list_processes():
    proc_pid = []
    proc_name = []
    proc_thread = []

    for process in psutil.process_iter():
        try:
            pid = process.pid
            name = process.name()
            threads = process.num_threads()

            proc_pid.append(pid)
            proc_name.append(name)
            proc_thread.append(str(threads))

        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    result = ''
    for item in [(id, name, thread) for id, name, thread in zip(proc_pid, proc_name, proc_thread)]:
        result += ' - '.join(str(i) for i in item) + '\n'

    return result


def kill(name):
    if name + ".exe" in (i.name() for i in psutil.process_iter()):
        close(name)
        return f"Process with name {name} was killed.\n"
    else:
        return f"Failed to kill application/process with name {name}.\n"


def start(name):
    open(name)
    if name + ".exe" in (i.name() for i in psutil.process_iter()):
        return f"Server started application/process with name {name}.\n"
    else:
        return f"Failed to start application/process with name {name}.\n"


def parse_msg(msg):
    command = [x for x in msg.split(" - ")]
    return command


def application_process(content):
    command = parse_msg(content)
    return_text = ""
    for item in command:
        result = ""

        if "List Application" in content:
            result = "List of application\n" + "Id - Name - Thread\n" + list_apps()

        if "List Process" in content:
            result = "List of process\n" + "Id - Name - Thread\n" + list_processes()

        if "Kill" in content:
            try:
                name = re.search(r"Kill\[name:(.*)\]", content).group(1)
            except:
                return_text += f"Wrong format at {content}\n"
                return_text += f"Format should be: Kill[name:<Application/Process name>]"
                continue

            result = "Kill application/process:\n" + kill(name)

        if "Start" in content:
            try:
                name = re.search(r'Start\[name:(.*)\]', content).group(1)
            except:
                return_text += f"Wrong format at {content}\n"
                return_text += f"Format should be: Start[name:<Application/Process name>]"
                continue

            result = "Start application:\n" + start(name)

        if result != "":
            return_text += "\n" + result

        print("Application/Process @@@ ### === ", result)

    return return_text
