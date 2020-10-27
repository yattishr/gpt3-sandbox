import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from api import GPT, Example, UIConfig
from api import demo_web_app


# Construct GPT object and show some examples
gpt = GPT(engine="davinci",
          temperature=0.7,
          max_tokens=100)

gpt.add_example(Example('aneamia', 
'Feel tired or lightheaded (sometimes with fainting) Weakness Fatigue easily Have decreased energy Appear pale Develop palpitations or rapid heart rate Experience shortness of breath'))

gpt.add_example(
    Example('cold/flu', 
    'Headaches, body aches, fever, and flu-like symptoms Nasal congestion, runny nose, and sneezing Cough Sore throat'))

gpt.add_example(Example(
    'asthama', 
    'shortness of breath, chest pain,cough'))

gpt.add_example(Example('alzheimers', 'loss of orientation (to person, place, or time), agitation, irritability, quarrelsomeness, and a diminishing ability to care for him- or herself and to dress appropriately.'))

gpt.add_example(Example('pregnancy', 
    'absence of menstrual periods  breast swelling and tenderness. Food cravings'))

gpt.add_example(Example('hyperthyroid', 
    'a rapid heart rate, excessive sweating, intolerance to heat, tremor, nervousness, or agitation. Other symptoms can include fatigue, weight loss, hair loss, increased appetite, problems with concentration, frequent bowel movements, and irregular or decreased menstrual blood flow in women'))

gpt.add_example(Example('hypothyroid', 
    'fatigue, depression, mild weight gain, cold intolerance, sleepiness, constipation dry and coarse hair, dry skin, and muscle cramps. Blood cholesterol levels may be elevated.'))

gpt.add_example(Example('diabetes', 
    'dehydration, hunger, increased urination, and increased thirst.'))

gpt.add_example(Example('HIV AIDS',
    'fever, swollen lymph nodes, joint and muscle aches, and sore throat. chills, night sweats, and mouth ulcers. '))

gpt.add_example(Example('high blood pressure',
    'dizziness, shortness of breath, headache, and blurred vision  nosebleeds, blood in the urine, fatigue, chest pain, '))                        

gpt.add_example(Example('Rheumatoid Arthritis', 
    'aches stiffness, muscle aches, low-grade fever, fatigue, lack of appetite, loss of energy . Joints can become warm, swollen, reddened, painful,'))


gpt.add_example(Example('hepatitis B', 
    'fatigue, loss of appetite, nausea, jaundice (yellowing of the skin and eyes), and pain in the upper right abdomen (due to the inflamed liver).'))

gpt.add_example(Example('Dengue', 
    'headache, fever, exhaustion, severe muscle joint pain, swollen lymph nodes rash, fever, itchy rash,headache'))

gpt.add_example(Example('Malaria', 
    'fever and chills, headaches, nausea and vomiting, and general weakness and body aches'))

gpt.add_example(
    Example('Chicken Pox', 
    'general weakness, fever up to 102 F, and red spots that start on the same day or so as the fever'))

gpt.add_example(
    Example('jaundice', 'Yellow discoloration of the skin, mucous membranes and the whites of the eyes Light-colored skin Poor feeding Lethargy/excessive sleepiness Changes in muscle tone (either listless or stiff with arching of the back) High-pitched crying Seizures'))

gpt.add_example(Example('Diarrhea', 
    'bowel movements are frequent watery. no signs of inflammation. cramping abdominal pain'))

gpt.add_example(Example('cataract', 
    'decrease in clarity of vision, not fully correctable with glasses. loss of contrast sensitivity. Disturbing glare in light'))

gpt.add_example(Example('pneumonia',
    'fever, chills, cough, shortness of breath, and fatigue.'))

gpt.add_example(Example('Urinary Retention',
    'inability to urinate painful, urgent need to urinate pain or discomfort in the lower abdomen bloating of the lower abdomen'))

# Define UI configuration
config = UIConfig(description="Medical Condition and it's Symtoms",
                  button_text="List Symptoms",
                  placeholder="Enter medical condition here...")

demo_web_app(gpt, config)
