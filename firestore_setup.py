import datetime
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

speakers = [{'twitter': 'IBMResearch',
  'biography': "Dr. Aisha Walcott-Bryant is a research scientist and manager of the AI Science and Engineering team at IBM Research, Africa. She is passionate about healthcare, interactive systems, and on addressing Africa's diverse challenges.In addition, Dr. Walcott-Bryant leads a team of researchers and engineers who are working on transformational innovations in global health and development while advancing the state of the art in AI, Blockchain, and other technologies.She and her team are engaged in projects in Maternal Newborn Child Health (MNCH), Family Planning (FP), disease intervention planning, and water access and management. Her team's recent healthcare work on “Enabling Care Continuity Using a Digital Health Wallet” was awarded Honorable Mention at the International Conference on Health Informatics, ICHI2019.Prior to her career at IBM Research Africa, Dr. Walcott-Bryant worked in Spain. There, she took on projects in the area of Smarter Cities at Barcelona Digital and Telefonica with a focus on physical systems for social media engagement, and multi-modal trip planning and recommending. Dr. Walcott-Bryant earned her PhD in Electrical Engineering and Computer Science at MIT where she conducted research on mobile robot navigation in dynamic environments at their Computer Science and Artificial Intelligence Lab (CSAIL).",
  'name': 'Dr. Aisha Walcott-Bryant',
  'workplace': 'IBM Research Africa, Nairobi',
  'jobtitle': 'Research Scientist',
  'image': 'https://iclr.cc/virtual_2020/static/images/aisha.jpg',
  'category': 12},
 {'biography': 'Leslie Pack Kaelbling is the Panasonic Professor of Computer Science and Engineering at the Computer Science and Artificial Intelligence Laboratory (CSAIL) at the Massachusetts Institute of Technology. She has made research contributions to decision-making under uncertainty, learning, and sensing with applications to robotics, with a particular focus on reinforcement learning and planning in partially observable domains. She holds an A.B in Philosophy and a Ph.D. in Computer Science from Stanford University, and has had research positions at SRI International and Teleos Research and a faculty position at Brown University. She is the recipient of the US National Science Foundation Presidential Faculty Fellowship, the IJCAI Computers and Thought Award, and several teaching prizes; she has been elected a fellow of the AAAI. She was the founder and editor-in-chief of the Journal of Machine Learning Research.',
  'workplace': 'MIT',
  'jobtitle': 'Professor of Computer Science',
  'image': 'https://iclr.cc/virtual_2020/static/images/Kaelbling-1.jpg',
  'name': 'Prof. Leslie Kaelbling',
  'category': 3,
  'twitter': 'MIT_CSAIL'},
 {'twitter': 'ruha9',
  'biography': 'Dr. Ruha Benjamin is Associate Professor of African American Studies at Princeton University, founder of the JUST DATA Lab, and author of People’s Science: Bodies and Rights on the Stem Cell Frontier (2013) and Race After Technology: Abolitionist Tools for the New Jim Code (2019) among other publications. Her work investigates the social dimensions of science, medicine, and technology with a focus on the relationship between innovation and inequity, health and justice, knowledge and power. Professor Benjamin is the recipient of numerous awards and fellowships including from the American Council of Learned Societies, National Science Foundation, Institute for Advanced Study, and the President’s Award for Distinguished Teaching at Princeton. For more info visit www.ruhabenjamin.com',
  'workplace': 'Princeton',
  'name': 'Prof. Ruha Benjamin',
  'jobtitle': 'Associate Professor',
  'image': 'https://pbs.twimg.com/profile_images/1332482148138430467/Om60Zf5h_400x400.jpg',
  'category': 7},
 {'twitter': 'laurent_dinh',
  'biography': "Laurent Dinh is a research scientist at Google Brain Montréal. His research focus has been on deep generative models, probabilistic modeling, and generalization in deep learning. He's best known for his contribution in normalizing flows generative models, such as NICE and Real NVP, and in generalization in deep learning.He obtained his PhD in deep learning at Mila, under the supervision of Yoshua Bengio, during which he visited Google Brain and DeepMind. Before that, he graduated from École Centrale Paris in Applied Mathematics and from École Normale Supérieure de Cachan in machine learning and computer vision.",
  'name': 'Dr. Laurent Dinh',
  'workplace': 'Google AI',
  'jobtitle': 'Research Scientist',
  'image': 'https://iclr.cc/virtual_2020/static/images/laurent.jpg',
  'category': 14},
 {'twitter': 'MihaelaVDS',
  'biography': "Professor van der Schaar is John Humphrey Plummer Professor of Machine Learning, Artificial Intelligence and Medicine at the University of Cambridge and a Turing Faculty Fellow at The Alan Turing Institute in London, where she leads the effort on data science and machine learning for personalized medicine. She is also a Chancellor's Professor at UCLA. She was elected IEEE Fellow in 2009. She has received numerous awards, including the Oon Prize on Preventative Medicine from the University of Cambridge (2018), an NSF Career Award (2004), 3 IBM Faculty Awards, the IBM Exploratory Stream Analytics Innovation Award, the Philips Make a Difference Award and several best paper awards, including the IEEE Darlington Award. She holds 35 granted USA patents. In 2019, she was identified by National Endowment for Science, Technology and the Arts as the female researcher based in the UK with the most publications in the field of AI. She was also elected as a 2019 'Star in Computer Networking and Communications'. Her research expertise spans signal and image processing, communication networks, network science, multimedia, game theory, distributed systems and machine learning. Her current research focus is on machine learning, AI and operations research for healthcare and medicine. For more details, see her website: http://www.vanderschaar-lab.com",
  'workplace': 'University of Cambridge',
  'name': 'Prof. Mihaela van der Schaar',
  'jobtitle': 'Professor of Machine Learning',
  'image': 'https://iclr.cc/virtual_2020/static/images/Mihaela_photo_new.jpg',
  'category': 11},
 {'biography': 'Devi Parikh is a Research Scientist at Facebook AI Research (FAIR) and an Associate Professor in the School of Interactive Computing at Georgia Tech. Her research interests are in computer vision, natural language processing, embodied AI, human-AI collaboration, and AI for creativity. She is a recipient of an IJCAI Computers and Thought award, a Sloan Research Fellowship, an NSF CAREER award, Young Investigator awards from the Office of Naval Research and Army Research Office, an Allen Distinguished Investigator Award in Artificial Intelligence, outstanding young faculty awards at Georgia Tech and Virginia Tech, a Rowan University Medal of Excellence for Alumni Achievement, a Forbes’ list of 20 “Incredible Women Advancing A.I. Research” recognition, and a Marr Best Paper Prize awarded at the International Conference on Computer Vision.',
  'workplace': 'Georgia Tech and Facebook AI Research',
  'jobtitle': 'Research Scientist',
  'name': 'Prof. Devi Parikh',
  'image': 'https://iclr.cc/virtual_2020/static/images/devi.png',
  'category': 1,
  'twitter': 'deviparikh'},
 {'twitter': 'ylecun',
  'biography': 'Yann LeCun is VP and Chief AI Scientist at Facebook and Silver Professor at NYU affiliated with the Courant Institute and the Center for Data Science. He was the founding Director of Facebook AI Research and of the NYU Center for Data Science. He received an EE Diploma from ESIEE (Paris) in 1983, a PhD in Computer Science from Université Pierre et Marie Curie (Paris) in 1987. After a postdoc at the University of Toronto, he joined AT&T Bell Laboratories. He became head of the Image Processing Research Department at AT&T Labs-Research in 1996, and joined NYU in 2003 after a short tenure at the NEC Research Institute. In late 2013, LeCun became Director of AI Research at Facebook, while remaining on the NYU Faculty part-time. He was visiting professor at Collège de France in 2016. His research interests include machine learning and artificial intelligence, with applications to computer vision, natural language understanding, robotics, and computational neuroscience. He is best known for his work in deep learning and the invention of the convolutional network method which is widely used for image, video and speech recognition. He is a member of the US National Academy of Engineering, a Chevalier de la Légion d’Honneur, a fellow of AAAI, the recipient of the 2014 IEEE Neural Network Pioneer Award, the 2015 IEEE Pattern Analysis and Machine Intelligence Distinguished Researcher Award, the 2016 Lovie Award for Lifetime Achievement, the University of Pennsylvania Pender Award, and honorary doctorates from IPN, Mexico and EPFL. He is the recipient of the 2018 ACM Turing Award (with Geoffrey Hinton and Yoshua Bengio) for “conceptual and engineering breakthroughs that have made deep neural networks a critical component of computing.”',
  'workplace': ' Facebook AI',
  'name': 'Prof. Yann LeCun',
  'jobtitle': 'Chief AI Scientist',
  'image': 'https://pbs.twimg.com/profile_images/2387565623/7gew8nz1z7ik1ch148so_400x400.jpeg',
  'category': 10},
 {'twitter': 'goodfellow_ian',
  'biography': 'Yoshua Bengio is recognized as one of the world’s artificial intelligence leaders and a pioneer of deep learning. Professor since 1993 at the Université de Montréal, he received the A.M. Turing Award 2018, considered like the Nobel prize for computing, with Geoff Hinton and Yann LeCun. Holder of the Canada Research Chair in Statistical Learning Algorithms, he is also the founder and scientific director of Mila, the Quebec Institute of AI–the world’s biggest university-based research group in deep learning. In 2018, he collected the largest number of new citations in the world for a computer scientist and earned the prestigious Killam Prize from the Canada Council for the Arts. Concerned about the social impact of AI, he actively contributed to the Montreal Declaration for the Responsible Development of Artificial Intelligence.',
  'workplace': 'NYU / MILA',
  'name': 'Prof. Yoshua Bengio',
  'jobtitle': 'Professor',
  'image': 'https://pbs.twimg.com/media/EmzlbupXYAgJfw9?format=jpg&name=medium',
  'category': 15},
 {'biography': 'Michael I. Jordan is the Pehong Chen Distinguished Professor in the Department of Electrical Engineering and Computer Science and the Department of Statistics at the University of California, Berkeley. His research interests bridge the computational, statistical, cognitive and biological sciences. Professor Jordan is a member of the National Academy of Sciences and a member of the National Academy of Engineering. He has been named a Neyman Lecturer and a Medallion Lecturer by the Institute of Mathematical Statistics. He received the IJCAI Research Excellence Award in 2016, the David E. Rumelhart Prize in 2015 and the ACM/AAAI Allen Newell Award in 2009.',
  'workplace': 'University of California, Berkeley',
  'jobtitle': 'Distinguished Professor',
  'name': 'Prof. Michael I. Jordan',
  'image': 'https://iclr.cc/virtual_2020/static/images/jordan.jpg',
  'category': 2,
  'twitter': 'IEEESpectrum'},
 {'twitter': 'drakearch',
  'biography': "Lead Data Scientist in Quest Media & Supplies, Inc. M.Sc. in computer science by the San Pablo's catholic university",
  'name': 'Drake Arch',
  'workplace': 'Quest Media & Supplies, Inc.',
  'jobtitle': 'Lead Data Scientist',
  'image': 'https://pbs.twimg.com/profile_images/1391075676095143942/UgFfBqm__400x400.jpg',
  'category': 4}]

