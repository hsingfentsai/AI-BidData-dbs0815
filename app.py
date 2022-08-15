#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask, render_template, request


# In[2]:


app = Flask(__name__)


# In[3]:


#dir(app)


# In[4]:


import joblib
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        rates = float(request.form.get("rates"))
        print(rates)
        model1 = joblib.load("regression_DBS")
        r1 = model1.predict([[rates]])
        model2 = joblib.load("tree_DBS")
        r2 = model2.predict([[rates]])
        return(render_template("index.html", result1=r1, result2=r2))
    else:
        return(render_template("index.html", result1="waiting", result2="waiting"))
    


# @app : decorator(force to run this first)<br>
# / : always the first directory to go to<br>
# render_template : the "index.html" file must inside template folder<br>
# else: before we press enter at the front end, always stay at "else:"<br>
# sklearn data structure needs two [ ] [ ] because it is two dimension<br>
# {{result1}}: 兩個{} {} means get from back end
# 

# In[ ]:


if __name__=="__main__":
    app.run(host="127.0.0.1", port=int("1111"))


# WSGI server: a protocal using to talk between front and back end.

# In[ ]:




