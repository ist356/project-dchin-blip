# Reflection

Student Name:  name
Student Email:  email

## Instructions

Reflection is a key activity of learning. It helps you build a strong metacognition, or "understanding of your own learning." A good learner not only "knows what they know", but they "know what they don't know", too. Learning to reflect takes practice, but if your goal is to become a self-directed learner where you can teach yourself things, reflection is imperative.

- Now that you've completed the assignment, share your throughts. What did you learn? What confuses you? Where did you struggle? Where might you need more practice?
- A good reflection is: **specific as possible**,  **uses the terminology of the problem domain** (what was learned in class / through readings), and **is actionable** (you can pursue next steps, or be aided in the pursuit). That last part is what will make you a self-directed learner.
- Flex your recall muscles. You might have to review class notes / assigned readings to write your reflection and get the terminology correct.
- Your reflection is for **you**. Yes I make you write them and I read them, but you are merely practicing to become a better self-directed learner. If you read your reflection 1 week later, does what you wrote advance your learning?

Examples:

- **Poor Reflection:**  "I don't understand loops."   
**Better Reflection:** "I don't undersand how the while loop exits."   
**Best Reflection:** "I struggle writing the proper exit conditions on a while loop." It's actionable: You can practice this, google it, ask Chat GPT to explain it, etc. 
-  **Poor Reflection** "I learned loops."   
**Better Reflection** "I learned how to write while loops and their difference from for loops."   
**Best Reflection** "I learned when to use while vs for loops. While loops are for sentiel-controlled values (waiting for a condition to occur), vs for loops are for iterating over collections of fixed values."

`--- Reflection Below This Line ---`
I struggled with many things on this project:

- First, I ran into the issue of python not recognizing the "code" folder as a module despite the __init__ file being clearly visible. I was stuck on this for a while, looking for alternative ways of importing and changing my file structure. Ultimately, I had to go back to Assignment 6 and borrow the sys.path.append strategy in order to solve this problem.

- Secondly, I found out Playwright and Streamlit don't mix well together. The only solution I found was to use the async library (with help from the information in this post: https://discuss.streamlit.io/t/using-playwright-with-streamlit/28380/5).

- I found Streamlit a little finicky to work with. Since it reran the file constantly, I would have problems with button actions triggering without a button press (solved with an if statement) and the ui not coming out exactly how I wanted it to.

- The free tier of the Polygon.io API only allowed for a few calls per minute which made testing tough.

- The response from Polygon.io came in the form of a dictionary of dictionaries. Initially, I tried using json_normalize() but that did not work and I had to resort to going through the dictionaries manually via their keys.

I gained practical knowledge of how to use playwright, interact with an API, and make charts with streamlit. I also learned how to make use of pickle to save things from streamlit, which is important because I want to implement a note-taking feature in the future. Also in the future and if I had more time, I would try to make the project more resilient to errors (i.e. better error handling) and implement additional features like charts for the financial statement data and finer-grained metrics (e.g. earnings-per-share and sales-per-share) for individual days by combining the retrieval tools.