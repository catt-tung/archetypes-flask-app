from flask import render_template, url_for, flash, request, redirect, Blueprint, abort
from flask_login import current_user, login_required
from myapp import db 
from myapp.models import Post
from myapp.posts.forms import PostForm

posts = Blueprint('posts', __name__)