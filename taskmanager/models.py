from taskmanager import db


class Category(db.Model):
    # schema for the Category model
    id = db.Column(db.Integer, primary_key=True)
    # sets string length max to 25, must be unique, can't be empty/blank
    category_name = db.Column(db.String(25), unique=True, nullable=False)
    # no Column used so invisible. Targets the Task table
    # backref targets itself - deleting the category deletes related tasks
    # cascade all, delete - finds all related tasks and deletes them
    # lazy, when query database for category it should find all tasks linked
    tasks = db.relationship(
        "Task", backref="category", cascade="all, delete", lazy=True)

    def __repr__(self):
        # __repr__ python function means to represent itself as a string
        # Similar to using (this) in Javascript.
        return self.category_name


class Task(db.Model):
    # schema for the Task model
    id = db.Column(db.Integer, primary_key=True)
    task_name = db.Column(db.String(50), unique=True, nullable=False)
    # text is a longer string
    task_description = db.Column(db.Text, nullable=False)
    # Boolean is a check box, default is not required
    is_urgent = db.Column(db.Boolean, default=False, nullable=False)
    # Date shows the date
    due_date = db.Column(db.Date, nullable=False)
    # Foreign key allows database to see links between other tables
    # ondelete = CASCADE, if a category_id is deleted
    # associated tasks will also be deleted
    category_id = db.Column(db.Integer, db.ForeignKey(
        "category.id", ondelete="CASCADE"), nullable=False)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        # placeholders used in 0,1,2. then self.id links them
        return "#{0} - Task: {1} | Urgent: {2}".format(
            self.id, self.task_name, self.is_urgent
        )
