from flask import Blueprint
from flask import request, render_template, redirect, url_for, session, flash
from flask_wtf import FlaskForm
from wtforms import TextAreaField, HiddenField, SubmitField, Form, StringField, SelectField
from wtforms.validators import DataRequired, Length, ValidationError

import movies.adapters.repository as repo
import movies.movie_library.movie_library as movie_library
import movies.search.services as services

search_blueprint = Blueprint(
    'search_bp', __name__)

@search_blueprint.route('/search', methods=['GET', 'POST'])
def search():
    search = MovieSearchForm(request.form)
    if request.method == 'POST':
        return search_results(search.data['search'], search.data['select'])

    return render_template('search/search.html',
                           form=search,
                           title="Search for Movies",
                           description="Search for movies by category.")

@search_blueprint.route('/results')
def search_results(search, select):
    search = search.title()
    searchExists = services.search_exists(search, select, repo.repo_instance)

    if searchExists:
        if select == "Actor":
            return redirect(url_for('movie_library_bp.movies_by_actor', actor=search))
        elif select == "Genre":
            return redirect(url_for('movie_library_bp.movies_by_genre', genre=search))
        elif select == "Director":
            return redirect(url_for('movie_library_bp.movies_by_director', director=search))
    else:
        flash('No results found!')
        return redirect(url_for('search_bp.search'))

class MovieSearchForm(Form):
    choices = [('Actor', 'Actor'),
               ('Director', 'Director'),
               ('Genre', 'Genre')]
    select = SelectField('Search for movie:', choices=choices)
    search = StringField('')

