import db_engine as eng
import matplotlib.pyplot as plt
from flask import Flask, send_file
from flask import render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return send_file("templates/index.html")

# @app.route("/movie_page")
# def movie_page(processed_text):
# 	if processed_text:
# 		ms = eng.get_matched_movie_names(processed_text)
# 		if len(ms) > 0:
# 			mid = ms[0][0]
# 			md = eng.get_movie_page_data(mid)
# 		else:
# 			md = {'title': "No Movie is Found"}
# 	else:
# 		md = {'title': "No Movie is Selected"}

# 	return render_template("movie_page.html", md = md)

def plot_figure(x, y):
	plt.plot(x, y, '-o') # draw a figure of x and y
    plt.title(expr_name) # set the title of the figure
    plt.xlabel('Temperature (k)') # set x label 
    plt.ylabel(ylabel + ' Evolution') # set y label
    # plt.grid(True) # draw grid of the figure to make it more readable
    plt.savefig(output_folder + ylabel.lower() + '_' + expr_name + '.png')


@app.route("/movie_page/<name>")
@app.route("/movie_page/")
def movie_page(processed_text = None):  
	print 'called with this name: ' + str(processed_text)  
	if processed_text:
		ms = eng.get_matched_movie_names(processed_text)
		print ms
		if len(ms) > 0:
			mid = ms[0][0]
			md = eng.get_movie_page_data(mid)

			md["temporal_fig_address"]
		else:
			md = {'title': "No Movie is Found"}
	else:
		md = {'title': "No Movie is Selected"}

	return render_template("movie_page.html", md = md)

@app.route("/movie_page/", methods=['POST'])
@app.route("/", methods=['POST'])
def my_form_post():
    text = request.form['movie_name']
    processed_text = text.upper()
    print 'recieved this movie name: ' + str(processed_text)
    return movie_page(processed_text)


if __name__ == "__main__":
    app.run(host='0.0.0.0')