import csv
import os

def read_csv(path):
    f = open(path, encoding='utf-8-sig')
    content = []
    reader = csv.reader(f)
    for row in reader:
        content.append(row)
    f.close()
    return content


def recommend():
    recommend_list = dict()
    for row in questions:
        question_id = row[0]
        accuracy = float(row[1])
        # 正确率评估
        score = -abs(accuracy-user_accuracy)*100
        # 标签评估
        tags = row[2].split(" ")
        for tag in tags:
            score += user_tags.get(tag, 0)/len(tag_questions.get(tag))
        # 历史记录评估
        score += user_questions.get(question_id, 0)*len(questions)
        recommend_list[question_id] = score
    return sorted(recommend_list.items(), key=lambda a: a[1], reverse=True)


def write_user_data():
    f = open('user_data.csv', 'w', newline='', encoding='utf-8-sig')
    writer = csv.writer(f)
    writer.writerow([correct, count])
    writer.writerow(user_tags.keys())
    writer.writerow(user_tags.values())
    writer.writerow(user_questions.keys())
    writer.writerow(user_questions.values())
    f.close()
    print("User data has been recorded")
    return


questions = read_csv('GRE.csv')

tag_questions = {}  # 标签{标签名称：题目出现的次数}
question_tags = {}

for row in questions:
    tags = row[2].split(" ")
    for tag in tags:
        if tag not in tag_questions:
            tag_questions[tag] = [row[0]]
        else:
            tag_questions[tag].append(row[0])
        if row[0] not in question_tags:
            question_tags[row[0]] = [tag]
        else:
            question_tags[row[0]].append(tag)

# print(tag_questions)
# print(question_tags)


# init user_data
user_tags = {}  # 用户{易错标签：做错标签的次数}
user_accuracy = 1
user_questions = {}
correct = 0
count = 0
if not os.path.isfile('user_data.csv'):
    write_user_data()


# load user_data
user_data = read_csv('user_data.csv')
# print("stuff in user data", user_data)
user_accuracy = float(user_data[0][0])
user_tags = dict(zip(user_data[1], [int(i) for i in user_data[2]]))
# print("loaded user tags", user_tags)
user_questions = dict(zip(user_data[3], [int(i) for i in user_data[4]]))
# print("loaded user questions", user_questions)
correct = int(user_data[0][0])
count = int(user_data[0][1])
if count != 0:
    user_accuracy = correct/count
# print("loaded user correct, count: ", correct, count)
print("User data has been loaded")


while True:
    print(recommend())
    next_question = recommend()[0][0]
    print("Do task at http://gre.kmf.com/question/%s.html"%next_question)
    print("Input 'T' if correct, 'F' if not, input anything else to exit")
    i = input()
    last_question = next_question

    if i == 'T':
        bias = -1
        correct += 1
    elif i == 'F':
        bias = -1
        for tag in question_tags.get(last_question):
            if tag not in user_tags:
                user_tags[tag] = 1
            else:
                user_tags[tag] += 1
    else:
        write_user_data()
        break

    if last_question not in user_questions:
        user_questions[last_question] = bias
    else:
        user_questions[last_question] += bias
    count += 1
    user_accuracy = correct / count
    print("your accuracy is: ", user_accuracy)
