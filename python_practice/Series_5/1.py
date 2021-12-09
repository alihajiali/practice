import pandas as pd

# part 1 )

dic = {
'name':['ali','ahmad','hasan','javad'],
'physics':[20,19,18.5,19.75],
'math':[18,17.50,16,19]
}
df = pd.DataFrame(dic,index=['','','',''])
print(df)

df.to_csv('1.csv')

# یک فایل اکسل با فرمت سی اس وی در کنار فایل پایتونی در دایرکتوری جاری ایجاد میشود
# محتویات ان نام دانش اموزان و نمرات ریاضی و فیزیک انها میباشد


#-------------------------------------------------------------------

# part 2 )

df = pd.read_csv('1.csv')
lst = df.values
name_list = []
physics_list = []
math_list = []
average_list = []
for i in lst :
    name_list.append(i[1])
    physics_list.append(i[2])
    math_list.append(i[3])
    average_list.append((i[2]+i[3])/2)
print(name_list)
print(physics_list)
print(math_list)
print(average_list)

dic = {
'name':name_list,
'math':math_list,
'physics':physics_list,
'avrage' :average_list
}
df = pd.DataFrame(dic,index=['','','',''])
print(df)

df.to_csv('2.csv')

# فایل اکسل اول را میخوانیم و محتوای هر ستون را در یک لیست ذخیره میکنیم
# سپس فایل اکسل دوم را به گونه ای میسازیم که جای ستون دوم و سوم عوض شود
# و به عنوان ستون چهارم میانگین ستون دوم و سوم را به ان اضافه میکنیم



