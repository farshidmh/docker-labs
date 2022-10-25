import transformers
from transformers import Pipeline
from transformers import pipeline
import time
from pprint import pprint

print ("Loading hugingface qa pipeline...")
t1 = time.perf_counter()
qapipe = pipeline("question-answering")
# qapipe = pipeline('question-answering',
#                    model='distilbert-base-uncased-distilled-squad', 
#                    tokenizer='bert-base-uncased')
t2 = time.perf_counter()
print ("Loaded huggingface  in {:,.1f} milli seconds".format ((t2-t1)*1e3))
print()

def ask_question (passage, question):
    t1 = time.perf_counter()
    answer = qapipe({ 'question': question, 'context': passage })
    t2 = time.perf_counter()
    print ('question: ', question)
    print ("answered in {:,.1f} milli seconds".format ((t2-t1)*1e3))
    pprint (answer)
    print ('--------------')

passage = """The Matrix is a 1999 science fiction action film written and directed by The Wachowskis, starring Keanu Reeves, Laurence Fishburne, Carrie-Anne Moss, Hugo Weaving, and Joe Pantoliano."""
question="Who stars in The Matrix?"
ask_question(passage, question)


## -------------------------------

passage = """
Polar bears live throughout the Arctic, in areas where they can hunt seals in wide cracks in the sea ice or at breathing holes. The taxonomic name for polar bears is Ursus maritimus, which means sea bear, a fitting name for these champion swimmers. They have been known to swim more than 60 miles (about 100 kilometers) without rest in search of food, using their broad front feet for paddling and their back legs like rudders to steer. Unfortunately, due to loss of ice, the bears are now having to swim longer distances, as much as a few hundred miles, which takes a toll on their energy and fat storage.

Despite the long, harsh winter, polar bears don’t hibernate. In fact, most of them (except pregnant females) continue to hunt seals throughout the winter. When the weather is extremely cold and hunting is impossible, bears may seek temporary shelter in show dens until conditions improve.

Polar bears can grow up to 5.3 feet (1.6 meters) at the shoulder

Females weigh 330 to 650 pounds (150 to 294 kilograms); males weigh 700 to 1,200 pounds (317 to 544 kilograms)
"""
question = "where does polar bear live?"
ask_question(passage, question)

question = "how much does a polar bear weigh?"
ask_question(passage, question)

question = "What do polar bears eat?"
ask_question(passage, question)

## -------------------------------

passage = """
Lightning is a powerful electrical discharge made during a thunderstorm. The electric current is very hot and causes the air around it to expand very quickly, which in turn makes thunder. Sometimes it happens between clouds. Sometimes (in the rain) it goes from cloud to ground. If it goes from cloud to ground, it can strike a person. Around 2000 people are struck by lightning each year. About 50 to 100 lightning bolts strike the Earth every second. Lightning has hit the Empire State Building as many as 500 times a year.
"""

question = "what is lightning?"
ask_question(passage, question)
question = "How many lightning bolts strike earth"
ask_question(passage, question)

## -------------------------------