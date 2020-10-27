import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from api import GPT, Example, UIConfig
from api import demo_web_app


# Construct GPT object and show some examples
gpt = GPT(engine="davinci",
          temperature=0.5,
          max_tokens=100)

gpt.add_example(Example('Augmented reality app that helps you design your room', 
'One of the concerns while buying furniture or any interior decoration item is whether the product will suit your room and where would it look the best. An AR app helps you style your room by permitting you to use your camera and place 3D models of various items and furniture in the virtual space on your phone and see how it would look. The app can even partner with various shopping sites and facilitate user to order it directly from the app.'))


gpt.add_example(
    Example('Scan and convert to pdf app', 
    'Rather than going to a shop to get your documents to scan and then converting them into pdf. A scan and save it to pdf app can help you keep important records such as receipts, documents, report cards, notes, whiteboards etc., on your mobile securely. This app permits you to quickly scan your documents in high quality and store or send them as multipage PDF or JPEG files.'))

gpt.add_example(Example(
    'Health check-up and food planner app', 
    'This app checks your health day by day and suggests you proper meals that you should consume in order to remain healthy. It connects you to the numerous healthy-recipes that are provided by professional chef-bloggers. You can set your content to be provided as per your health situation, for e.g. if you are heart patient, you’ll be recommended recipes made of ingredients that are heart-healthy. The app can partner with groceries to deliver healthy items online directly from the app.'))

gpt.add_example(Example('Railway tracking app', 'Citizens of metropolitan cities are heavily dependent on trains to get to their destination. It can be incredibly disruptive if the trains are late and you have no way of knowing if you should wait or consider an alternative way of getting to your destination. A railway tracking app can give you the exact time of where the train is, so if you have an emergency and the train is late you can take a bus or a taxi.'))

gpt.add_example(Example('Language learning app', 
    'The language learning app that helps users with some beginner lessons on different languages in one of the most brilliant app ideas for 2020. The app can have different levels of difficulty with the first level being alphabets and basic letters to the advanced level containing full-fledged conversations. The app can enable voice so the learners know how words are pronounced.'))

gpt.add_example(Example('Voice translation app', 
    'One of the primary concern of travelling abroad is not knowing the language of the country and the struggle of trying to communicate with the natives. An app that can translate your voice will be a revolutionary way to communicate for travellers. The words can be spoken to the phone which will be translated to their desired language. The app must also work both ways where other languages can be translated to your language in real-time.'))

gpt.add_example(Example('Bike servicing app', 
    'A door-step bike servicing platform and application which will use technology for the convenience of two-wheeler owners by providing them a transparent connection with high-quality vehicle maintenance providers. The platform can provide assisted door-step pick-up and drop, an in-built inventory management system that enables reduction of waiting-time, smarter stock allocation, an order management system etc.'))

gpt.add_example(Example('Call recording app', 
    'There are many victims today suffering from harassment, prank calling and phishing. They can download this app and if there is a spam call harassing the user, they can use the app to record the call so that it can be shown as evidence later.'))

gpt.add_example(Example('Scan to shop apps',
    'These type of app will let you scan the items that you find desirable and find them or their closest substitute on online shops so that you can buy them instantly.'))

gpt.add_example(Example('Mall navigation map',
    'A digital mall navigation map stores the digital map of all the shopping malls in the area and can be used to navigate the mall as well as directions leading up to it. It is particularly helpful for larger malls where with the help of the app the user can find the exact store or even status of the restaurant, parking spot or crowdedness of the mall.'))                        

gpt.add_example(Example('Criminal alert app', 
    'Seeing a missing person or a wanted criminals’ face once on the television is difficult to remember. Plus, there is also a chance of meeting a stranger who turns out to be a criminal that you don’t know about. An application idea is such that the app will alert you of criminals in your area- so that you can save a life as well as help in catching a lawbreaker.'))


gpt.add_example(Example('Fitness App', 
    'A healthy lifestyle web application targeting health conscious people to track their habits assisted by registered nutritionists, pathologists and health coaches in order to ultimately lower the risk of lifestyle disorders. The application would be equipped with several charts that help the user manage their overall health- like weight, sugar, heart rate, blood pressure etc. User is also equipped with individual meal charts, lifestyle plans, nutrition plans as per their condition. It will also be integrated with chat facility that allows users to talk with the community as well as health professionals.'))

gpt.add_example(Example('Tip Calculator app', 
    'The tip calculator app has features that allow fast bill entry for those dining out with friends or family and have to split the bill. You can calculate the exact percentage of tipping amount from your total bill on the spot and get good service each time you want service from the institution.'))

gpt.add_example(Example('Real-time car sharing app', 
    'A real-time car sharing app allows the user to enlist their car and put in the destination as to where they are going. Another user on the app who is going the same way can put in their destination and find the users with cars who are going in the same direction. In the end they can split costs.'))

gpt.add_example(
    Example('Food recommendation app', 
    'A food recommendation/ review app shows suggestions from people who like to explore different restaurants and can be trusted to put out reviews and recommendations of what people can try when they visit so and so eating place.'))

gpt.add_example(
    Example('Parking space finder app', 'This app can help people find an available parking spot in a specific location. The app can make use of GPS, webcams, location and real-time parking data in order to find user a free parking space as soon as they want.'))

gpt.add_example(Example('Graphical restaurant table reservation', 
    'You need privacy in a corner seat for a special date or need the central table for making a great announcement. But in restaurants it’s difficult to get the exact seating arrangement for what you’ve planned. With a graphical restaurant reservation app, you can choose the desired seats or table and book them for a specific time.'))

gpt.add_example(Example('Virtual study group app', 
    'Students can meet up on a common forum and prepare for their exams along with other students that are studying for the same subject matter.  The app can provide them with study material, tools, discussion helps, guides etc.'))

gpt.add_example(Example('Language learning app',
    'More and more people are learning new things for broader life experiences and to enhance their skill-set. You can take advantage by creating an app that can help users learn the A, B, C, Ds of new languages and then progress as per their knowledge level. This new app idea in 2020 can even facilitate audio features for users to learn the correct pronunciation of words.'))

gpt.add_example(Example('Karaoke app',
    'Everyone has a pop star fantasy, even if they are not much of a singer. With a karaoke app, the user can sing and use filters to sound like their singing idols. Plus, amateur singers can also practice on the app.'))

# Define UI configuration
config = UIConfig(description="App Idea Generation App",
                  button_text="Generate",
                  placeholder="An App for...")

demo_web_app(gpt, config)
