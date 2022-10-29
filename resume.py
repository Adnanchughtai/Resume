import streamlit as st
from PIL import Image

with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

#####################
# Header 
st.write('''
# **Muhammad Adnan**, M.Sc.
##### *Curriculum Vitae* 
''')

image = Image.open('dp1.png')
st.image(image, width=230)

st.markdown('## Summary', unsafe_allow_html=True)
st.info('''
- A master's graduate in the field of molecular entomology, with vast experience in mosquito culturing and maintenance, and molecular characterization of newly identified
    viruses from field-collected mosquitoes. My long-term objective is to be a valuable member of the medical entomology community and aid in the eradication of the
    deadliest vector-borne illnesses. I am looking for a Ph.D. opportunity in order to deepen my knowledge in this specific area. 
- I have broad experience in programming and machine learning tools.
''')

#####################
# Navigation

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #6120e3;">
  <a class="navbar-brand" href="" target="_blank">Muhammad Adnan</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="/">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#education">Education</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#Work Experience">Work Experience</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#Trainings">Trainings</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#Publications & Conferences">Publications</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#Honors & Awards">Honors & Awards</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#Digital & Programming skills">Digital & Programming skills</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#Languages & Social Media">Languages & Social Media</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

#####################
# Custom function for printing text
def txt(a, b):
  col1, col2 = st.columns([4,1])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

def txt2(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)

def txt3(a, b):
  col1, col2 = st.columns([1,2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)
  
def txt4(a, b, c):
  col1, col2, col3 = st.columns([1.5,2,2])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)
  with col3:
    st.markdown(c)

#####################
st.markdown('''
## Education
''')

txt('**Research Student** (Insect Virology), *Kyushu University*, Japan',
'2020-2022')
st.markdown('''
- My initial interest in joining this lab was to expand my skill set to include a molecular approach to entomological studies. I was however captivated by the laboratories interest
    in the molecular mechanisms of arbovirus diseases. I was fascinated by the studies that aimed at understanding interactions between the arthropod vector and arboviruses or
    insect-specific viruses at the genomic level. The expression of this interest led to being assigned to a project that was aimed at determining the genomic factors relevant to the
    replication of viruses using 3 negeviruses as model organisms because of its unique replication strategy. The aim of the project I was working on was to determine the
    process by which the sub-genomic RNA of Negeviruses was synthesized. This project enabled me to master a variety of techniques such as;
    - **Molecular Virology**
        - Negevirus propagation and harvesting
        - Viral RNA extraction
        - Plaque assay for virus quantification
    - **Molecular Biology**
        - Cell culture maintenance: C6/36 & mammalian cell lines
        - Polymerase chain reaction (PCR)
        - RT-PCR
        - RACE method
        - Nested PCR
        - Gene expression (Luciferase & GFP)
        - Sample preparation for sequencing
        - Silkworm culture maintenance for baculovirus gene expression system
            Baculovirus injection into silkworm larvae for recombinant protein expression
        - Plasmid amplification & bacterial culture

- Research Topic ` Identification, analysis and molecular characterization of insect specific viruses from the field collected mosquitoes`.
- Received MEXT & JICA Scholarship.
''')

txt('**Masters of Science** (Tropical Medicine (**Medical Entomology**), *Mahidol University International College*, Thailand',
'2017-2020')
st.markdown('''
- GPA: `3.25`
- Graduated with First Class Honors.
- Thesis: `Comparison of effective dose with deterrence time for three botanicals oils by using Multi-Chamber-Blood-Feeding system against Aedes aegypti`.
- **Major subjects**: Advanced Medical Entomology, Practical Entomology, Molecular Entomology, Immunology, Parasitology, Protozoology, Helminthology, Molecular Cellular
    Biology, Biostatistics, virology, bacteriology, etc.
- **Master's Research Project**: Tests on repellents were typically performed on well-shaven animals, such as rabbits, dogs, guinea pigs, chicks, and sheep, in place of human subjects.
    However, the use of these alternates is limited by animal rights concerns as well as concerns about their comparativeness to the human system. In this study, we developed
    an improved novel test system for evaluating the efficacy of mosquito repellents. This multi-chamber-blood-feeding method was designed to require relatively fewer test
    mosquitoes, with a reduced risk of repellent-cross-contamination. Three botanical oils, Citronella, Lemon eucalyptus, and Lavender, were used in assessing the practicability of
    this novel system, with absolute ethanol as the negative control. Mosquito nets were treated with varying concentrations of botanical oils and their efficacy in repelling
    mosquitoes was determined. Citronella was observed to be the most effective botanical oil in repelling mosquitoes, with an effective dose (ED ) of 13.48% and a deterrent time
    of 240 minutes. The results of this study highlight the efficiency of this novel system in testing the efficacy of mosquito repellents and insecticides as well as screening for
    insecticide resistance in a mosquito population.
    - **Medical Entomology skills**
        - Field mosquito sampling
        - Maintenance of mosquito colonies (Aedes aegypti, Ae. albopictus, Culex pipiens,
            Anopheles minimums, Anopheles dirus).
        - Identification of mosquito species.
        - Intrathoracic injection of virus for vector competence assessments
        - Artificial membrane feeding through (Hemotek membrane system)
        - Analysis of the ovary for parous and nulliparous status
        - Microscopic examination
        - Repellent bioassay testing
        - Insecticide testing bioassay

''')

