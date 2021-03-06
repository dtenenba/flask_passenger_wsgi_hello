#!/usr/bin/python3

import os

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    message = """
<html>
<head>
<title>A sample Flask App</title>
</head>
<body>

<h1>Sample Flask App</h1>

<p>This is a flask app running in Passenger,
inside Open OnDemand. Written by Dan.
Its source is <a href="https://github.com/dtenenba/flask_passenger_wsgi_hello">here</a>.</p>

<p>You can develop any kind of app and deploy it
in OnDemand. </p>

<p>There are two kinds of apps, Passenger Apps
and Interactive Apps. </p>

<p>Passenger apps (of which this is one) 
run on the same machine that runs
Open OnDemand and they need to be written
in some language that works with WSGI and 
passenger (the main ones are Ruby, Python, and Node.js).</p>

<p>A couple nice things about these apps are:</p>

<ul>
<li>You don't have to worry about authentication. 
    The user is already signed in before this app
    runs.</li>
<li>This app is actually running as your user, not
     as <i>apache</i> or <i>www-data</i>. Here is
     the value  of the <code>USER</code> environment variable:</li>
     <b>{}</b>
</li>
</ul>

<p>A word about Interactive apps - they can be written
in any language, and instead of running on the
machine that runs Open OnDemand, they run on a cluster node.
So we can set up RStudio Server and Jupyter as Interactive apps.
We can create some nice interface for Cromwell as well. 
</p>

<p>
Another interesting thing about Interactive apps
is that they do not have to be web applications - 
they can be any X11 app. Magically using VNC these are 
proxied and presented in a web browser. 
</p>

<p>The main example of a Interactive app (which is shipped
as part of Open OnDemand) is the ability
to open a virtual desktop on a cluster node
inside your browser window. </p>

<p>Note that Interactive apps require some software
(Sockify, nmap-ncat, and TurboVNC) to be installed on all cluster nodes.
Hopefully this should be a small addition to our chef recipes.</p>

<p>I will create a demo of an Interactive app soon.</p>

<p>Another thing that is sort of a hybrid of these two app types
is the terminal shell. In Open OnDemand, click on the <code>Clusters</code> menu 
and then click <code>CLUSTER_NAME_PLACEHOLDER shell access</code>. 
You'll get a shell/terminal right in your browser window. 
This shell is on the same machine as Open OnDemand. </p>

</body>
</html>
    """
    return message.format(os.getenv("USER").strip())

if __name__ == "__main__":
    app.run()
