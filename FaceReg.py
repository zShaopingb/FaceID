from aip import AipFace

APP_ID = '10449289'
API_KEY = 'gtvBGSXQ7lY1fjX0XGB9s8sE'
SECRET_KEY = 'u1R4vFMfTkpPoHtMGEr1eclu0i3vvrkp'

client = AipFace(APP_ID, API_KEY, SECRET_KEY)


def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


result = client.addUser(
    'zhujh',
    'user info',
    'group1',
    get_file_content('face.jpg')
)

print(result)