#
#  ��ҵ������������ʽʵ�֣�
#       1��xxxxx
#       ��д���� ����������
#
#       ����д���test .....
#
#       2��xxxxx
#       ��д���� ����������
#
#       ����д���test .......
#

# 1��ʵ��һ�����������ж��ַ���str2�Ƿ���str1���Ӵ�������ǣ���ú�������str2��str1���״γ� �ֵĵ�ַ�����򣬷���None��

def find_sub(s1: str, s2: str):
    """
    ֱ��ʹ���ַ���������ʽ
    :param s1:
    :param s2:
    :return:
    """
    if not s1 or not s2:
        raise ValueError('input not allow empty string')
    try:
        i = s1.index(s2)
    except ValueError:
        return None
    return i

# test

find_sub('aa', 'aab')
find_sub('cc', 'eee')

# 2����������һ���б�����ҳ�xԪ���Ƿ����б����棬������ڷ���1�������ڷ���0

def is_in(x, lst=None):
    if lst is None:
        lst = []
    if x in lst:
        return 1
    return 0

# test

is_in('a', ['a', 'c', 'c'])
is_in('b', ['c', 'd'])