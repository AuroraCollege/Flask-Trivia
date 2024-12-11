# Trivia [Example Solution]
This is a basic trivia app for learning the basics of SQL Alchemy.

Have a look through _all_ the files to get an idea of how it goes together. 

## Your Task 
Lets record the score from each attempt and create a high score page. This is not using user accounts or anything fancy - more like a simple pinball-machine stile high schore page.

### 1. Getting the user's name

Let's start by giving the user somewhere to add their name with their attempt. 

```html
<div>
    <label for="name">Enter your name:</label>
    <input type="text" id="name" name="name" required>
</div>
```
This will provide an input like this:

<div>
    <label for="name">Enter your name:</label>
    <input type="text" id="name" name="name" required>
</div>

### 2. Giving us somewhere to store it

Jump into the `models.py` file, and add a new `class` called `User`, that extends from `Base` in the same way that the `Question` class does already.

Using the `Question` class as a template, add a `tablename` (users), an `id` column, a `name` column and a `score` column. 

### 3. Migrate the changes to the database

The only change required in the `init_db.py` file is to add `Question` to the models you are importing:

``` python
from models import Base, Question
```

### 4. Update app.py
`app.py` will also need access to the new model:
```python
#app.py
from models import Base, Question, User
```
In the `submit()` route, you will need to get the user's name from the POST request, and initialise a `score` variable:
```python
name = request.form.get("name")
score = 0
```

Inside your `for` loop, increment your score for each question that is answered correctly:
```python 
score += 1 
```

And most importantly, store the attempt in the database! 

We will create a new user object (using the `User` class we imported earlier), add the user to the session, and then commit our change to the database. 

```python
# Create a new User object
user = User(name=name, score=score) 
# Add the user to the session
session.add(user) 
# Commit the changes to the database
session.commit() 
```

### 5. Display the results!
Show the results of this attempt by rendering the template:

```python
return render_template("results.html", name=name, score=score)
```
Addinng something like this in `results.html`:
```html

    <h1>Results</h1>
    <p>Thank you, {{ name }}!</p>
    <p>Your score: {{ score }}</p>
    <a href="{{ url_for('index') }}">Try Again</a>
```

## Challenge

Once you have this working, your next challenges are:
1. Add a leaderboard! (You'll probably want more questions)
2. Add functionality to delete anyone below the top 10 high scores to avoid the database growing too big.
3. Implement the ability to add new questions into the quiz app! 
