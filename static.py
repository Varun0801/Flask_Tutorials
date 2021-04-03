# A web application often requires static files.
# JavaScript file or CSS file supporting a web page.
# Usually the web server is configured to serve them.
# During development these files are served from static folder in your package or next to your module.
# Available at /static on the application.
# A special endpoint 'static' used to generate URL for static files.
                # url_for('static', filename = 'style.css')
# app.static_url_path --> can be used to specify a different path for the static files on the web. Defaults to the name of the static_folder #folder.
# app.static_folder --> the folder with static files that should be served at static_url_path. Defaults to the 'static' folder in the root #path of the application. 

from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug = True)