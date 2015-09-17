import json
import requests


class Connection(object):
    def __init__(self):
        # self.base_url = "http://10.12.202.141:9999/tournaments/master/"
        self.base_url = "http://10.12.202.144:9999/tournaments/sandbox-4/"
        self.headers = {'Authorization': 'WaryCoralCockroachGoose', 'Content-Type': 'application/json'}

    def get(self, endpoint):
        """
        curl -w"\n" 'http://10.12.202.141:9999/tournaments/main/games/my/setup' -H 'Authorization: Secret' -H 'Content-Type: application/json'
        """
        return requests.get(self.base_url + endpoint, headers=self.headers)

    def post(self, endpoint, data):
        """
        curl -w"\n" 'http://10.12.202.141:9999/tournaments/main/games/my/setup' -H 'Authorization: Secret' -H 'Content-Type: application/json'
        """
        response = requests.post(self.base_url + endpoint, data=json.dumps(data), headers=self.headers)
        return json.loads(response.content)

    def get_game(self):
        return self.get('games/my/setup')

    def submit_move(self, shot_angle=None, shot_power=None, move_distance=None):
        """
        mabn@hackkrk$ curl 'http://10.12.202.141:9999/tournaments/main/moves' -H
        'Content-Type: application/json' -H 'Authorization: MagnanimousHoneyDewWombatPony'
        --data-binary $'{\n  "shotAngle": 0,\n  "shotPower": 0,\n  "moveDistance": 10\n}'
        """
        data = {
            "shotAngle": shot_angle,
            "shotPower": shot_power,
            "moveDistance": move_distance,
        }
        return self.post('moves', data=data)