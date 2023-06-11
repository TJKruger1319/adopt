from flask import Flask, render_template, redirect, request
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adoption'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "SECRET!"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

app.app_context().push()

connect_db(app)

@app.route('/')
def show_pets():
    """Renders list of pets"""
    pets = Pet.query.all()
    return render_template("petlist.html", pets=pets)

@app.route('/add')
def show_pet_form():
    """Renders the add pet form"""
    form = AddPetForm()
    return render_template("add_pet_form.html", form=form)


@app.route('/add', methods=["POST"])
def add_pet():
    """Validates and adds pet to database"""
    form = AddPetForm()
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data

        pet = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes)
        db.session.add(pet)
        db.session.commit()
        return redirect("/")
    else:
        return render_template("add_pet_form.html", form=form)
    
@app.route('/<int:pet_id>')
def show_pet(pet_id):
    """Shows the pet and gives access to the edit pet form"""
    form = EditPetForm()
    pet = Pet.query.get_or_404(pet_id)
    return render_template("pet.html", pet=pet, form=form)

@app.route('/<int:pet_id>', methods=["POST"])
def edit_pet(pet_id):
    """Upon vaidating the edited pet information, it puts it into the database"""
    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm()

    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.avaliable = form.avaliable.data
        db.session.commit()
        return redirect("/")
    else:
        return render_template("pet.html", pet=pet, form=form)