txt('**Bachelor of Science** (B.Sc. (Hons) Agriculture **Entomology**), *Gomal University International College*, Pakistan',
'2012-2016')
st.markdown('''
- GPA: `4.00`
- Graduated with First Class Honors.
- Thesis: `Effect of prey density on the biology and functional response of Crysoperla carnea`.
- **Major subjects**: Insect morphology, Insect behavior, Insect physiology, Insect anatomy, Insect pest crops, beneficial insects, integrated pest management, forest entomology,
    Insect immunology, etc.
- **Bachelor's Research Project**: The effect of prey density on biology and functional response of green lacewing, *Crysoperla carnea* (Stephens) (Neuroptera: Chrysopidae) was studied in
    the laboratory of the Entomology Section of the Agricultural Research Institute, Dera Ismail Khan, at 25±1 ºC, 65±5% RH and 10:14 light: dark regime. Newly emerged larvae of
    *C. carnea* were fed 20, 30, 40, 50, 60, 70, 80, 90, and 100 fresh eggs of *Sitotroga cerealell* (Lepidoptera: Gelechiidae) in a small plastic bottle. It was observed that the prey density
    had a significant effect on the positive consumption rate, development, and fecundity of *C. carnea*. The daily predation rate of C. carnea increased slowly during the first two
    instars and reached its peak in the third larval instar. Although *C. carnea* completed its development at all prey densities, the increase in prey densities reduced developmental
    time and mortality. Lacewing larvae provided with an overabundance of *S. cerealella* eggs developed faster than the larvae provided with fewer eggs. Lacewings fed during the
    larval stage with 20 eggs/day showed the lowest fecundity with the increase in prey density. A lower intrinsic rate of increase was because the population fed at a low prey
    density had prolonged developmental time, a higher mortality rate in immature stages, as well as a low daily rate of progeny.
''')

#####################
st.markdown('''
## Work Experience
''')

txt('**B.Sc Internship**, Department of Entomology, Agriculture Research Institute, Pakistan',
'3 Months (2016)')
st.markdown('''
- I worked on a project titled “Biological parameters and functional attributes of *Crysoperla carnea* (Stephen) on artificial and natural diets." Through this project, we aimed to confirm
    whether artificial food (Honey and yeast mixture) is good for rearing over natural food (*Sitotroga cerealella* eggs). for release into the cotton field for other harmful insect control
    (Biological control).
''')

txt('**Internship**, Japan Space System (JSS), Japan',
'15 days (2022)')
st.markdown('''
- Attended this internship had two major purposes: first, to receive certificate credit. Second, I discovered how space technology would be helpful in tracking (GPS) in the field
    of vector-borne illnesses to identify endemic regions.
''')

#####################
st.markdown('''
## Trainings 
''')

txt('**Mosquito Competency Training**, Department of Medical Entomology (Mahidol University), Thailand',
'3 days (2019)')
st.markdown('''
- In this session, professors taught us the technique to check mosquito competency by injecting the virus into the intra-thoracic microinjection and seeing the survival and viral
    dissemination rate in the mosquito body.
- **Learning skills**: mosquito culture, DENV-2 propagation, plaque assay, microinjection needle use, and mosquito survival record.
''')

txt('**Modern Morphometric Training Course**, Department of Medical Entomology (Mahidol University), Thailand',
'1 Week (2019)')
st.markdown('''
- This training was organized by the Department of Medical Entomology in order to teach the students the importance of mosquito wing mapping to differentiate among different
    species.
- **Learning skills**: Mosquito sampling for microscopic examination; wing capturing for digitizing; analysis software.
''')