conferences = [{'description': 'Artificial Intelligence (AI) has for some time stoked the creative fires of computer scientists and researchers world-wide -- even before the so-called AI winter. After emerging from the winter, with much improved compute, vast amounts of data, and new techniques, AI has ignited our collective imaginations. We have been captivated by its promise while wary of its possible misuse in applications. AI has certainly demonstrated its enormous potential especially in fields such as healthcare. There, it has been used to support radiologists and to further precision medicine; conversely it has been used to generate photorealistic videos which distort our concept of what is real. Hence, we must thoughtfully harness AI to address the myriad of scientific and societal challenges; and open pathways to opportunities in governance, policy, and management. In this talk, I will share innovative solutions which leverage AI for global health with a focus on Africa. I will present a vision for the collaborations in hopes to inspire our community to join on this journey to transform Africa and impact the world.',
  'title': 'AI + Africa = Global Innovation',
  'topic': 'AI Innovation',
  'datetime': datetime.datetime(2021, 12, 6, 14, 0),
  'speaker': 'Dr. Aisha Walcott-Bryant'},
 {'description': "We, as robot engineers, have to think hard about our role in the design of robots and how it interacts with learning, both in 'the factory' (that is, at engineering time) and in 'the wild' (that is, when the robot is delivered to a customer). I will share some general thoughts about the strategies for robot design and then talk in detail about some work I have been involved in, both in the design of an overall architecture for an intelligent robot and in strategies for learning to integrate new skills into the repertoire of an already competent robot.",
  'title': 'Doing for Our Robots What Nature Did For Us',
  'topic': 'Robotics',
  'datetime': datetime.datetime(2021, 12, 6, 19, 0),
  'speaker': 'Prof. Leslie Kaelbling'},
 {'description': 'From everyday apps to complex algorithms, technology has the potential to hide, speed, and even deepen discrimination, while appearing neutral and even benevolent when compared to racist practices of a previous era. In this talk, I explore a range of discriminatory designs that encode inequity: by explicitly amplifying racial hierarchies, by ignoring but thereby replicating social divisions, or by aiming to fix racial bias but ultimately doing quite the opposite. This presentation takes us into the world of biased bots, altruistic algorithms, and their many entanglements, and provides conceptual tools to decode tech promises with sociologically informed skepticism. In doing so, it challenges us to question not only the technologies we are sold, but also the ones we manufacture ourselves.',
  'title': '2021 Vision: Reimagining the Default Settings of Technology & Society',
  'topic': 'Computer Vision',
  'datetime': datetime.datetime(2021, 12, 7, 14, 0),
  'speaker': 'Prof. Ruha Benjamin'},
 {'title': 'Invertible Models and Normalizing Flows',
  'description': 'Normalizing flows provide a tool to build an expressive and tractable family of probability distributions. In the last few years, research in this field has successfully harnessed some of the latest advances in deep learning to design flexible invertible models. Recently, these methods have seen wider adoption in the machine learning community for applications such as probabilistic inference, density estimation, and classification. In this talk, I will reflect on the recent progress made by the community on using, expanding, and repurposing this toolset, and describe my perspective on challenges and opportunities in this direction.',
  'topic': 'Deep Learning',
  'datetime': datetime.datetime(2021, 12, 7, 16, 0),
  'speaker': 'Dr. Laurent Dinh'},
 {'description': 'Medicine stands apart from other areas where machine learning can be applied. While we have seen advances in other fields with lots of data, it is not the volume of data that makes medicine so hard, it is the challenges arising from extracting actionable information from the complexity of the data. It is these challenges that make medicine the most exciting area for anyone who is really interested in the frontiers of machine learning – giving us real-world problems where the solutions are ones that are societally important and which potentially impact on us all. Think Covid 19! In this talk I will show how machine learning is transforming medicine and how medicine is driving new advances in machine learning, including new methodologies in automated machine learning, interpretable and explainable machine learning, dynamic forecasting, and causal inference.',
  'title': 'Machine Learning: Changing the future of healthcare',
  'topic': 'Machine Learning',
  'datetime': datetime.datetime(2021, 12, 8, 19, 0),
  'speaker': 'Prof. Mihaela van der Schaar'},
 {'description': "I will talk about AI systems at the intersection of computer vision and natural language processing. I will give an overview of why problems at the intersection of vision and language are exciting, what capabilities today's AI systems have, and what challenges remain.",
  'title': 'AI Systems That Can See And Talk',
  'topic': 'AI Systems',
  'datetime': datetime.datetime(2021, 12, 8, 21, 0),
  'speaker': 'Prof. Devi Parikh'},
 {'description': 'Humans and animals learn enormous amount of background knowledge about the world in the early months of life with little supervision and almost no interactions. How can we reproduce this learning paradigm in machines? One proposal for doing so is Self-Supervised Learning (SSL) in which a system is trained to predict a part of the input from the rest of the input. SSL, in the form of denoising auto-encoder, has been astonishingly successful for learning task-independent representations of text. But the success has not been translated to images and videos. The main obstacle is how to represent uncertainty in high-dimensional continuous spaces in which probability densities are generally intractable. We propose to use Energy-Based Models (EBM) to represent data manifolds or level-sets of distributions on the variables to be predicted. There are two classes of methods to train EBMs: (1) contrastive methods that push down on the energy of data points and push up elsewhere; (2) architectural and regularizing methods that limit or minimize the volume of space that can take low energies by regularizing the information capacity of a latent variable. While contrastive methods have been somewhat successful to learn image features, they are very expensive computationally. I will propose that the future of self-supervised representation learning lies in regularized latent-variable energy-based models. ',
  'title': 'Reflections from the Turing Award Winners',
  'topic': 'Deep Learning',
  'datetime': datetime.datetime(2021, 12, 9, 13, 0),
  'speaker': 'Profs. Yann LeCun and Yoshua Bengio'},
 {'description': 'While there has been significant progress at the interface of statistics and computer science in recent years, many fundamental challenges remain. Some are mathematical and algorithmic in nature, such as the challenges associated with optimization and sampling in high-dimensional spaces. Some are statistical, including the challenges associated with multiple decision-making. Others are economic in nature, including the need to cope with scarcity and provide incentives in learning-based two-way markets. I will present recent progress on each of these fronts.',
  'title': 'The Decision-Making Side of Machine Learning: Dynamical, Statistical and Economic Perspectives',
  'topic': 'Machine Learning',
  'datetime': datetime.datetime(2021, 12, 9, 17, 0),
  'speaker': 'Prof. Michael I. Jordan'}]


def delete_collection(coll_ref, batch_size=64):
    docs = coll_ref.limit(batch_size).stream()
    deleted = 0

    for doc in docs:
        #print(f'Deleting doc {doc.id} => {doc.to_dict()}')
        doc.reference.delete()
        deleted = deleted + 1

    if deleted >= batch_size:
        return delete_collection(coll_ref, batch_size)


def main():
    # initialize firebase
    cred = credentials.Certificate("serviceAccountKey.json")
    firebase_admin.initialize_app(cred)

    db = firestore.client()

    # clear collections
    delete_collection(db.collection('speakers'))
    delete_collection(db.collection('conferences'))

    # populate collections
    for conference in conferences:
        db.collection('conferences').add(conference)

    for speaker in speakers:
        db.collection('speakers').add(speaker)

    print('Done!')

if __name__ == "__main__":
    main()