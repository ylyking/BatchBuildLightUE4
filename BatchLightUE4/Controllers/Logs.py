import os
import sys
import shutil
from ..Models.DB import paths_dict

# This files create a copy of your Unreal log file, useful to see easily
# your rendering errors.

def logsave(level):

    level = level + ".log"
    root_path = sys.path[0]
    # root_path = os.path.dirname(sys.modules['__main__'].__file__)
    log = paths_dict['UE4 Project']

    src = os.path.dirname(log) + "\Saved\Logs\ProVolley.log"
    src = os.path.normpath(src)
    dst = os.path.dirname(root_path) + r'/Logs/' + level
    dst = os.path.normpath(dst)

    if not os.path.exists(os.path.dirname(dst)):
        os.makedirs(os.path.dirname(dst))

    print("Main Module >> ", root_path)

    shutil.copyfile(src, dst)