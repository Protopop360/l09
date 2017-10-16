
def lucky_list(judge, victim, sherif, executioner):
	print(judge + "Удачи на казни")
	print(victim + "Удачи")
	print(sherif + "требую справедлвости и расстрела виновных")
	print(executioner + "Оправил на обучение Пасккалю")
lucky_list(judge = " Малик", sherif = " сулейман", executioner= " Эльдар", victim = " Света")




def freud(victim,is_sick = True):
	if is_sick == True:
		print("Фрейд, радостно потирая руки, достает сигару и тушит об " + victim)
	elif is_sick == False:
		print("Печаль Фериде Гаджихалиловна")
	else:
		print("Вы Фрейд")
freud("Эльдара")







print(1,3,4,5,6,7,89,9,9,0,0, sep = " больше ")
def reptiloid_list(*args, **kwargs):
	print("ОСтерегайтесь их!!:", args)
	print("Стрелять", kwargs)
reptiloid_list("Сулейман", "Султанмурад", "Дмитрий", "Саид", jid = "Эльдар")


получить список продуктов 
перебрать и приготовить рандомно
дать назавание блюду 
cook = ["зажарим", "сварить","освежевать"]
random.choice(cook)
