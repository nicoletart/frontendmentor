from flask import Flask, request, render_template, Markup
import food

 
# Flask constructor
app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True
 
inv = None
# A decorator used to tell the application
# which URL is associated function
@app.route('/', methods =["GET", "POST"])
def gfg():
      final = ""
      inv = ""
      if request.method == "GET":
        food.empty_fridge()
      if request.method == "POST":
       # getting input with name = fname in HTML form
         inv = request.form.get("inventory")
       # getting input with name = lname in HTML form
         inv = food.add_food(inv)
         inv = food.lookInFridge(inv)
         inv = food.listToString(inv)
         food.check()
         final = food.generator()
      return render_template("form.html", final = final, inv = inv)

@app.route('/dell', methods =["GET", "POST"])
def dell(): 
  if request.method == "POST":
    food.empty_fridge()
  return render_template("form.html")


if __name__=='__main__':
   app.run()


