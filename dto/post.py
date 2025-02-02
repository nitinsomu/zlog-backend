class PostDTO:
    def __init__(self, title, summary, content, image, username):
        self.title = title
        self.summary = summary
        self.content = content
        self.image = image
        self.username = username

    def to_dict(self):
        return {
            "title": self.title,
            "summary": self.summary,
            "content": self.content,
            "image": self.image,
            "username": self.username
        }
