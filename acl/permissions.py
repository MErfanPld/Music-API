PERMISSIONS = []

MUSIC_PERMISSIONS = {
    'title': 'Music Permissions',
    'permissions': [
        {'name': 'List Music', 'code': 'music_list'},
        {'name': 'Create Music', 'code': 'music_create'},
        {'name': 'Edit Music', 'code': 'music_edit'},
        {'name': 'Delete Music', 'code': 'music_delete'},
        {'name': 'Detail Music', 'code': 'music_detail'},]
}
PERMISSIONS.append(MUSIC_PERMISSIONS)


ALBUM_PERMISSIONS = {
    'title': 'Album Permissions',
    'permissions': [
        {'name': 'List Album', 'code': 'album_list'},
        {'name': 'Create Album', 'code': 'album_create'},
        {'name': 'Edit Album', 'code': 'album_edit'},
        {'name': 'Delete Album', 'code': 'album_delete'},
        {'name': 'Detail Album', 'code': 'album_detail'},]
}
PERMISSIONS.append(ALBUM_PERMISSIONS)

class ROLE_CODES:
    USER = "user"
    SINGER = "singer"
