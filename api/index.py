from flask import Flask
app = Flask(__name__)

@app.route("/api/python")
def hello_world():
    return "<p>Hello, World!</p>"
# from flask import Flask, send_from_directory,current_app,jsonify,request,render_template
# from flask_restful import Api, Resource, reqparse
# from flask_cors import CORS #comment this on deployment
# from main import Chat,Recycle
# app = Flask(__name__)

# api = Api(app)

# app.config['CORS_HEADERS'] = 'Content-Type'
# app.config['UPLOAD_FOLDER'] = r'/*' 
# app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024


# @app.route("/", defaults={'path':''})
# def serve(path):
#     print(app.static_folder)
    
#     return send_from_directory(app.static_folder,'index.html')

# @app.errorhandler(500)
# def internal_server_error(error):
#     # Handle internal server errors and include the CORS header in the response
#     response = jsonify({'error': 'Internal Server Error'})
#     response.headers.add('Access-Control-Allow-Origin', '*')
#     return response, 500

# api.add_resource(Chat, '/api/chat')
# api.add_resource(Recycle, '/api/recycle')

# if __name__ == "__main__":
#     app.run()