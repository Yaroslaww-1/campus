import os

from django.core.files.storage import default_storage


class AwsS3Service:
    @staticmethod
    def upload_replace_file(id, prevUrl, file):
        AWS_BUCKET_NAME = os.getenv('AWS_BUCKET_NAME')
        AWS_REGION_NAME = os.getenv('AWS_REGION_NAME')
        if prevUrl is not None:
            path = prevUrl.replace(
                "https://s3-{0}.amazonaws.com/{1}/".format(AWS_REGION_NAME, AWS_BUCKET_NAME), "")
            default_storage.delete(path)
        filepath = default_storage.save("media/" + id + "/" + file.name, file)
        fileUrl = "https://s3-{0}.amazonaws.com/{1}/{2}".format(
            AWS_REGION_NAME,
            AWS_BUCKET_NAME,
            filepath
        )
        return fileUrl
