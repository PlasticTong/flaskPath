from flask import Flask, request
from path import Tn_paths
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources=r'/*')


@app.route('/mesfilter/path_generation', methods=['POST'])
def path_generation():
    from path import Tn_paths
    data_dict = request.get_json()
    data = data_dict['data']
    parameter = data_dict['parameter']
    metrix =Tn_paths(data,parameter['k'],parameter['delta'])
    # print(metrix)
    return metrix


if __name__ == '__main__':
    app.run(host='0.0.0.0',port='5002')
