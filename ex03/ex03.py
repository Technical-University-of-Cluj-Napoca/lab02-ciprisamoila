import os, datetime

def smart_try_catch(d: dict, key: str, default):
    res = default
    try:
        res = d[key]
    except KeyError:
        pass
    return res

def smart_log(*args, **kwargs) -> None:
    str_args = [str(a) for a in args]
    message = " ".join(str_args)
    level = smart_try_catch(kwargs, 'level', 'info')
    timestamp = smart_try_catch(kwargs, 'timestamp', True) # timestamp is allways shown except when told not to
    date = smart_try_catch(kwargs, 'date', False) # date in never shown except when told
    save_to = smart_try_catch(kwargs, 'save_to', "")
    color = smart_try_catch(kwargs, 'color', True)
    #print(level, timestamp, date, save_to, color)

    msg_complete = []
    dt = datetime.datetime.now()
    if date:
        msg_complete.append(str(datetime.date(dt.year, dt.month, dt.day)))
    if timestamp:
        msg_complete.append(str(datetime.time(dt.hour, dt.minute, dt.second)))
    msg_complete.append('[' + level.upper() + ']')
    msg_complete.append(message)

    log = " ".join(msg_complete)

    if save_to:
        with open(save_to, 'a') as f:
            f.write(log + '\n')

    if color:
        msg_complete.append("\033[0m")
        c = ""
        match level:
            case "info": c = "\033[0;34m"
            case "debug": c = "\033[0;30m"
            case "warning": c = "\033[1;33m"
            case "error": c = "\033[0;31m"
        msg_complete.insert(0, c)


    colored_log = " ".join(msg_complete)
    print(colored_log)

# if __name__ == "__main__":
#     username = os.getlogin()
#     smart_log("System started successfully.", level="info")
#     smart_log("User", username, "logged in", level="debug", timestamp=True)
#     smart_log("Low disk space detected!", level="warning", save_to="logs/system.log", date=True)
#     smart_log("Model", "training", 1, "failed!", level="error", color=True, save_to="logs/errors.log")
#     smart_log("Process end", color=False, timestamp = False, save_to="logs/errors.log")
