import matplotlib.pyplot as plt

def quiz_score_calc(quiz):
        score = 0
        #when was django launched: 2005
        if(quiz.question_0 == 2005):
                score += 1

        #whats the programming language most often used with django: Python
        if(quiz.question_1 == "Python"):
                score += 1

        #whats the file extension most often used to add style to an html file: css
        if(quiz.question_2 == "css"):
                score += 1

        #to display multiple elements inside a div we can use display: :flex
        if(quiz.question_3 == "flex"):
                score += 1

        return score

def build_graph_data(objects):
        data = {}
        for quiz in objects:
                data[quiz.name] = quiz_score_calc(quiz)

        print("data built")
        return data

def build_graph(objects):
        # creating the dataset
        data = build_graph_data(objects)
        users = list(data.keys())
        values = list(data.values())

        fig = plt.figure(figsize = (10, 5))

        # creating the bar plot
        plt.bar(users, values, color ='grey',
                width = 0.4)

        plt.xlabel("Courses offered")
        plt.ylabel("Score")
        plt.title("Users")
        plt.savefig('portfolio/static/portfolio/images/my_graph.png')

