import logging
import requests

log = logging.getLogger(__name__)

class LoadTest(object):
    def __init__(self, gun):
        self.gun = gun

    def setup(self, param):
        log.info('Starting LoadTest: %s', param)

    def case_get(self, projectile):
        with self.gun.measure('case_get'):
            log.info('Shoot! GET-method: %s', projectile)
            requests.get(projectile)

    '''def case_post(self, projectile):
        with self.gun.measure('case_post'):
            log.info('Shoot! POST-method: %s', projectile)
            requests.post(projectile)'''
