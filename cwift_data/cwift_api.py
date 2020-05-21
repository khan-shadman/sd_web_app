import urllib 
import datetime as d
import dload
# from carrot.utilities import publish_task
from carrot.utilities import create_scheduled_task
from django.conf import settings
import os 


def get_cwift(date=2016):

    if date < int(d.datetime.now().year) - 1:
        dload.save_unzip("https://nces.ed.gov/programs/edge/data/EDGE_ACS_CWIFT2015.zip", os.path.join(settings.BASE_DIR, 'cwift_data\\static\\'))
    # resp = urllib.urlopen("https://nces.ed.gov/programs/edge/data/EDGE_ACS_CWIFT2015.zip")
    return "This is working"

# publish_task(get_cwift,  int(d.datetime.now().year))


create_scheduled_task(get_cwift, {'months': 6}, int(d.datetime.now().year))