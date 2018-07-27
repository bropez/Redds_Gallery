"""
A script that downloads local copies of pictures for the database
downloader downloads images from a given url

written by: Matthew Lopez
"""
import csv
import urllib.request
import db_edit


def downloader(image_url, image_name):
    """
    a method to download an image file from a given url
    :param image_url: the url that you'd like to download from
    :param image_name: the image name that is added to the image_url
    :return: none
    """
    urllib.request.urlretrieve(image_url, "pictures/" + image_name + ".jpg")


with open('out2.csv') as csvfile:
    content_reader = csv.reader(csvfile)
    for row in content_reader:
        if not row:
            pass
        else:
            current_name = row[1]
            new_name = row[1].lower()
            no_space_name = new_name.replace(" ", "")
            link = "pictures/" + no_space_name + ".jpg"
            db_edit.update(new_name, link, current_name)
            # downloader(row[0], name)