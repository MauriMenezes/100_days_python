# fruits = ['Apple', 'Pear', 'Orange']


# def make_pie(index):
#     try:
#         fruit = fruits[index]
#         print(fruit + " pie")
#     except IndexError:
#         print('fruit pie')


facebook_posts = [
    {'likes': 21, 'comments': 2},
    {'comments': 49, 'shares': 1},
    {'comments': 2, 'shares': 3},
    {'likes': 7, 'comments': 31},
    {'likes': 19, 'comments': 43}
]

total_likes = 0
for post in facebook_posts:
    try:
        total_likes += post['likes']
    except KeyError:
        pass
print(total_likes)
