# rept = {"python" : "питон",
#         "anaconda" : "анаконда",
#         "tortoize" : "черепаха"}
#
# rept["snake"] = "змея"
# rept["tortoise"] = rept.pop("tortoize")
# for key in rept:
#  print(rept[key] + " по-английски будет " + key)



# cnt = ["Andorra", "Belarus", "Denmark",
#        "Kenya", "Jamaica", "Romania"]
# fh = [1.0, 6.0, 1.5, 4.0, 2.5, 2.0]
#
# cnt_fn = dict(zip(cnt, fh))
# for i in cnt_fn.items():
#   print(i)
# print(cnt_fn)


# slovar={}
# pairs = [(2, 4), (4, 6), (0, 1), (5, 2), (9, 1), (3, 8)]
# numbers = [num for num, _ in pairs]
# numbers2 = [num for _, num in pairs]
# for i in range(len(pairs)):
#         slovar[pairs[i]]=numbers[i]*numbers2[i]
# print(slovar)


# grades = {'Anna': 4, 'Bob': 3, 'Claire': 5, 'Dick': 2, 'Elena': 5,
#          'Fred': 5, 'George': 4, 'Kristina': 3, 'Nick': 2,
#          'Ursula': 4, 'Viktor': 5}
# excel = []
# good = []
# satisf = []
# bad = []
#
# for key, value in grades.items():
#     print(key,value)
#     if value == 5:
#         excel.append(key)
#     elif value == 4:
#         good.append(key)
#     elif value == 3:
#         satisf.append(key)
#     else:
#         bad.append(key)
#
# print(excel)
# print(good)
# print(satisf)
# print(bad)