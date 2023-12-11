import wikipedia
import random
from time import time

# getting topics info
def getting_topics():
    print("plzz wait while we getting the topic......\n")
    try:
        wikipedia.set_lang("en")
        topics = ["Hydrogen evolution reaction","Hydroxyethylrutoside"]
        topic = random.choice(topics) 
        topic_result = (wikipedia.summary(topic,sentences = 1))
        print(f"{topic_result}\n")
        return topic_result
    except:
        error = print("Cheak your internet connection")
        return error,None
    
# main function
def main():
    topic_result = getting_topics()
    input("press enter to start")
    print("Type here\n")       
    time_start = time()
    userInput = str(input())
    time_end = time()

    # Calculat mistakes
    miss = 0
    loop_num = 0
    for item in topic_result:
        try:
            if topic_result[loop_num] == userInput[loop_num]:
                loop_num +=1
            else:
                miss +=1    
                loop_num +=1
        except :
            miss +=1
    
    # Calculat time and speed
    time_round = round(time_end - time_start, 2)
    speedC = round(len(userInput) / time_round, 2)
    speed = round(len(topic_result) / time_round, 2)
    print(f"correct speed = {speedC} WPA\nAverage speed = {speed} WPA\nMistakes = {miss}")

if __name__== "__main__":
    main()