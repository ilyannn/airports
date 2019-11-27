import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///{}/data/airports.db'.format(basedir)
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    def perform_configuration(self, app_config):
        app_config['SQLALCHEMY_DATABASE_URI'] = self.SQLALCHEMY_DATABASE_URI
        app_config['SQLALCHEMY_TRACK_MODIFICATIONS'] = self.SQLALCHEMY_TRACK_MODIFICATIONS