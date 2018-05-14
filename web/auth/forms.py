import re
from flask_wtf import FlaskForm

from wtforms.fields import TextField, SelectField, StringField, PasswordField, BooleanField, SubmitField
from wtforms.fields.html5 import URLField
from wtforms.validators import ValidationError, url, length, regexp, optional, DataRequired, Email, EqualTo
from dao import Departement
from bson.objectid import ObjectId

#TODO: Make this usable
class SettingsForm(FlaskForm):
    """docstring for SettingsForm"""

    ui_lang = SelectField(
        label="Primary site language",
        description="Site will try to show UI labels using this " +
            "language. User data will be shown in original languages.",
    )
    url = URLField(
        label="Personal site URL",
        description="If you have personal site and want to share " +
            "with other people, please fill this field",
        validators=[optional(), url(message="Invalid URL.")])
    username = TextField(
        label="Public profile address",
        description="Will be part of your public profile URL. Can " +
            "be from 2 up to 40 characters length, can start start from [a-z] " +
            "and contains only latin [0-9a-zA-Z] chars.",
        validators=[
            length(2, 40, message="Field must be between 2 and 40" +
            " characters long."),
            regexp(r"[a-zA-Z]{1}[0-9a-zA-Z]*",
                re.IGNORECASE,
                message="Username should start from [a-z] and " +
                    "contains only latin [0-9a-zA-Z] chars")
        ]
    )

class RegistrationForm(FlaskForm):
    prenom = StringField('Prénom', validators=[DataRequired()])
    nom = StringField('Nom', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    departement = SelectField('Département INSA', choices=[(d._id, d.nom) for d in Departement.get_all()], coerce=ObjectId, validators=[DataRequired()])
    niveau = SelectField('Année d\'études', choices=[('3', '3A'), ('4', '4A')], validators=[DataRequired()])
    mobilite = SelectField('J\'ai déjà effectué une mobilité internationale : ', choices=[('o', 'Oui'), ('n', 'Non')], validators=[DataRequired()])
    mdp = PasswordField('Mot de passe', validators=[DataRequired()])
    mdp2 = PasswordField('Répétez le mot de passe', validators=[DataRequired(), EqualTo('mdp')])
    submit = SubmitField('S\'inscrire')


class LoginForm(FlaskForm):
    """Login form to access writing and settings pages"""

    email = StringField('Email', validators=[DataRequired(), Email()])
    mdp = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Se souvenir de moi')
