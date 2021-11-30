<h1>Registration API</h1>
<h2 style="color: #3CB371">Mean libs</h2>
<h4>- Python 3.9.7</h4>
<h4>- Django 3.2.9</h4>
<h4>- Django REST Framework 3.12.4</h4>
<hr>
<h2 style="color: #6495ED">Description</h2>
<p>
    This is a simple API to register in database everything you need, the models created here are only<br/> 
    being used to register a simple user and their address. You can check it in registration_app/models.py. <br/>
    It was developed with <strong style="color: #3CB371">Django, Django REST Framework, PostegreSQL as SGBD </strong> and some other libs <br/>
    that you can find in requirements.txt file. 
</p>

<h2 style="color: #6495ED">A initial consideration</h2>
<p>
    There's some implemetations to make. Fell free to modifi it how you likes. Report me if you find some issue <br/>
    or if you have some improvement sugestion. Thanks!<br/>
    <strong>Note: I'll deploy it on AWS in future. Enjoy it!</strong>
</p>

<h2 style="color: #6495ED">Authentication</h2>
<p>
    After you create a new user you'll need to request a JWT Token to make requests in all endpoints for post, get <br/>
    dlete, and put methods. <br/>
    Note: I added a new method called filter for you get especifique informations in any table sending the <br/>
    primary key and the field or fields you need to filter. If you to need filter more than one iformation <br/>
    send the fields in a list ex.: <strong style="color: #3CB371">['first_name', 'email']</strong>.
</p>

<h2 style="color: #6495ED">Instalation</h2>
<p>
    To run this API locally you'll need to install Python according of your machine Operational Sistem,<br>
    you can download it here: <a href="https://www.python.org/downloads/">Python Download</a>.<br/>
</p>
<hr>
<p>
    I recomend you create a virtual enviroment and install there all the libs of requirements.txt file. if you don't<br/>
    know how to do it you can see here how to do it: 
    <a href="https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/26/python-virtual-env/">Python Virtual Environments</a><br/>
</p>
<hr>
<p>
    To install the libs of requirements.txt you'll need to surf in your terminal ( recomend you have your virtual enviroment activeted already )
    till the root of this project and run the command <strong style="color:#F0E68C"> pip install -r requirements.txt </strong>.
</p>
<hr>
<p>
    <strong style="color: #DC143C">Note: Before you follow the next step pass the database credentials in settings.py DATABASES variable.<br/></strong>
    If all the libs were install with sucessfull check the connection with your database, in this project I'm using <br/>
    the SGBD PostgreSQL, runing the command <strong style="color:#F0E68C">python manage.py migrate</strong>.
    This command will create the tables in your database.
</p>
<hr>
<p>
    If the before step was executed with successfull you can run the command <strong style="color:#F0E68C"> python manage.py runserver</strong><br/>
    and access <a>http://127.0.0.1:8000/documentation/</a> to see the end points already created and how they work.
</p>
<hr>
<h2>Final Considerations</h2>
<p style="color: #FF0000">
    All steps teached here are for local usege of this api. If you want to use it in production you'll need to see <br/>
    how to deploy it in platforms you choise.
</p>
<p>Here you can see a basic way to deploy on Heroku</p>
<li><a href="https://www.youtube.com/watch?v=8l8xwvRO1_U&ab_channel=SamuelGon%C3%A7alves">Deploing on Heroku - Samuel Gonçalves</a></li>
<p>
    I hope you enjoy to use it, you can clone this project and use how you like. I just ask you send me a message if <br/>
    you'll use this project in some production.<br/>
    <strong></strong>
</p>    
<h3>Contact me</h3>
<ul>
    <p>If you need some help for use this API contact me.</p>
    <li><a href="https://www.linkedin.com/in/marcos-vin%C3%ADcius-alves-da-silva-1b6017132">Linkedin</a></li>
    <li><a href="https://www.facebook.com/marcos.vinicius.18062">Facebook</a></li>
    <li><a href="https://wa.me/+5544991837743">WhatsApp</a></li>
</ul>
