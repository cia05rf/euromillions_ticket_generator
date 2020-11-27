import os
import platform

def loop_mk_dir(tgt_dir:str):
    """Take a dir string, attempt to create the tgt_dir.
    If it cannot it will loop back over the folders until it finds a root folder that exists.
    It will then build up a file structure"""
    #Check if this dir already exists
    if not os.path.isdir(tgt_dir) \
        and not os.path.isfile(tgt_dir):
        #Get the platform
        sep = "\\" if platform.system().lower() == "windows" else "/"
        #Check if the parent exists
        par_dir = sep.join(tgt_dir.split(sep)[:-1])
        if not os.path.isdir(par_dir):
            loop_mk_dir(par_dir)
        else:
            os.mkdir(tgt_dir)