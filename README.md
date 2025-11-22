# Career-Advisor-
## Overview - Choosing a career is one of the biggest decisions a student has to make, yet it often feels confusing and overwhelming. Many students are unsure about what they are good at or which path matches their abilities. A Career Recommendation System Based on Academic Strengths helps make this process simpler and more meaningful by using a student’s subject-wise performance to offer suitable career suggestions.
The idea is easy to understand. Every student has unique talents, and these naturally show up in their academic results. Some students may find math and problem-solving easy, while others may do better in science, languages, social sciences, or creative subjects. These strengths can give a clear indication of the types of careers where a student is likely to perform well and feel satisfied. Instead of choosing a career based on pressure, trends, or guesswork, students can rely on a more logical and helpful method.
In this system, the student’s marks or grades are taken as input. The program looks at the subjects where the student performs best and matches these strengths with related career fields. For instance, strong scores in math and programming may point toward engineering or computer science, while high performance in language and communication may suggest careers such as journalism, law, teaching, or public relations.
By offering suggestions that align with a student’s natural strengths, the system helps them make clearer, more confident, and well-informed career choices. It acts as a simple yet powerful tool that supports students in planning a future that suits their abilities and interests.


Here's the comprehensive documentation in bullet points:

## **Problem Statement**
- Students lack clear guidance connecting academic performance with career choices
- No automated system to analyze subject strengths and suggest relevant career paths
- Manual career counseling is time-consuming, expensive, and inaccessible to many
- Need for instant, data-driven career recommendations based on academic strengths
- Absence of visual tools to represent academic performance and career mapping

## **Objectives**
- Develop an automated career recommendation system based on academic performance
- Provide instant career guidance without human intervention
- Visualize academic strengths through charts and graphs
- Create an accessible tool for students to explore career options
- Bridge the gap between academic performance and career choices

## **Functional Requirements**
- Accept user input for marks in 5 predefined subjects (Math, Science, English, History, Programming)
- Validate input marks to ensure they are between 0-100
- Calculate and identify the strongest subject using maximum marks
- Map strongest subject to relevant career options
- Classify performance into categories (Excellent/Good/Average/Needs Improvement)
- Generate visual representations using bar charts and pie charts
- Display career recommendations with simulated salary data

## **Non-functional Requirements**
- **Performance**: Process and display results within 2-3 seconds
- **Usability**: Simple, intuitive interface requiring no technical knowledge
- **Reliability**: 100% uptime for desktop application with error-free execution
- **Maintainability**: Clean, modular code structure for easy modifications
- **Portability**: Cross-platform compatibility (Windows, macOS, Linux)
- **Accuracy**: Correct career mapping and performance classification

## **System Architecture Diagram**
```
User Input → Data Processing → Analysis Engine → Output Generation
    ↓              ↓               ↓               ↓
 Marks Entry   NumPy Arrays   Career Mapping   Console Output
                             Performance Calc   Charts Display
```

## **Process Flow or Workflow Diagram**
1. **Start Application** → 2. **Input Marks for 5 Subjects** → 3. **Validate Input** → 4. **Process Data with NumPy** → 5. **Identify Strongest Subject** → 6. **Generate Career Recommendations** → 7. **Classify Performance** → 8. **Create Visualizations** → 9. **Display Results** → 10. **End**

## **UML Diagrams**

**○ Use Case Diagram**
- **Actor**: Student/User
- **Use Cases**:
  - Enter academic marks
  - View career recommendations
  - See performance analysis
  - View visual charts
  - Get subject-wise classification

**○ Class Diagram / Component Diagram**
```
Main Program
├── Data Input Handler
├── Analysis Engine
│   ├── Performance Calculator
│   ├── Career Mapper
│   └── Classification Engine
├── Visualization Generator
└── Output Formatter
```

**○ Sequence Diagram**
```
User → System: Input marks
System → NumPy: Process marks array
NumPy → System: Return strongest subject index
System → Career Map: Get careers for subject
Career Map → System: Return career list
System → Matplotlib: Generate charts
Matplotlib → System: Return chart objects
System → User: Display results and charts
```

## **Database/Storage Design (if applicable)**
- **No database implementation** in current version
- **In-memory data storage** using Python lists and dictionaries
- **Future ER Diagram Concept**:
  - Students (StudentID, Name, Grade)
  - Subjects (SubjectID, SubjectName)
  - Marks (MarkID, StudentID, SubjectID, Marks)
  - Careers (CareerID, CareerName, SubjectID, Description)

## **Dataset Description** (Computation/ML Context)
- **Dataset Type**: Synthetic user-generated data
- **Features**: Marks in 5 subjects (numerical, 0-100 scale)
- **Size**: Single user instance (real-time input)
- **Labels**: Career categories mapped to subject domains
- **Data Structure**: Structured numerical data with categorical mappings

## **Model Selection Rationale**
- **NumPy argmax()**: Selected for simplicity and efficiency in finding maximum values
- **Rule-based Classification**: Chosen over ML for transparent, interpretable results
- **Linear Processing**: Appropriate for straightforward calculations without complex patterns
- **Rationale**: Problem doesn't require predictive modeling; deterministic rules suffice for career mapping based on clear subject-performance relationships

## **Evaluation Methodology**
- **Functional Testing**: Verify correct strongest subject identification
- **Input Validation Testing**: Test boundary values (0, 100) and invalid inputs
- **Career Mapping Accuracy**: Ensure correct subject-career correlations
- **Visualization Testing**: Verify chart generation and data representation
- **User Acceptance Testing**: Gather feedback on interface usability and recommendation relevance
- **Performance Testing**: Measure response time for complete workflow execution

## Features -
1.	Career Recommendations - Suggests jobs based on strongest subject
2 .Performance Analysis - Finds your best subject automatically
3.Data Visualization - Shows marks as bar chart and pie chart
4.Simple Input - Easy marks entry for 5 subjects
5.Performance Categories - Groups marks into excellence levels
6.Clean Output - Organized career suggestions and charts


## Technologies/Tools Used:
1.Python 3.x
2.NumPy (for data analysis)
3.Matplotlib (for visualization)
4.Random (for career salaries)

## Steps to Install & Run:
1.Install Python from python.org
2.Install required libraries:
3.Bash
4.pip install numpy matplotlib
5.Save the code as career_advisor.py

## Run the program:
1.	Open python career_advisor.py
2.Enter marks when prompted (0-100)
3.View results and charts



## Instructions for Testing:
1.	Test with high marks (90+) to see "Excellent" category
2.	Test with low marks (<60) to see "Needs Improvement"
3.	Try equal marks to verify strongest subject selection
4.	Check that charts display correctly
5.	Verify career recommendations match the strongest subject
6.	Test with boundary values (0, 100, 60, 75, 90)
