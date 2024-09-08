from flet import *

phenotype1 = Dropdown(
        label="Phenotype for species 1",
        
        options=[
            dropdown.Option("Homozygote"),
            dropdown.Option("Heterozygote")
        ]
    )
genotype1 = TextField(label="Genotype for species 1",autofocus=True)
phenotype2 = Dropdown(
    label="Phenotype for species 2",
    options=[
        dropdown.Option("Homozygote"),
        dropdown.Option("Heterozygote")
    ]
)
genotype2 = TextField(label="Genotype for species 2",autofocus=True)
genotype_alphabet1 = TextField(label="Enter the description for species 1: ",autofocus=True)
genotype_alphabet2 = TextField(label="Enter the description for species 2: ",autofocus=True)
offspring_phenotypes = []
offspring_probabilities = []

class Calculator(UserControl):
    
    def __init__(self,page):
        super().__init__()
        self.page = page
        self.results=Column([],scroll=True)
        
      

    def cal(self, e):
        self.results.controls.clear()
        # Function to determine the offspring phenotype based on allele dominance
        def determine_offspring_phenotype(allele1, allele2, phenotype1, phenotype2):
            if allele1.isupper() and allele2.isupper():
                return f"{phenotype1} ({allele1}{allele2})"
            elif allele1.islower() and allele2.islower():
                return f"{phenotype2} ({allele1}{allele2})"
            else:
                return f"{phenotype1}{phenotype2} ({allele1}{allele2})"

        # Function to calculate probabilities for each offspring phenotype
        def calculate_probabilities(offspring_phenotypes):
            total_offspring = len(offspring_phenotypes)
            probability = 1 / total_offspring
            return [probability] * total_offspring

        # Function to print individual probabilities for each phenotype
        prob=Column()
        def print_individual_probabilities(offspring_phenotypes, offspring_probabilities, genotype_description):
            H3=(Text(value="Individual probabilities for each phenotype:",style=TextThemeStyle.BODY_LARGE))
            for phenotype, probability in zip(offspring_phenotypes, offspring_probabilities):
                prob.controls.append(Text(value=f"{phenotype} [{genotype_description}]: {probability}",size=15))
            
            CLi=Container(content=Row([Column([H3,prob])],alignment=MainAxisAlignment.CENTER),padding=10,bgcolor="#E6E6FA",border_radius=20)
            self.results.controls.append(Container(content=CLi,
                            bgcolor="#C8A2C8",
                            padding=15,
                            border_radius=15,
                            ))
            self.update()
        
            

        # Function to calculate cumulative probabilities for each phenotype
        def calculate_cumulative_probabilities(offspring_phenotypes, offspring_probabilities):
            cumulative_probabilities = {}
            for phenotype, probability in zip(offspring_phenotypes, offspring_probabilities):
                if phenotype in cumulative_probabilities:
                    cumulative_probabilities[phenotype] += probability
                else:
                    cumulative_probabilities[phenotype] = probability
            return cumulative_probabilities

        # Function to sum probabilities of like phenotypes
        def sum_probabilities_of_like_phenotypes(cumulative_probabilities):
            summed_probabilities = {}
            for phenotype, probability in cumulative_probabilities.items():
                phenotype_name = phenotype.split(" ")[0]  # Extract the phenotype name
                if phenotype_name in summed_probabilities:
                    summed_probabilities[phenotype_name] += probability
                else:
                    summed_probabilities[phenotype_name] = probability
            return summed_probabilities

        def main():
            
            # Get input from the user
            
            
            # Validate input (Optional: Implement your specific validation logic here)

            # Generate offspring phenotypes
            species1_alleles = genotype1.value + genotype1.value if phenotype1.value.lower() == "homozygote" else genotype1.value.upper() + genotype1.value.lower()
            species2_alleles = genotype2.value + genotype2.value if phenotype2.value.lower() == "homozygote" else genotype2.value.upper() + genotype2.value.lower()

            offspring_phenotypes = []
            for allele1 in species1_alleles:
                for allele2 in species2_alleles:
                    offspring_phenotype = determine_offspring_phenotype(allele1, allele2, phenotype1.value, phenotype2.value)
                    offspring_phenotypes.append(offspring_phenotype)

            # Calculate probabilities for each phenotype
            offspring_probabilities = calculate_probabilities(offspring_phenotypes)

            # Print individual probabilities for each phenotype
            genotype_description = genotype_alphabet1.value + genotype_alphabet2.value
            print_individual_probabilities(offspring_phenotypes, offspring_probabilities, genotype_description)

            # Calculate cumulative probabilities for each phenotype
            cumulative_probabilities = calculate_cumulative_probabilities(offspring_phenotypes, offspring_probabilities)

            # Print offspring phenotypes and cumulative probabilities
            off_prob=Column()
            H2=(Text(value="Offspring phenotypes and cumulative probabilities:",size=18))
            for phenotype, probability in cumulative_probabilities.items():
                off_prob.controls.append(Text(value=f"{phenotype}: {probability}",size=15))
            
            CPi=Container(content=Column([H2,off_prob]),bgcolor="#E6E6FA",border_radius=20,padding=10)
            # Sum probabilities of like phenotypes
            sum_prob=Column()
            summed_probabilities = sum_probabilities_of_like_phenotypes(cumulative_probabilities)
            H1=(Text(value="Summed probabilities of like phenotypes:",size=18,font_family=""))
            for phenotype, probability in summed_probabilities.items():
                sum_prob.controls.append(Text(value=f"{phenotype}: {probability}",size=15))
            
            CPp=Container(content=(Column([H1,sum_prob])),bgcolor="#E6E6FA",border_radius=20,padding=10)
            Fin_CPp=Row([CPi,CPp],alignment=MainAxisAlignment.SPACE_EVENLY)
            self.results.controls.append(Container(content=Fin_CPp,
                        padding=10,
                        bgcolor="#C8A2C8",
                        alignment=alignment.center,
                        border_radius=15))
            self.update()
        main()
        def create_punnett_square():
        # Generate the Punnett square
            square = [
                [f"{genotype1.value[0]}{genotype2.value[0]}", f"{genotype1.value[0]}{genotype2.value[1]}"],
                [f"{genotype1.value[1]}{genotype2.value[0]}", f"{genotype1.value[1]}{genotype2.value[1]}"]
            ]

            # Calculate the probabilities
            probability_BB = genotype1.value.count('B') / 2 * genotype2.value.count('B') / 2
            probability_Bb = (genotype1.value.count('B') / 2 * genotype2.value.count('b')) + (genotype1.value.count('b') * genotype2.value.count('B') / 2)
            probability_bb = genotype1.value.count('b') / 2 * genotype2.value.count('b') / 2

            # page.add the Punnett square with customized column and row names
            self.results.controls.append(Row([DataTable(
                        columns=[
                            DataColumn(Text("")),
                            DataColumn(Text(genotype1.value[0])),
                            DataColumn(Text(genotype1.value[1])),
                        ],
                        rows=[
                            DataRow(
                                cells=[
                                    DataCell(Text(genotype2.value[0])),
                                    DataCell(Text(square[0][0])),
                                    DataCell(Text(square[0][1])),
                                ],
                            ),
                            DataRow(
                                cells=[
                                    DataCell(Text(genotype2.value[1])),
                                    DataCell(Text(square[1][0])),
                                    DataCell(Text(square[1][1])),
                                ],
                            ),
                            
                        ],
                    ),],alignment=MainAxisAlignment.CENTER)
                )
            self.update()

        if len(genotype1.value) and len(genotype2.value) ==2 :
            create_punnett_square()
        else:
           self.results.controls.append(Text("To show punnett square enter genotype with 2 alleles! Note that the phenotype does not affect the Punnet square results! ",weight=FontWeight.BOLD))
        self.update()
        self.dlg=AlertDialog(title=Text("Results",text_align=TextAlign.CENTER,weight=FontWeight.W_700),content=self.results)
        self.page.dialog=self.dlg
        self.dlg.open=True
        self.page.update()
        
        
        
            
        
        
        
      
            
        
    def build(self):
        col_2= Column([Row([
            Container(content=Column([phenotype1,genotype1,genotype_alphabet1],alignment=MainAxisAlignment.CENTER),
                    padding=40,
                    bgcolor="#C8A2C8",
                    border_radius=border_radius.only(top_right=30,bottom_left=30),
                    ink= True,
                    shadow=BoxShadow(
                            spread_radius=1,
                            blur_radius=30,
                            color=colors.BLACK,
                            offset=Offset(-10, 10),
                            blur_style=ShadowBlurStyle.NORMAL,
                            ),
                    
                    ),
            Container(content=Text(value="X",size=30),
                    padding=10,
                    border_radius=30,
            ),
            Container(content=Column([phenotype2,genotype2,genotype_alphabet2],alignment=MainAxisAlignment.CENTER),
                    bgcolor="#E6E6FA",
                    padding=40,
                    border_radius=border_radius.only(top_left=30,bottom_right=30),
                    ink=True,
                    shadow=BoxShadow(
                            spread_radius=1,
                            blur_radius=30,
                            color=colors.BLACK,
                            offset=Offset(10, 10),
                            blur_style=ShadowBlurStyle.NORMAL,
                            ),
                    )
            ],alignment=MainAxisAlignment.SPACE_AROUND),
            Row([
                ElevatedButton("Generate",
                                        style=ButtonStyle(
                                            bgcolor={MaterialState.DEFAULT:"#8F19FB", MaterialState.HOVERED:"#B97FED"},
                                            color="#FFFFFF",
                                            shape=RoundedRectangleBorder(radius=10)
                                        ),
                                        on_click=self.cal,
                                        width=200,
                                        height=50,
                                        )
                ],
                alignment=MainAxisAlignment.CENTER)
            ],
            alignment=MainAxisAlignment.SPACE_BETWEEN
            )
        
        
        
        return Container(
                content=Column([
                    Container(content=Row([IconButton(icon="home",icon_size=30,on_click=lambda e:self.page.go("/home")),
                         Text("Calculator",size=70,weight=FontWeight.BOLD),
                         PopupMenuButton(
                             items=[
                                 PopupMenuItem(text="Home",on_click=lambda e:self.page.go("/home")),
                                 PopupMenuItem(text="Learn",on_click=lambda e:self.page.go("/learn")),
                                 PopupMenuItem(text="Questions",on_click=lambda e:self.page.go("/quest"))
                                 ])],
                        alignment=MainAxisAlignment.SPACE_BETWEEN),
                              padding=padding.only(bottom=30,left=40)),
                    col_2],alignment=MainAxisAlignment.SPACE_BETWEEN),
                image_src="weee.png",
                height=720,
                bgcolor="",
                padding=padding.only(left=100,right=100,top=50,bottom=140),
                border_radius=30,
                image_opacity=0.7,
                image_fit=ImageFit.COVER
                )