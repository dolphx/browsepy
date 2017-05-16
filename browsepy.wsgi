import sys
import os
activate_this='/home/gar-portal/browsepy/env/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(__file__)),'.'))

sys.path.append('/home/gar-portal/browsepy/')


from browsepy import app as application
application.config['directory_start']='/mnt/UNISDR'
application.config['directory_base']='/mnt/UNISDR'
application.config['directory_ignore'] = ['MedellinCompleto', 'Meta']
application.config["use_binary_multiples"] = False
application.config['title'] = 'UNISDR Global Assessment Report Download Portal'

