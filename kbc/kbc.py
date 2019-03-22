print("*************************************************************************************************")
print("welcometo my KBC game")
print("**************************************************************************************************")
money =[1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,640000,1250000,2500000,5000000,10000000]
#function to print the money
def win_money(correct_answer):
		print(money[correct_answer-1])
		if money[correct_answer-1]==10000:
			print("Congrats!you completed first level.")
		elif money[correct_answer-1]==320000:
			print("Congrats! you completed second level.")
		elif money[correct_answer-1]==10000000:
			print("Congrats!!!!!you win 1 croer rupyee.")


def start():
		#Questions which is going to ask
		question=[
					  "who is the first person to reach mount everest?",
					  "who is the first person to reach north pole?",
					  "who is the first person to reach south pole?",
					  "which is the religion of the world?",
					  "which is the first country to print book?",
					  "which is the first country to issue paper currency?",
					  "which is the first country to commence competitive examination in civil services?",
					  "who is the first president of the U.S.A?",
					  "who is the first prime minister of Britain?",
					  "who is the Governor General of the United Nations?",
					  "The author of Business @ speed of Thought is?",
					  "who among the following is the author of the book india Remembered?"
					  "who among the following wrote the poem subh-e-Azadi?",
					  "who wrote Devdas?",
					  "who said 'Man is a political animal ?",

				  ]
		# Options for questions are?
		first_option=[	
						"Shepra Tensing,Edmund Hillary","Robert Peary",
					  	"Amundsen","Hinduism",
					  	"china","china",
					  	"china","George Washington","George Washington",
					  	"Trigveli(Norway)","Dick Fransis",
					  	"jk Rowling","Sahir Ludhiyavi",
					  	"bibbutibhushan Bandopadhyay","Socrates",
					  	

					 ]
		second_option=[	
						"Rajesh sharma","Rahesh sharma",
					   	"Rajesh sharma","Muslim",
					   	"India","India",
					   	"India","Robert Walpole","Robert walpole",
					   	"Robert Walpole","john Gray","Robert Dallek",
					   	"Faiz Ahmed Faiz","saratchandra chattopadhyay","plato",
					  

					  ]
		third_option=[	
						"charles hillary","charles hillary",
					  	"charles hillary","sikh",
					  	"USA","USA",
					  	"USA","Henry Waterloo","Henry Waterloo",
					  	"Henry Waterloo","Bill Gates","Pamela Mountbatten",
					  	"Muhammad Iqbal","Kalidasa","Dante",
					  	
					  ]
		fourth_option=[	
						"Johan don","Johan don",
						"Johan don","Christian",
						"UK","UK",
						"UK", "George Bush", "George Bush","George Bush",
						"David Baldexi","Stephen HawKING",
						"Maulana abul kalam", "surdas",
						"Aristotle",

					  ] 
		all_option=[
					first_option,second_option,
					third_option,fourth_option
					]
		#iterate till you don't get wrong answer
		wrong_answer=False
		#counting to know on which level the user 
		correct_answer=0
		#List for keeping record of answers of above question
		ans_key=[0,0,0,0,0,0,0,0,1,0,2,2,1,1,3,2]

		#Game start
		while(wrong_answer!=True):
			#variable used for question from list
			stage=0
			
			#prints the question from the list
			print("Q."+question[stage])

			#print options
			for Number,option in enumerate(all_option):
				print (str(Number+1)+". "+option[stage])
			#Take input of the user
			answer=int(input("Please ,tell your answer "))

			key = (ans_key[stage]+1)
			#check ,the answer is correct or not
			if  key == answer:
				print("Congrats!your  answer is right: Rs", end="")
				correct_answer+=1
				win_money(correct_answer)
			else:
				print("Sadly...your answer is wrong")
				correct_answer=0
				wrong_answer=True
			#check it is the last level or not
			if(correct_answer==15):
				break
			stage+=1
start()