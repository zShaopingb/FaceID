from aip import AipFace

""" 
    字段	    必选	类型	说明
    log_id	    是	    number	请求唯一标识码，随机数
    result_num	是	    number	返回结果数目，即：result数组中元素个数
    result	    是	    array	结果数组，数组元素为匹配得分，top n。 得分范围[0,100.0]。推荐得分超过80可认为认证成功
    ext_info	否	    array	对应参数中的ext_fields
    +faceliveness	否	string	活体分数，如0.49999。
                             单帧活体检测参考阈值0.834963，超过此分值以上则可认为是活体。
                             活体检测接口主要用于判断是否为二次翻拍，需要限制用户为当场拍照获取图片；
                             推荐配合客户端SDK有动作校验活体使用 
"""
APP_ID = '10449289'
API_KEY = 'gtvBGSXQ7lY1fjX0XGB9s8sE'
SECRET_KEY = 'u1R4vFMfTkpPoHtMGEr1eclu0i3vvrkp'

client = AipFace(APP_ID, API_KEY, SECRET_KEY)


def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

name = 'zhub'
result = client.verifyUser(
    name,
    'group1',
    get_file_content('tmp.jpg'),
)
if('error_code' in result):
    print('error')
else:
    print('success')