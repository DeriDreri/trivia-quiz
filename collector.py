import requests

def collector():
    difficulties = ['easy', 'medium', 'hard']
    baseURL = "https://opentdb.com/api.php?amount=15&difficulty="
    for dif in difficulties:
        workURL = baseURL+dif 
        for i in range (1, 31):
            file = requests.get(workURL)
            text = file.text
            finalText = text[29:-1]
            with open('offline/'+dif+'/dic'+(str)(i)+'.txt', 'w') as f:
                f.write(finalText)

collector()

            
    
   
