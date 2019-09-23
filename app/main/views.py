from flask import render_template,request,redirect,url_for,abort
from flask_login import login_required, current_user
from .. import db, photos
import markdown2 
from . import main
from ..models import User,Blog,Comment,Quote,Subscribers
from .forms import UpdateProfile,PostBlog,PostCommentForm,SubscribeForm
from ..requests import get_quotes
from ..email import mail_message


@main.route('/')
def index():

    title='Blog'
    blogs=Blog.query.all()

    random_quotes = get_quotes()

    return render_template('index.html',title=title,blogs=blogs,quotes=random_quotes)

#User profile 

@main.route('/user/<fname>',methods=['GET','POST'])
def profile(fname):
    user = User.query.filter_by(firstname = fname).first()
    blogs = Blog.query.filter_by(user_id=current_user.id).all()



    return render_template("profile/profile.html", user = user,blogs=blogs)

@main.route('/user/<fname>/update/',methods = ['GET','POST'])
@login_required
def update_profile(fname):
    user = User.query.filter_by(firstname = fname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()
    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('main.profile',fname=user.firstname))

    return render_template('profile/update.html',form =form,user=user)

@main.route('/user/<fname>/update/pic',methods= ['POST'])
@login_required
def update_pic(fname):
    user = User.query.filter_by(firstname = fname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()

    return redirect(url_for('main.profile',fname=fname))


@main.route('/user/<fname>/post_blog',methods = ['GET','POST'])
def post_blog(fname):

    user = User.query.filter_by(firstname = fname).first()

    form = PostBlog()
    if form.validate_on_submit():
        title = form.title.data
        text = form.text.data
        category = form.category.data

        new_blog = Blog(title=title,text=text,category=category,user=current_user)

        db.session.add(new_blog)
        db.session.commit()
        subscribers=Subscribers.query.all()
        for subscriber in subscribers:
            mail_message('New Blog','email/new_blog',subscriber.email)
        return redirect(url_for('main.index'))

    return render_template("profile/post_blog.html", user = user,BlogForm=form)

@main.route('/user/<fname>/post_blog/picture/<int:id>',methods= ['POST'])
@login_required
def upload_picture(fname):
    blog = Blog.query.filter_by(id=id).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        blog.pic = path
        db.session.commit()

    return redirect(url_for('main.post_blog',fname=fname))

@main.route('/blog/<int:id>', methods = ['GET','POST'])
def blog(id):
    #getting comments for a pitch

    all_comments=Comment.query.filter_by(post_id=id).all()


    blog = Blog.query.filter_by(id=id).first()
    form = PostCommentForm()
    #from for comments
    if form.validate_on_submit():
        comment=form.comment.data

        new_comment=Comment(post_comment=comment,post_id=id) 
        db.session.add(new_comment)
        db.session.commit()     
        return redirect(url_for('main.blog', id=blog.id))

    return render_template('blog.html',blog=blog, comment_form=form,all_comments=all_comments)


@main.route('/subscribe',methods=["GET","POST"])
def subscribe():
    form = SubscribeForm()
    if form.validate_on_submit():

        new_subscriber = Subscribers(email=form.email.data)
        db.session.add(new_subscriber)
        db.session.commit() 
        subscribers = Subscribers.query.all()

        return redirect(url_for('main.index'))
    return render_template('subscribe.html',subscribe_form=form)


@main.route('/delete/<int:id>',methods=["GET","POST"])
def delete(id):
    deleted = Blog.query.filter_by(id=id).first()
    db.session.delete(deleted)
    db.session.commit()
    return redirect (url_for('main.index'))

@main.route('/commentDelete/<int:id>',methods=["GET","POST"])
@login_required
def delete_comment(id):

    deleted_comment = Comment.query.filter_by(id=id).first()
    db.session.delete(deleted_comment)
    db.session.commit()
    return redirect (url_for('main.index')) 