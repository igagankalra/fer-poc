#!usr/bin/env python

def save_output_into_flat_file(personGroupId, img_url, face_id, time):
    """Method to save output into flatfile.

    Arguments:
        personGroupId {String} -- This defines the client company{required for later use as we have to train using this}
        img_url {String} -- name of the file which is being uploaded{has to be changed by the client name when fully functional}
        face_id {String} -- faceId generated by the Cognative API
        time {String} -- Time stamp to save the time when ID was generated.
    """
    with open('output.txt', 'a') as f:
        f.write('{} \t {} \t {} \t {}\n'.format(personGroupId, img_url, face_id, time))
