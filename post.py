
class RedditPost():

    # Initializer for a single reddit post class
    def __init__(self, input):
        self.title = input["title"]
        self.score = input["score"]
        self.url = input["permalink"]
        # Some posts do not contain thumbnails, so it is necessary to check for them
        if "thumbnail" in input.keys():
            self.thumbnail = input["thumbnail"]
        else:
            self.thumbnail = False
        if self.thumbnail == "self":
            full_text = input['selftext']
            if len(full_text) > 100:
                full_text = full_text[:100] + "..."
            self.text = full_text
        else:
            self.text = False
        if self.thumbnail == "self" or self.thumbnail == "default" or self.thumbnail == "nsfw":
            self.thumbnail = False

    def __str__(self):
        return str({
            "title": self.title,
            "score": self.score,
            "thumbnail": self.thumbnail
        })
