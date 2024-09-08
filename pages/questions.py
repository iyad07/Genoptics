from flet import *
questions=[("WHAT IS A  MONOHYBRID CROSS?",Dropdown(label="Your Answer",
                    width= 625,
                    border_color="#B97FED",
                    bgcolor="#B97FED",
                    options=[
                        dropdown.Option("a) A genetic cross involving two traits"),
                        dropdown.Option("b) A cross between genetically identical parents"),
                        dropdown.Option("c) A cross between purebred parents"),
                        dropdown.Option("d) A genetic cross using a single trait with two alleles")
                    ]),"d) A genetic cross using a single trait with two alleles"),
            ("WHAT IS THE DIFFERENCE BETWEEN GENOTYPE AND PHENOTYPE?",Dropdown(label="Your Answer",
                    width= 1000,
                    border_color="#B97FED",
                    bgcolor="#B97FED",
                    options=[
                        dropdown.Option("a) Genotype refers to physical appearance, while phenotype refers to genetic makeup."),
                        dropdown.Option("b) Genotype refers to genetic makeup, while phenotype refers to physical appearance."),
                        dropdown.Option("c) Genotype and phenotype are synonyms."),
                        dropdown.Option("d) Genotype refers to DNA, while phenotype refers to proteins.")
                    ]),"b) Genotype refers to genetic makeup, while phenotype refers to physical appearance."),
            ("WHAT ARE GENES?",Dropdown(label="Your Answer",
                    width= 625,
                    border_color="#B97FED",
                    bgcolor="#B97FED",
                    options=[
                        dropdown.Option("a) A type of chromosome"),
                        dropdown.Option("b) A unit of hereditary material located on chromosomes"),
                        dropdown.Option("c) An allele for a specific trait"),
                        dropdown.Option("d) A type of genetic engineering technique")
                    ]),"b) A unit of hereditary material located on chromosomes"),
            (("WHAT ARE CARRIER?"),Dropdown(label="Your Answer",
                    width= 625,
                    border_color="#B97FED",
                    bgcolor="#B97FED",
                    options=[
                        dropdown.Option("a) Thread-like structures in cells"),
                        dropdown.Option("b) Alternate forms of a gene"),
                        dropdown.Option("c) Cells with unique genetic information"),
                        dropdown.Option("d) Non-genetic traits")
                    ]),"b) Alternate forms of a gene"),
            (("WHAT ARE CHROMOSOMES?"),Dropdown(label="Your Answer",
                    width= 625,
                    border_color="#B97FED",
                    bgcolor="#B97FED",
                    options=[
                        dropdown.Option("a) An individual with two dominant alleles"),
                        dropdown.Option("b) An individual expressing a recessive trait"),
                        dropdown.Option("c) An individual carrying a recessive allele without expressing the trait"),
                        dropdown.Option("d) An individual with a genetic disorder")
                    ]),"c) An individual carrying a recessive allele without expressing the trait"),
            (("WHAT IS THE PURPOSE OF THIS NOTE?"),Dropdown(label="Your Answer",
                    width= 625,
                    border_color="#B97FED",
                    bgcolor="#B97FED",
                    options=[
                        dropdown.Option("a) To discuss the importance of random mutations"),
                        dropdown.Option("b) To explore the effects of environmental factors on genetics"),
                        dropdown.Option("c) To provide an overview of essential genetic concepts and terms"),
                        dropdown.Option("d) To analyze the relationship between genetics and psychology")
                    ]),"c) To provide an overview of essential genetic concepts and terms"),
            (" WHAT IS A HYBRID?",Dropdown(label="Your Answer",
                    width= 625,
                    border_color="#B97FED",
                    options=[
                        dropdown.Option("a) An individual with a genetic disorder"),
                        dropdown.Option("b) Offspring resulting from mating genetically similar parents"),
                        dropdown.Option("c) Offspring resulting from the mating of genetically distinct parents"),
                        dropdown.Option("d) Offspring with identical alleles")
                    ]),"c) Offspring resulting from the mating of genetically distinct parents"),
            ("WHAT IS A HETEROZYGOUS INDIVIDUAL?",Dropdown(label="Your Answer",
                    width= 625,
                    border_color="#B97FED",
                    options=[
                        dropdown.Option("a) The complete set of genetic material in an individual"),
                        dropdown.Option("b) The number of chromosomes in a somatic cell"),
                        dropdown.Option("c) The number of genes in a species"),
                        dropdown.Option("d) The length of a DNA molecule")
                    ]),"a) The complete set of genetic material in an individual"),
            ("WHAT DOES “GENOME” ENCOMPASS?",Dropdown(label="Your Answer",
                    width= 625,
                    border_color="#B97FED",
                    options=[
                        dropdown.Option("a) One with two identical alleles"),
                        dropdown.Option("b) One with two different alleles for a gene"),
                        dropdown.Option("c) One with two dominant alleles"),
                        dropdown.Option("d) One with a genetic disorder")
                    ]),"b) One with two different alleles for a gene"),
            (("WHAT IS “CODOMINANCE”?"),Dropdown(label="Your Answer",
                    width= 625,
                    border_color="#B97FED",
                    options=[
                        dropdown.Option("a) When one allele's effect masks that of another allele"),
                        dropdown.Option("b) When both alleles in a heterozygous individual are equally expressed"),
                        dropdown.Option("c) When alleles are located at different loci"),
                        dropdown.Option("d) When a gene has multiple alleles")
                    ]),"b) When both alleles in a heterozygous individual are equally expressed"),
            (("WHAT IS THE MOLECULAR STRUCTURE OF DNA?"),Dropdown(label="Your Answer",
                    width= 625,
                    border_color="#B97FED",
                    options=[
                        dropdown.Option("a) Single strand"),
                        dropdown.Option("b) Spiral ladder"),
                        dropdown.Option("c) Tetrahedral shape"),
                        dropdown.Option("d) Double helix")
                    ]),"d) Double helix"),
            (("WHAT DO DOMINANT ALLELES DO?"),Dropdown(label="Your Answer",
                    width= 625,
                    border_color="#B97FED",
                    options=[
                        dropdown.Option("a) Mask the effects of recessive alleles"),
                        dropdown.Option("b) Express both alleles equally"),
                        dropdown.Option("c) Blend the traits of both alleles"),
                        dropdown.Option("d) Mutate in response to environmental changes")
                    ]),"a) Mask the effects of recessive alleles"),
            ("WHAT ARE POLYGENIC TRAITS?",Dropdown(label="Your Answer",
                    width= 625,
                    border_color="#B97FED",
                    options=[
                        dropdown.Option("a) Traits influenced by multiple gene loci"),
                        dropdown.Option("b) Traits influenced by a single gene"),
                        dropdown.Option("c) Traits influenced only by the environment"),
                        dropdown.Option("d) Traits caused by genetic mutations")
                    ]),"a) Traits influenced by multiple gene loci"),
            
             
            
            ]



    
