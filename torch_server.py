import argparse
import logging
import sys
import time

import falcon
from falcon_cors import CORS
import json
import waitress
import lawa
import lawrouge
from operator import itemgetter

if sys.hexversion < 0x03070000:
    ft = time.process_time
else:
    ft = time.process_time_ns
    
logging.basicConfig(level=logging.INFO, format='%(asctime)-18s %(message)s')
logger = logging.getLogger()
cors_allow_all = CORS(allow_all_origins=True,
                      allow_origins_list=['*'],
                      allow_all_headers=True,
                      allow_all_methods=True,
                      allow_credentials_all_origins=True
                      )

parser = argparse.ArgumentParser()
parser.add_argument(
    '-p', '--port', default=58086,
    help='falcon server port')
args = parser.parse_args()


class TorchResource:

    def __init__(self):
        logger.info("...")
        self.rouge = lawrouge.Rouge(isChinese=True)
        logger.info("###")

    def process_context(self, target, candidates):
        start = ft()
        candidates = [candidate for candidate in candidates if len(candidate.strip()) > 0]
        pairs = zip([target] * len(candidates), candidates)
        scores = [self.rouge.get_scores([t],[c], avg=2) for t,c in pairs]
        f_scores = [score['f'] for score in scores]
        index, element = max(enumerate(f_scores), key=itemgetter(1))
        logger.info("score:{}ns".format(ft() - start))
        return {'score':element,'index':index, 'candidate':candidates[index]}

    def on_get(self, req, resp):
        logger.info("...")
        resp.set_header('Access-Control-Allow-Origin', '*')
        resp.set_header('Access-Control-Allow-Methods', '*')
        resp.set_header('Access-Control-Allow-Headers', '*')
        resp.set_header('Access-Control-Allow-Credentials', 'true')
        target = req.get_param('target', True)
        candidates = req.get_param('candidates', True)
        # mode = req.get_param('mode', default=0)
        resp.media = self.process_context(target, candidates)
        logger.info("###")

    def on_post(self, req, resp):
        """Handles POST requests"""
        resp.set_header('Access-Control-Allow-Origin', '*')
        resp.set_header('Access-Control-Allow-Methods', '*')
        resp.set_header('Access-Control-Allow-Headers', '*')
        resp.set_header('Access-Control-Allow-Credentials', 'true')
        resp.set_header("Cache-Control", "no-cache")
        start = ft()
        jsondata = json.loads(req.stream.read(req.content_length))
        target=jsondata['target']
        candidates = jsondata['candidates']
        resp.media = self.process_context(target, candidates)
        logger.info("tot:{}ns".format(ft() - start))
        logger.info("###")


if __name__ == "__main__":
    api = falcon.API(middleware=[cors_allow_all.middleware])
    api.req_options.auto_parse_form_urlencoded = True
    api.add_route('/z', TorchResource())
    waitress.serve(api, port=args.port, threads=48, url_scheme='http')
