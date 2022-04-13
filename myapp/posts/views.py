from flask import render_template, url_for, flash, request, redirect, Blueprint, abort
from flask_login import current_user, login_required
from myapp import db 
from myapp.models import Post
from myapp.posts.forms import PostForm, PostUpdateForm

posts = Blueprint('posts', __name__)

# Create
@posts.route('/create', methods=['GET', 'POST'])
@login_required
def create_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, category=form.category.data, content=form.content.data, user_id=current_user.id)
        db.session.add(post)
        db.session.commit()
        flash('Post Created')
        print('Post was created')
        return redirect(url_for('core.index'))
    return render_template('create_post.html', form=form)

# Show
@posts.route('/<int:post_id>')
def post(post_id):
    post = Post.query.get_or_404(post_id) 
    return render_template('post.html', title=post.title, date=post.date, post=post)

# Update
@posts.route('/<int:post_id>/update',methods=['GET','POST'])
@login_required
def update(post_id):
    post = Post.query.get_or_404(post_id)

    if post.author != current_user:
        abort(403)

    form = PostUpdateForm()

    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        post.category = form.category.data
        db.session.commit()
        flash('Post Updated')
        return redirect(url_for('posts.post',post_id=post.id))

    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
        form.category.data = post.category

    return render_template('update_post.html',title='Updating',form=form)

# Delete
@posts.route('/<int:post_id>/delete',methods=['GET','POST'])
@login_required
def delete_post(post_id):

    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)

    db.session.delete(post)
    db.session.commit()
    flash('Post Deleted')
    return redirect(url_for('core.index'))

# Show by Category
#Child
@posts.route('/child')
def post_child():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.filter_by(category = 'Child').paginate(page=page, per_page=5) 
    return render_template('child.html', posts=posts)

#Victim
@posts.route('/victim')
def post_victim():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.filter_by(category = 'Victim').paginate(page=page, per_page=5) 
    return render_template('victim.html', posts=posts)

#Saboteur
@posts.route('/saboteur')
def post_saboteur():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.filter_by(category = 'Saboteur').paginate(page=page, per_page=5) 
    return render_template('saboteur.html', posts=posts)

#Prostitute
@posts.route('/prostitute')
def post_prostitute():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.filter_by(category = 'Prostitute').paginate(page=page, per_page=5) 
    return render_template('prostitute.html', posts=posts)