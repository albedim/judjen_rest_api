from flask import jsonify
from flask_cors import CORS

from app.configuration.config import sql, app
from app.routers import user_notification, repost, favorite, storytag, friendrequest, tag, user, friend, story
from app.utils.utils import BASE_URL


app.register_blueprint(repost.repostRouter)
app.register_blueprint(user_notification.userNotificationRouter)
app.register_blueprint(favorite.favoriteRouter)
app.register_blueprint(friend.friendRouter)
app.register_blueprint(friendrequest.friendrequestRouter)
app.register_blueprint(tag.tagRouter)
app.register_blueprint(user.userRouter)
app.register_blueprint(story.storyRouter)
app.register_blueprint(storytag.storytagRouter)

CORS(app)


@app.route("/")
def read_root():
    return jsonify({'documentation': f"{BASE_URL}/docs"})


def create_app():
    with app.app_context():
        sql.create_all()
    return app


if __name__ == "__main__":
    create_app().run(host="192.168.1.8", port=8000)
