from . import bp as social
from flask import render_template, flash, url_for, redirect, request
from app.models import User, Post
from flask_login import current_user, login_required


# INDEX for easier access
@social.route('/', methods=['GET', 'POST'])
@login_required
def index():
    if request.method == 'POST':
        body = request.form.get('body')

        new_post = Post(body=body, user_id = current_user.id)
        # always save changes to data inside a db!
        new_post.save()
        # successful post - green
        flash('Thanks for keeping these posts appropriate for our young visitors!','success')
        return redirect(url_for('social.index'))
    posts = current_user.followed_posts()
    return render_template('index.html', posts=posts)


# DELETE
@social.route('/delete_post/<int:id>')
@login_required
def delete_post(id):
    # Get post with the post id from the database
    post = Post.query.get(id)   
    # Is user the post author?
    if post and post.author.id != current_user.id:
        # Warning message
        flash('You are not authorized to delete to this post.', 'danger')
        # I approve this redirect - no change
        return redirect(url_for('social.index'))
        # Delete the post
    post.delete()
        # User feedback
    flash("Your post has been deleted as requested.","primary")
    # Send them back from whence they came - love that phrase!
    return redirect(request.referrer or url_for('social.index'))

# EDIT
@social.route('/edit_post/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_post(id):
    # Get post with the post id from the database
    post = Post.query.get(id)
    # author = curent user?
    if post and post.author.id != current_user.id:
        flash('You are not authorized to make changes to this post.', 'danger')
        return redirect(url_for('social.index'))
    # if its a GO!
    if request.method == 'POST':
        # Edit the post with the new infomation from the form
        post.edit(request.form.get('body'))
        post.save()
        # User Feedback
        flash('Your post has been edited.', 'success')
        # Send them back edit post page (my_posts)
        return redirect(url_for('social.my_posts'))
    # show the the edit post page
    return render_template('edit_post.html.j2', post=post)

# Allow current user to see all other users
@social.route('/show_users')
@login_required
def show_users():
    users = User.query.filter(User.id != current_user.id).all()
    return render_template('show_users.html.j2', users=users)

# current user may choose to follow another user
@social.route('/follow/<int:id>')
@login_required
def follow(id):
    user_to_follow = User.query.get(id)
    current_user.follow(user_to_follow)
    flash(f"You are now following {user_to_follow.first_name} {user_to_follow.last_name}.", "success")
    return redirect(url_for("social.show_users"))

# allow current user to unfollow a formerly followed user
@social.route('/unfollow/<int:id>')
@login_required
def unfollow(id):
    user_to_unfollow = User.query.get(id)
    current_user.unfollow(user_to_unfollow)
    flash(f"You are no longer following {user_to_unfollow.first_name} {user_to_unfollow.last_name}.", "warning")
    return redirect(url_for("social.show_users"))

# current user may view a single post
@social.route('/post/<int:id>')
@login_required
def get_a_post(id):
    post = Post.query.get(id)
    return render_template('single_post.html.j2', post=post, view_all=True)

# current user may view all of his/her own posts
@social.route('/post/my_posts')
@login_required
def my_posts():
    # posts = Post.query.filter_by(user_id = current_user.id).all()
    return render_template('my_posts.html.j2', posts=current_user.posts.all())