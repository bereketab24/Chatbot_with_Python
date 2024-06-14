#import a random module to being able to select random items from a sequences and shuffling sequences randomly. in this case, like the greeting and response list.
import random

# Define a dictionary of facilities and their locations
facilities = {
    "library": {
        "location": "Jan Moskov building, at the left corner of the campus",
        "description": "The library contains a vast collection of computers, books, journals, and other resources to support research and learning."
    },
    "laboratories": {
        "location": "At the right of the main gate",
        "description": "The laboratories are equipped with advanced equipment and technology to support research and experimentation."
    },
    "classes": {
        "location": "Ghion Building",
        "description": "The classes are held in various classrooms throughout the building."
    },
    "registration office": {
        "location": "At the front of the main gate",
        "description": "The registration offices are the central hub for student services,\n including admissions, registration, financial aid, and more. Find out more in our website www.bit.bdu.edu.et."
    }
}

# Define a dictionary of lecturers and their information
lecturers = {
    "Kelemework": {
        "department": "Computing",
        "office": "Korean Building , Room 101",
        "email": "Kelemework@bdu.edu.et",
        "bio": "He is a lecturer of Python programing language at BDU."
    },
    "Estifanos": {
        "department": "Electrical",
        "office": "Agri Building, Room 018",
        "email": "Estifanos@bdu.edu.et",
        "bio": "He is a lecturer of Electric circuit at BDU.\n He specialize in renewable energy. And has done several projects all over Ethiopia."
    },
    "Melkamu": {
        "department": "Mechanical",
        "office": "Agri Building, Room 011",
        "email": "Melkamu@bdu.edu.et",
        "bio": "He is a lecturer of workshop at BDU.\n He specializes in Electomechanical Engineering."
    }
}

# Define a list of greetings and responses
greetings = [
    "Hello! How can I assist you today?",
    "Greetings! How may I be of service?",
    "Welcome! What can I assist you with today?"
]

responses = [
    "I'm sorry, I don't understand. Could you please rephrase your question?",
    "I'm not sure what you're asking. Can you be more specific?",
    "I didn't catch that. Could you please try again?",
    "I'm sorry, I don't have that information. Is there something else I can help you with?",
    "I'm not programmed to answer that question. Can you please ask me something else?"
]


# Define a function to handle user input and return chatbot response
def chatbot_response(user_input):
    # Check if user is asking for a facility location
    for facility in facilities:
        if facility in user_input:
            info = facilities[facility]
            return f"The {facility} is located at {info['location']}. {info['description']}"

    # Check if user is asking for a lecturer information
    if "lecturer" in user_input.lower():
        options = "\n".join([f"{i + 1}. {lecturer}" for i, lecturer in enumerate(lecturers)])
        return f"Which lecturer would you like to learn more about? Please enter the name of lecturer you want:\n{options}"

    for lecturer in lecturers:
        if lecturer.lower() in user_input.lower():
            info = lecturers[lecturer]
            return f"{lecturer} is a lecturer in the {info['department']} department.\n His office is located at {info['office']}\n and you can contact him at {info['email']}.\n {info['bio']}"

    # If no facilities or lecturers were found, provide a random response
    return random.choice(responses)


# Define a main function to handle the chatbot conversation
def chat():
    greeting = random.choice(greetings)
    print(greeting)
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        else:
            response = chatbot_response(user_input)
            if greeting == response:
                print(random.choice(responses))
            else:
                print(response)

# Run the chatbot by calling the chat function
chat()