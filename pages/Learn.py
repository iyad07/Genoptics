from flet import *


class Learn(UserControl):
    
    def __init__(self,page):
        super().__init__()
        self.page = page
        self.slides=Row([
            Container(
                content=Column([
                    Row([Text("Genetic Terminologies",size=60,weight=FontWeight.BOLD,)],alignment=MainAxisAlignment.CENTER)
                ],alignment=MainAxisAlignment.SPACE_EVENLY),
                width=1035,
                height=400,
                
                bgcolor="#eeeeee",
                padding=100,
                border_radius=40),
            Container(
                content=Column([
                    Row([Text("Genes",size=40,weight=FontWeight.W_800)],alignment=MainAxisAlignment.CENTER),
                    Text("Genes are the fundamental units of heredity found on chromosomes. They control various characteristics or traits in plants and animals. A gene can be made up of numerous DNA bases.",size=20,text_align=TextAlign.JUSTIFY),
                    Row([Container(image_src="gene1.jpeg",image_fit=ImageFit.FILL,width=200,height=100,border_radius=30),Container(image_src="gene4.jpeg",image_fit=ImageFit.FILL,width=200,height=100,border_radius=30),Container(image_src="gene2.jpeg",image_fit=ImageFit.FILL,width=200,height=100,border_radius=30),Container(image_src="gene3.jpeg",image_fit=ImageFit.FILL,width=200,height=100,border_radius=30)],alignment=MainAxisAlignment.CENTER),
                ],alignment=MainAxisAlignment.SPACE_AROUND),
                height=400,
                width=1035,
                bgcolor="#eeeeee",
                padding=50,
                border_radius=40
                ),
            Container(
                content=Column([
                    Row([Text("Locus",size=40,weight=FontWeight.W_800)],alignment=MainAxisAlignment.CENTER),
                    Text("The locus refers to the specific position of a gene on a chromosome. It's like an address that indicates where a gene is located.",size=20,text_align=TextAlign.JUSTIFY),
                    Row([Container(image_src="locus1.jpeg",image_fit=ImageFit.FILL,width=200,height=100,border_radius=30),
                         Container(image_src="locus2.jpeg",image_fit=ImageFit.FILL,width=200,height=100,border_radius=30),
                         Container(image_src="locus3.png",image_fit=ImageFit.FILL,width=200,height=100,border_radius=30),
                         Container(image_src="locus4.png",image_fit=ImageFit.FILL,width=200,height=100,border_radius=30)],alignment=MainAxisAlignment.CENTER),
                    
                ],alignment=MainAxisAlignment.SPACE_AROUND),
                height=400,
                width=1035,
                bgcolor="#eeeeee",
                padding=100,
                border_radius=40
                ),
            Container(
              content=Column([
                  Row([Text("Alleles",size=40,weight=FontWeight.W_800)],alignment=MainAxisAlignment.CENTER),
                  Text("Alleles are alternate forms or versions of a gene that exist at the same locus on homologous chromosomes. They give rise to contrasting traits. For example, peach and brown eye color alleles.",size=20,text_align=TextAlign.JUSTIFY),
                  Row([Container(image_src="dll1.jpeg",image_fit=ImageFit.FILL,width=200,height=100,border_radius=30),
                       Container(image_src="dll2.jpg",image_fit=ImageFit.FILL,width=200,height=100,border_radius=30),
                       Container(image_src="dll3.jpeg",image_fit=ImageFit.FILL,width=200,height=100,border_radius=30),
                       Container(image_src="dll4.jpg",image_fit=ImageFit.FILL,width=200,height=100,border_radius=30)],alignment=MainAxisAlignment.CENTER),
                  
              ],alignment=MainAxisAlignment.SPACE_AROUND),
              height=400,
              width=1035,
              bgcolor="#eeeeee",
              padding=100,
              border_radius=40),
            Container(
                content=Column([
                    Row([Text("Carrier",size=40,weight=FontWeight.W_800)],alignment=MainAxisAlignment.CENTER),
                    Text("A carrier is an individual who carries a recessive allele for a trait without expressing the trait themselves. Carriers can pass on the allele to their offspring.",size=20,text_align=TextAlign.JUSTIFY),
                    Row([Container(image_src="car.jpg",image_fit=ImageFit.FILL,width=200,height=100,border_radius=30),
                         Container(image_src="car2.jpg",image_fit=ImageFit.FILL,width=200,height=100,border_radius=30),
                         Container(image_src="car3.jpg",image_fit=ImageFit.FILL,width=200,height=100,border_radius=30),
                         Container(image_src="car4.jpg",image_fit=ImageFit.FILL,width=200,height=100,border_radius=30)],alignment=MainAxisAlignment.CENTER),
                    
                ],alignment=MainAxisAlignment.SPACE_AROUND),
                height=400,
                width=1035,
                bgcolor="#eeeeee",
                padding=100,
                border_radius=40),
            Container(
                content=Column([
                    Row([Text("Chromosomes",size=40,weight=FontWeight.W_800)],alignment=MainAxisAlignment.CENTER),
                    Text("Chromosomes are thread-like structures within cells that contain genes. The number of chromosomes is species-specific. Humans, for instance, have 46 chromosomes in each somatic cell.",size=20,text_align=TextAlign.JUSTIFY),
                    Row([Container(image_src="chrom.jpg",image_fit=ImageFit.FILL,width=200,height=100,border_radius=30),
                         Container(image_src="chrom2.jpg",image_fit=ImageFit.FILL,width=200,height=100,border_radius=30),
                         Container(image_src="chrom3.jpg",image_fit=ImageFit.FILL,width=200,height=100,border_radius=30),
                         Container(image_src="chrom4.jpg",image_fit=ImageFit.FILL,width=200,height=100,border_radius=30)],alignment=MainAxisAlignment.CENTER),
                    
                ],alignment=MainAxisAlignment.SPACE_AROUND),
                height=400,
                width=1035,
                bgcolor="#eeeeee",
                padding=100,
                border_radius=40),
            Container(
                content=Column([
                    Row([Text("Genome",size=40,weight=FontWeight.W_800)],alignment=MainAxisAlignment.CENTER),
                    Text("The genome represents an individual's complete set of genetic material. In humans, this encompasses approximately 2.9 billion base units in DNA.",size=20,text_align=TextAlign.JUSTIFY),
                    
                ],alignment=MainAxisAlignment.SPACE_AROUND),
                height=400,
                width=1035,
                bgcolor="#eeeeee",
                padding=100,
                border_radius=40),
            Container(
                content=Column([
                    Row([Text("Dominance and Codominance",size=40,weight=FontWeight.W_800)],alignment=MainAxisAlignment.CENTER),
                    Text("Dominance occurs when one allele's effect masks that of another allele. Codominance, on the other hand, manifests when both alleles in a heterozygous individual are equally expressed.",size=20,text_align=TextAlign.JUSTIFY),
                    
                ],alignment=MainAxisAlignment.SPACE_AROUND),
                height=400,
                width=1035,
                bgcolor="#eeeeee",
                padding=100,
                border_radius=40),
            Container(
                content=Column([
                    Row([Text("Dominant and Recessive Alleles",size=40,weight=FontWeight.W_800)],alignment=MainAxisAlignment.CENTER),
                    Text("Dominant alleles mask the effects of recessive alleles in the phenotype. Dominant alleles are represented by capital letters, while recessive alleles by lowercase letters.",size=20,text_align=TextAlign.JUSTIFY),
                    
                ],alignment=MainAxisAlignment.SPACE_AROUND),
                height=400,
                width=1035,
                bgcolor="#eeeeee",
                padding=100,
                border_radius=40),
            Container(
                content=Column([
                    Row([Text("Dominant and Recessive Alleles",size=40,weight=FontWeight.W_800)],alignment=MainAxisAlignment.CENTER),
                    Text("Dominant alleles mask the effects of recessive alleles in the phenotype. Dominant alleles are represented by capital letters, while recessive alleles by lowercase letters.",size=20,text_align=TextAlign.JUSTIFY),
                    
                ],alignment=MainAxisAlignment.SPACE_AROUND),
                height=400,
                bgcolor="#eeeeee",
                width=1035,
                padding=100,
                border_radius=40),
            Container(
                content=Column([
                    Row([Text("DNA (Deoxyribonucleic Acid)",size=40,weight=FontWeight.W_800)],alignment=MainAxisAlignment.CENTER),
                    Text("DNA is a complex molecule that holds the genetic code and is composed of sugars, phosphates, and bases in a double-helix structure.",size=20,text_align=TextAlign.JUSTIFY),
                    Row([Container(image_src="gene1.jpeg",image_fit=ImageFit.FILL,width=200,height=100,border_radius=30),
                         Container(image_src="gene4.jpeg",image_fit=ImageFit.FILL,width=200,height=100,border_radius=30),
                         Container(image_src="gene2.jpeg",image_fit=ImageFit.FILL,width=200,height=100,border_radius=30),
                         Container(image_src="gene3.jpeg",image_fit=ImageFit.FILL,width=200,height=100,border_radius=30)],alignment=MainAxisAlignment.CENTER),
                    
                ],alignment=MainAxisAlignment.SPACE_AROUND),
                height=400,
                width=1035,
                bgcolor="#eeeeee",
                padding=100,
                border_radius=40),
            Container(
                content=Column([
                    Row([Text("Genotype and Phenotype",size=40,weight=FontWeight.W_800)],alignment=MainAxisAlignment.CENTER),
                    Text("Genotype refers to an organism's genetic makeup, while phenotype represents its observable physical characteristics influenced by both genetics and the environment.",size=20,text_align=TextAlign.JUSTIFY),
                    
                ],alignment=MainAxisAlignment.SPACE_AROUND),
                height=400,
                width=1035,
                bgcolor="#eeeeee",
                padding=100,
                border_radius=40),
            Container(
              content=Column([
                  Row([Text("Heterozygous and Homozygous",size=40,weight=FontWeight.W_800)],alignment=MainAxisAlignment.CENTER),
                  Text("Heterozygous individuals possess two different alleles for a gene (e.g., Aa), whereas homozygous individuals have two identical alleles (AA or aa).",size=20,text_align=TextAlign.JUSTIFY),
                  
              ],alignment=MainAxisAlignment.SPACE_AROUND),
              height=400,
              width=1035,
              bgcolor="#eeeeee",
              padding=100,
              border_radius=40),
            Container(
                content=Column([
                    Row([Text("Monohybrid and Dihybrid Crosses",size=40,weight=FontWeight.W_800)],alignment=MainAxisAlignment.CENTER),
                    Text("Monohybrid crosses involve a single trait, while dihybrid crosses consider two traits. These crosses help predict offspring traits.",size=20,text_align=TextAlign.JUSTIFY),
                    
                ],alignment=MainAxisAlignment.SPACE_AROUND),
                height=400,
                width=1035,
                bgcolor="#eeeeee",
                padding=100,
                border_radius=40)
        
                
              ],scroll=True)
        self.pb= ProgressBar(value=0,width=1035,height=10,color="#210C3B")
        

        
        
        
      

    def slid(self, e):
        self.slides.scroll_to(delta=1045,duration=1000)
        self.pb.value+=1/len(self.slides.controls)
        sleep=0.5
        self.update()
    
    
        
        
        

      
            
        
    def build(self):
        
        lea=Column([Row([IconButton(icon="home",on_click=lambda e:self.page.go("/home")),
                         Text("Learn",size=70,weight=FontWeight.BOLD),
                         PopupMenuButton(
                             items=[
                                 PopupMenuItem(text="Home",on_click=lambda e:self.page.go("/home")),
                                 PopupMenuItem(text="Calculator",on_click=lambda e:self.page.go("/calculator")),
                                 PopupMenuItem(text="Questions",on_click=lambda e:self.page.go("/quest"))
                                 ])],alignment=MainAxisAlignment.SPACE_BETWEEN),
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
        con=Container(
                content=lea,
                image_src="weee.png",
                bgcolor="",
                height=720,
                padding=padding.only(left=150,right=150,top=50,),
                border_radius=30,
                image_opacity=0.7,
                image_fit=ImageFit.FILL
                )
        
        return con
  
    


     