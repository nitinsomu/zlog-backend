class PostDTO:
    def __init__(self, title, summary, content, image):
        self.title = title
        self.summary = summary
        self.content = content
        self.image = image

    def to_dict(self):
        return {
            "title": self.title,
            "summary": self.summary,
            "content": self.content,
            "image": self.image
        }