class Questions(UserControl):
    
    def __init__(self, page):
        super().__init__()
        self.score = 0
        self.page = page
        self.slides = Row([], scroll=True)    
        self.pb = ProgressBar(value=0, width=1035, height=5,color="#210C3B")

        # Use the existing dropdowns from the questions list
        self.answer_dropdowns = [question[1] for question in questions]

        for i, (question, _, _) in enumerate(questions):
            # Add the question and dropdown to the slides
            self.slides.controls.append(Container(
                content=Column([Text(question,weight=FontWeight.BOLD), self.answer_dropdowns[i]],alignment=MainAxisAlignment.CENTER),
                height=400,
                width=1035,
                bgcolor="#eeeeee",
                padding=100,
                border_radius=40
            ))
            self.update()
            
    def slid(self, e):
        self.score=0
        # Scroll to the next question
        self.slides.scroll_to(delta=1045, duration=1000)
        self.pb.value+=1/len(questions)
        self.update()
        
        
        
        
        def check_answers():
            # Iterate through the answers and check correctness
            for i, dropdown in enumerate(self.answer_dropdowns):
                # Get the user's answer from the corresponding dropdown
                user_answer = dropdown.value
                
                # Get the correct answer for the current question
                correct_answer = questions[i][2]
                
                # Check if the user's answer is correct
                if user_answer == correct_answer:
                    self.score += 1
                    
                
            # Display the final score
            
            final_message = f"You got {self.score} out of {len(questions)} questions correct."
            self.dlg = AlertDialog(title=Text(final_message, text_align=TextAlign.CENTER, weight=FontWeight.W_700))
            self.page.dialog = self.dlg
            self.dlg.open = True
            self.page.update()
        check_answers()
        



       
        
    
    
        
        
        

      
            
        
    def build(self):
        
        lea=Column([Row([IconButton(icon="home",icon_size=30,on_click=lambda e:self.page.go("/home")),
                         Text("Questions",size=70,weight=FontWeight.BOLD),
                         PopupMenuButton(
                             items=[
                                 PopupMenuItem(text="Home",on_click=lambda e:self.page.go("/home")),
                                 PopupMenuItem(text="Calculator",on_click=lambda e:self.page.go("/calculator")),
                                 PopupMenuItem(text="Learn",on_click=lambda e:self.page.go("/quest"))
                                 ])],
                        alignment=MainAxisAlignment.SPACE_BETWEEN),
                    self.pb,
                    self.slides,
                    Row([ElevatedButton("Next",
                                        style=ButtonStyle(
                                            bgcolor={MaterialState.DEFAULT:"#8F19FB", MaterialState.HOVERED:"#B97FED"},
                                            color="#FFFFFF",
                                            shape=RoundedRectangleBorder(radius=10)
                                        ),
                                        on_click=self.slid,
                                        width=100,
                                        height=50,
                                        )
                         ],alignment=MainAxisAlignment.END)
                    ],scroll=True)
        
        
        return Container(
                content=lea,
                image_src="weee.png",
                height=720,
                
                padding=padding.only(left=150,right=150,top=50,),
                border_radius=30,
                image_opacity=0.7,
                image_fit=ImageFit.FILL
                )
  
    


     