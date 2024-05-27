import graphene
from graphene_django import DjangoObjectType
from datetime import timedelta
from .models import *



class Output(graphene.ObjectType):
    """
    Custom ErrorType to hold error messages.
    You can define fields here to represent different components of your error messages.
    """
    success = graphene.Boolean()    
    error = graphene.String()

class CommentList(DjangoObjectType):

    class Meta:
        model = Comment
        fields = '__all__'


class LikeList(DjangoObjectType):

    class Meta:
        model = Like
        fields = '__all__'


class PostList(DjangoObjectType):
    comment_set = graphene.List(CommentList)

    class Meta:
        model = Post
        fields = '__all__'

    def resolve_comment_set(self, info):
            return Comment.objects.filter(post=self.id)


class BaseQuery(graphene.ObjectType):
    posts = graphene.List(PostList)
    likes = graphene.List(LikeList)
    comments = graphene.List(CommentList)
    post = graphene.List(PostList, id=graphene.Int())


    def resolve_likes(self, info):
        return Like.objects.all()

    def resolve_posts(self, info):
        return Post.objects.all()

    def resolve_post(self, info, id):
        return Post.objects.filter(id=id)


class CreatePost(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        description = graphene.String(required=True)
        publish_date = graphene.String()
        author = graphene.String()

    success = graphene.Boolean()
    error = graphene.Boolean()

    @classmethod
    def mutate(cls, root, info, title, description, publish_date=None, author=""):
        try:
            post = Post(title=title, description=description, author=author, publish_date=publish_date)
            post.save()
            return cls(success=True)
        except Exception as e:
            return cls(success=False, error=True)


class UpdatePost(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        title = graphene.String(required=True)
        description = graphene.String(required=True)
        publish_date = graphene.String()
        author = graphene.String()

    success = graphene.Boolean()
    error = graphene.Boolean()

    @classmethod
    def mutate(cls, root, info, id, title, description, publish_date=None, author=None):
        try:
            post = Post.objects.filter(id=id).first()
            if post:
                setattr(post, 'title', title)
                setattr(post, 'description', description)
                setattr(post, 'publish_date', publish_date) if publish_date else None
                setattr(post, 'author', author) if author else None
                post.save()
                return cls(success=True, error=False)
            return cls(error=True, success=False)
        except Exception as e:
            return cls(success=False, error=True)


class CreateLike(graphene.Mutation, Output):
    class Arguments:
        post = graphene.Int(required=True)
        author = graphene.String()
    
    likes = graphene.List(LikeList)

    @classmethod
    def mutate(cls, root, info,  post, author=""):
        try:
            post = Post.objects.filter(id=post).first()
            if post:
                like = Like(post=post, author=author)
                like.save()
                likes = Like.objects.all()
                return CreateLike(success=True, error={}, likes=likes)
            else:
                likes = Like.objects.all()
                return CreateLike(success=True, error={},likes=likes)
        except Exception as e:
            return CreateLike(success=False, error={},likes=[])


class CreateComment(graphene.Mutation):
    class Arguments:
        text = graphene.String(required=True)
        post = graphene.Int(required=True)
        author = graphene.String()

    success = graphene.Boolean()
    error = graphene.Boolean()

    @classmethod
    def mutate(cls, root, info, text, post, author=""):
        try:
            post = Post.objects.filter(id=post).first()
            if post:
                comment = Comment(text=text, post=post, author=author)
                comment.save()
                return cls(success=True)
            else:
                return cls(error=True, success=False)
        except Exception as e:
            return cls(success=False, error=True)


class BaseMutation(graphene.ObjectType):
    create_post = CreatePost.Field()
    update_post = UpdatePost.Field()
    create_comment = CreateComment.Field()
    create_like = CreateLike.Field()


schema = graphene.Schema(query=BaseQuery, mutation=BaseMutation)