import random
asasas=["Sure.", 
        "Yeah." , 
        "Its funny you say that, because my third eldest actually told me about this. She was the first in the family to attend university. She is smart, I will give her that.", 
        "Sorry I didn't hear that, could you repeat that?",
        "What's the name of your company again?",
        "Yes yes yes, yes, yes.",
        "Someone called me last week, was that you?",
        "I just woke up from a nap, could you start over again?", 
        "Hold on, there is a bee on my arm. Keep talking.", 
        "Sorry, I had to feed my pet bear. What did you say?", 
        "Hold on, let me finish stealing this diamond first.",
        "I dropped the telephone, what did you say?"]
while True:
    a=raw_input("")
    b=random.randint(0, 8)
    print asasas[b]
    
    