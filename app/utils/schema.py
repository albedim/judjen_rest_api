WELCOME_EMAIL = '''
<!DOCTYPE html>
<html lang="en">
<head>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cabin:ital,wght@0,400;0,500;0,600;0,700;1,400;1,500;1,600;1,700&display=swap" rel="stylesheet">

  <style>
    h1, h2, p{
      font-family: 'Cabin', sans-serif;
      display: flex;
    }
    .a{
      font-family: 'Cabin', sans-serif;
    }
    h2 {
      font-size: larger;
      color: gray;
    }
    .c{
      color: #668AE4;
    }
    .u{
      text-decoration: underline;
      text-decoration-color: #668AE4;
    }
    .flex{
      display: flex;
    }
    .a{
      background-color: #668AE4;
      color: white;
      padding: 18px;
      padding-right: 34px;
      padding-left: 34px;
      text-decoration: none;
      border: none;
      border-radius: 4px;
    }
    p{
      font-size: large;
    }
    .mt{
      margin-top: 40px;
    }
  </style>

</head>
<body>
  <div>
    <div>
      <div class="flex">
        <h1>Hey</h1><h1 class="c">{anonymous_name}</h1><h1>,  Welcome to JudJen!</h1>
      </div>
    </div>
    <div style="margin-top: -14px;">
        <p>{anonymous_name} is how all JudJers are going to call you
          <br>This is your anonymous name, personal Identifer or whatever...
          <br>Just Have fun, read of cringe stories and tell us yours!</p>
        </p>
    </div>
    <div class="mt">
      <a class="a" href={BASE_FE_URL}>
        Get Started
      </a>
    </div>
  </div>
</body>
</html>
'''

RECOVER_PASSWORD_EMAIL = '''
<!DOCTYPE html>
<html lang="en">
<head>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cabin:ital,wght@0,400;0,500;0,600;0,700;1,400;1,500;1,600;1,700&display=swap" rel="stylesheet">

  <style>
    h1, h2, p{
      font-family: 'Cabin', sans-serif;
      display: flex;
    }
    .a{
      font-family: 'Cabin', sans-serif;
    }
    h2 {
      font-size: larger;
      color: gray;
    }
    .c{
      color: #668AE4;
    }
    .u{
      text-decoration: underline;
      text-decoration-color: #668AE4;
    }
    .flex{
      display: flex;
    }
    .a{
      background-color: #668AE4;
      color: white;
      padding: 18px;
      padding-right: 34px;
      padding-left: 34px;
      text-decoration: none;
      border: none;
      border-radius: 4px;
    }
    p{
      font-size: large;
    }
    .mt{
      margin-top: 40px;
    }
  </style>

</head>
<body>
  <div>
    <div>
      <div class="flex">
        <h1>Recover your password </h1><h1 class="c">{anonymous_name}</h1></h1>
      </div>
    </div>
    <div style="margin-top: -14px;">
        <p>This email was sent in order to make you recover your password. 
          <br>Tap the button and follow the steps to recover your password
          <br>Don't reply this email please, thank you!</p>
        </p>
    </div>
    <div class="mt">
      <a class="a" href={RECOVER_PASSWORD_URL}>
        Recover your password
      </a>
    </div>
  </div>
</body>
</html>
'''