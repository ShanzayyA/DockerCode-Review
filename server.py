# Deployment server used
from waitress import serve

# Framework objects used
from flask import Flask, abort, Response
from flask_restful import Resource, Api

import forkrepos as  fr
import sonarcloud as sc
import code_review as cr

import json
import os



app = Flask(__name__)
api = Api(app)

class GithubCodeReview(Resource):

    def get(self, username):
        try:

            fr.ForkRepos(username)
            sc.SonarAnalysis()
            return cr.GetCodeReview()
        except: 
            abort(400)


api.add_resource(GithubCodeReview, '/<string:username>')

if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=8080)
