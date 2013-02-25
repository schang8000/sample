import os

class Config(object):
    DEBUG = True
    TESTING = False
    LOG_LEVEL = os.environ.get('LOG_LEVEL', 'DEBUG')
    FBAPI_APP_ID = '244705705666496' 
    FBAPI_APP_SECRET ='b5e74b6ea15965fbda483535db50de5e' 
    FBAPI_SCOPE = ['user_likes', 'user_photos', 'user_photo_video_tags']
