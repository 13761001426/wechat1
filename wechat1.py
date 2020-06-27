import itchat
import re

def filter_str(desstr, restr=''): #过滤掉中、英、数字以外的字符
    res = re.compile("[^\\u4e00-\\u9fa5^a-z^A-Z^0-9]")
    return res.sub(restr, desstr)

def sex_rename(sex):
    if sex == 1:
        return "男"
    elif sex == 2:
        return "女"
    else:
        return "未知"

itchat.auto_login()
friends = itchat.get_friends(update=True)[0:]
male = 0
female = 0
other = 0
for i in friends:
    sex = i["Sex"]
    if sex == 1:
        male += 1
    elif sex == 2:
        female += 1
    else:
        other += 1
total = len(friends)

print("微信共有好友{}人（包括自己）".format(len(friends)))
print("="*25)
print("男性：{}人,占{:.1f}%".format(male,100*male/total))
print("女性：{}人,占{:.1f}%".format(female,100*female/total))
print("未知：{}人,占{:.1f}%".format(other,100*other/total))
f1 = open("wx_list.csv","w")
head1 = ["昵称","备注名","性别","地区","市/区","签名"]
f1.write(",".join(head1)+"\n")
for j in friends:
    list1 = [filter_str(j["NickName"]),filter_str(j["RemarkName"]),sex_rename(j["Sex"]),j["Province"],j["City"],
             filter_str(j["Signature"]).replace("span","").replace("class","").replace("emoji","")]
    f1.write(",".join(list1)+"\n")
f1.close()