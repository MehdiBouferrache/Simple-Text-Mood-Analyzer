from textblob import TextBlob
from time import sleep

def get_choice():
    choice= int(input(
            "1.Do you want a feeling analysis ?\n2.Do you want to quit?\n "
            "(select the number corresponding your choice)\n\n"
            ))
    return choice


def measure_subjectivity(subjectivity):
    if subjectivity < 0.4:
        print(
            "Your statement is very objective. it does not imply any remarkable "\
              "feelings and can not be analyzed "
              )
        exit()

def measure_polarity(polarity):
    if polarity>0:
        print("Your sentence is positive !")
    else:
        print("Your sentence is negative.")

def custom_print(func):
    def wrapper(*args,**kwargs):
        text= func(*args,**kwargs)
        for character in text:
            print(character,end='', flush=True)
            sleep(0.05)
    return wrapper

# if character==".":end='\n' else : end=''

@custom_print
def give_advice(polarity):
    if polarity>0:
        
        advice =    '''You have a lot of positive energy
Keep it up by doing the activity that keeps you feel happy and hopingly
healthy both mentally and physically. 
Do not forget to thank Allah in your happy moments too.\n'''
        
    else:

        advice=    '''You look overwhelmed
1-Remember that Allah is with you.
2-Take a deep breath.
3-Try to recall or find the reason of your sad feelings.
4-Unless the reason (activity,person...) that makes you feel bad is helping you grow,
then try to avoid it completely.
5-You can do an activity that makes you feel happry and relaxed
such as reading Quran, practicing sports...\n'''
        
    return advice
        
a_choice=get_choice()

while a_choice==1:
    user_input=input("Express your feelings so they can be analyzed:\n")
    TextBlob_user_input= TextBlob(user_input)
    polarity,subjectivity=TextBlob_user_input.sentiment
    print(type(polarity))
    measure_subjectivity(subjectivity)
    measure_polarity(polarity)
    give_advice(polarity)
    a_choice=get_choice()


else: 
    if a_choice==2:
        exit()
    else:
        print("Unavailable choice")
        a_choice=get_choice()
