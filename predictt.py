import pickle
import streamlit as st
from streamlit_option_menu import option_menu


with open('hd.pkl','rb') as file:
  clf=pickle.load(file)
with open('dbts.pkl','rb') as file:
  clf1=pickle.load(file)  
 
with st.sidebar:
    selected = option_menu('Proactive Health Gaurd',

                           ['Welcome','Autism','Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinsons Prediction','Dengue','Malaria','Review'],
                           
                          
                           default_index=0)


if selected=='Welcome':
    st.image("logo1.png")
    st.title(":red[Health Care Analyzer and Disease Predictor]")
    st.write(":blue[ProActive Health Guard is a revolutionary healthcare initiative employing machine learning, Streamlit, bots, and Python libraries for proactive disease prediction. The project's diverse machine learning algorithms analyze comprehensive health datasets, predicting conditions from malaria to mental health issues. Streamlit facilitates a user-friendly interface, enriched by interactive bots, fostering engagement. With a focus on early detection and personalized insights, ProActive Health Guard aims to transform healthcare paradigms, reduce system burden, and empower individuals to manage their well-being effectively. This pioneering project exemplifies the synergy of technology and healthcare, leading towards a future of personalized, preventive, and improved healthcare outcomes.]")
if selected == 'Diabetes Prediction':

  
    st.title('Diabetes Prediction using ML')
    st.write(":blue[Diabetes mellitus refers to a group of diseases that affect how the body uses blood sugar (glucose). Glucose is an important source of energy for the cells that make up the muscles and tissues. It's also the brain's main source of fuel.]")



    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')

    with col2:
        Glucose = st.text_input('Glucose Level')

    with col3:
        BloodPressure = st.text_input('Blood Pressure value')

    with col1:
        SkinThickness = st.text_input('Skin Thickness value')

    with col2:
        Insulin = st.text_input('Insulin Level')

    with col3:
        BMI = st.text_input('BMI value')

    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')

    with col2:
        Age = st.text_input('Age of the Person')



    diab_diagnosis = ''

    

    if st.button('Diabetes Test Result'):

        user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,
                      BMI, DiabetesPedigreeFunction, Age]

        user_input = [float(x) for x in user_input]

        prediction = clf1.predict([user_input])

        if prediction == 1:
            diab_diagnosis = 'The person is diabetic'
        else:
            diab_diagnosis = 'The person is not diabetic'

    st.success(diab_diagnosis)    
    

if selected == 'Heart Disease Prediction':

    # page title
    st.title('Heart Disease Prediction using ML')
    st.write(":blue[There are many types of heart disease, and each one has its own symptoms and treatment. For some, lifestyle changes and medicine can make a huge difference in improving your health. For others, you may need surgery to make your ticker work well again.]")
    st.image("heart1.jpeg")

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')

    with col2:
        sex = st.text_input('Sex')

    with col3:
        cp = st.text_input('Chest Pain types')

    with col1:
        trestbps = st.text_input('Resting Blood Pressure')

    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')

    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')

    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')

    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')

    with col3:
        exang = st.text_input('Exercise Induced Angina')

    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')

    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')

    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')

    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')

  
    heart_diagnosis = ''

   

    if st.button('Heart Disease Test Result'):

        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]

        user_input = [float(x) for x in user_input]

       
        prediction= clf.predict([user_input])

        if prediction == 1:
            heart_diagnosis = 'The person is having heart disease'
        else:
            heart_diagnosis = 'The person does not have any heart disease'

    st.success(heart_diagnosis)
if selected == 'Review':    
    st.title(":red[Review section]")
    st.write(":blue[Thank you for trying our app ,your every feedback matters]")
    st.text_area("Write your suggestions")
    st.write(":blue[how was your experience on a scale of 1 to 10.]")
    st.slider("",0,10)