txt('**Biosafety and Biosecurity Training Course**, Department of Medical Sciences (Mahidol University), Thailand',
'3 days (2019)')
st.markdown('''
- The main objective of this training was to provide the participants with the knowledge and skills to handle biological materials safely and to prevent the spread of infectious.
''')

txt('**Effective Presentation technique (English Version)**, Department of Medical Entomology (Mahidol University), Thailand',
'2 days (2019)')
st.markdown('''
- This session was organized in order to trained the students about the main tool box in power point and body languages during delivering presentation.
''')

#####################
st.markdown('''
## Publications 
''')

txt('Effect of prey density the biology and functional response of Crysoperla carnea', '2017',)
st.markdown('''
[Link](https://www.entomoljournal.com/archives/2017/vol5issue1/PartM/5-1-67-294.pdf) 
''')
txt('Impact of full vs deficit irrigations on various phenological stages of wheat','2018',)
st.markdown('''
[Link](https://innspub.net/impact-of-full-vs-deficit-irrigations-on-various-phenological-stages-of-wheat/)
''')
txt('Evaluation of effective dose with protection time of DEET by using multi-chamber-bloodfeeding system against *Aedes aegypti*', '2020',) 
st.markdown('''
[Link](https://rsucon.rsu.ac.th/proceeding/article/2413)
''')
txt('Comparison of effective dose with deterrence time of three essential oils by using multichamber blood feeding system (MCBF) against', '*Aedes aegypti*,') 
st.markdown('''
- **Processing**
''')

#####################
st.markdown('''
## Conferences 
''')

txt('RSU International Research Conference (RSU 2020) Rangsit University - Bangkok - Thailand', '17/05/2020')
st.markdown('''
- **Oral Presentation**
''')
txt('Joint International Tropical Medicine Meeting (JITMM) International conference (Montien Hotel Surawong) - Bangkok - Thailand', '17/11/2019 - 20/11/2019')
st.markdown('''
- **Attended**
''')


#####################
st.markdown('''
## Honors & Awards
''')

txt('Research Student Scholarship (**MEXT+JICA**) Japan – Kyushu University, Japan', '2020-2022')
txt('Dr Sylvia Meek (**Malaria consortium**) FTM Scholarship for Masters in Medical Entomology, at Mahidol University, Bankgok, Thailand', '2017-2020')
txt('**1st Position In Entomology Department**, Gomal University, Pakistan', '2016')
txt('Three talents awards (**Jamaat Islam and Faculty Annual function**)', 'Gomal University') 
txt('**Recieved laptop** from (Prime Minister of Pakistan) on achieving 1st postion in the whole department', 'Gomal University')           


#####################
st.markdown('''
## Communication & Interpersonal Skills  
''')

st.markdown('''
- **Transferable skills**: Communication, Teamwork, Leadership, Problem Solving, Time Management, Adaptability, & Scientific integrity.
- **Scientific communication**: Oral presentation, Poster presentation, & Writing scientific papers.
- **Collborative skills**: Worked in a team of 4 members in the bachelors and masters projects.
''')



#####################
st.markdown('''
## Digital Skilla
''')
st.markdown('''
- **Ms Office**: Word, Excel, Power Point, & Access.
- **SPSS**: Statistical Package for Social Sciences.
''')


######################
st.markdown('''
## Programming Skills
''')
st.markdown('''
- **Python**: Pandas, Numpy, Matplotlib, Seaborn, Scikit-learn, Streamlit, & Plotly.
- **Github**: Version control system.
- **Markdown**: Markup language.
- **Data structure**: List, Tuple, Dictionary, & Set, Data visualization, Data Wrangling, Data analysis, & Data cleaning.
- **Machine learning**: Supervised learning, Unsupervised learning, & Reinforcement learning.
- **Computer vision**: Image processing, Image classification, & Object detection.
''')

######################
st.markdown('''
## Languages
''')
txt('English', 'Fluent')
txt('Urdu', 'Native')
     

#####################
st.markdown('''
## Social Media
''')
txt2('LinkedIn', 'https://www.linkedin.com/in/muhammad-adnan-36204a12a/')
txt2('Twitter', 'https://twitter.com/Adnanaadi93')
txt2('ResearchGate', 'https://www.researchgate.net/profile/Muhammad-Adnan-29')
txt2('GitHub', 'https://github.com/Adnanchughtai')
txt2('Kaggle', 'https://www.kaggle.com/aadi94')
txt2('Facebook', 'https://www.facebook.com/adnan.aadi.9279')

