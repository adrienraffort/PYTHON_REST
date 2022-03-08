from flask_restful import reqparse, abort, Api, Resource

from flask import Flask, jsonify
from flask_cors import CORS, cross_origin


app = Flask(__name__)
api = Api(app)

app.config['CORS_HEADERS'] = 'Content-Type'




parser = reqparse.RequestParser()
parser.add_argument('task')


class Trajet(Resource):
    def get(self, km_parcours, km_voiture, temps_recharge):
        kp: int = int(km_parcours)
        kv: int = int(km_voiture)
        tr: int = int(int(temps_recharge) * 60)
        temps: int = int(0)
        log = ""
        km: int = int(kv)
        while kp > 0:
            if km > 0 and kp > km:
                kp -= km
                temps = temps + km * 40
                km = 0
                log += " 1:" + str(temps) + " "

            if km > 0 and kp <= km:
                temps = temps + int(kp * 40)
                kp = 0
                log += " 2:" + str(temps) + " "

            if km <= 0:
                temps = temps + tr
                km = kv
                log += " 3:" + str(temps) + " "



        return {"time" : int(temps), "log" : log}, 201


api.add_resource(Trajet, '/trajet/<km_parcours>/<km_voiture>/<temps_recharge>')


if __name__ == '__main__':
    app.run(debug=True)
