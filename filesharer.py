from filestack import Client

class FileSharer:

    def __init__(self, filepath, api_key='AViVqp7suSQWWEdrl6hf9z'):
        self.api_key = api_key
        self.filepath = filepath
    # Uploads File and outputs URL link
    def share(self):
        client = Client(self.api_key)
        new_filelink = client.upload(filepath=self.filepath)
        return new_filelink.url
