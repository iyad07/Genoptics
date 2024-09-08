from flet import*
class Home(UserControl):
    
    def __init__(self,page):
        super().__init__()
        self.page = page
    def build(self):
        menu_bar=Row([
            Row([Text("Genoptics",size=45,weight=FontWeight.BOLD)],alignment=MainAxisAlignment.START,width=500),
            Row([
                TextButton("LEARN",
                           style=ButtonStyle(
                                color={MaterialState.DEFAULT:"#402E58", 
                                       MaterialState.HOVERED:"#402E58",
                                       MaterialState.PRESSED:"#ffffff"},
                                bgcolor={MaterialState.HOVERED:"#B97FED",
                                         MaterialState.PRESSED:"#402E58"},
                                shape=RoundedRectangleBorder(radius=10)
                ),on_click=lambda e:self.page.go("/learn")),
                TextButton("QUESTIONS",
                           style=ButtonStyle(
                                color={MaterialState.DEFAULT:"#402E58", 
                                       MaterialState.HOVERED:"#402E58",
                                       MaterialState.PRESSED:"#ffffff"},
                                bgcolor={MaterialState.HOVERED:"#B97FED",
                                         MaterialState.PRESSED:"#402E58"},
                                shape=RoundedRectangleBorder(radius=10),               
                ),on_click=lambda e:self.page.go("/quest")),   
                ElevatedButton("CALCULATE",
                    style=ButtonStyle(
                        bgcolor={MaterialState.DEFAULT:"#8F19FB", 
                                 MaterialState.HOVERED:"#B97FED"},
                        color="#FFFFFF",
                        shape=RoundedRectangleBorder(radius=10)
                    ),
                    
                    width=150,
                    height=50,
                    on_click=lambda e:self.page.go("/calculator")
                    )
            ],alignment=MainAxisAlignment.SPACE_BETWEEN,width=530)
        ])
        header=Column([menu_bar],alignment=MainAxisAlignment.START)
        Intro=Row([
            Container(content=Column([Row([Text("Simplify",size=30) ,
                    Text("genetic",color="#402E58",size=30,weight=FontWeight.BOLD ),
                    Text("exploration by effortlessly",size=30) ,
                    Text("calculating probabilities between two species,",color="#402E58",size=30,weight=FontWeight.BOLD), 
                    Text("unlocking the secrets of inheritance.",size=30)
                    ],wrap=True),
                ElevatedButton("GET STARTED",
                    style=ButtonStyle(
                        bgcolor={MaterialState.DEFAULT:"#402E58", MaterialState.HOVERED:"#B97FED"},
                        color="#FFFFFF",
                        shape=RoundedRectangleBorder(radius=10)
                    ),
                    width=150,
                    height=50,
                    on_click=lambda e:self.page.go("/learn")
                    )],alignment=MainAxisAlignment.SPACE_EVENLY),
                     height=450,
                     width=700,
                     padding=padding.only(bottom=20,right=40),
                     
                     
                     ),
            Column([Container(
                image_src="guy.png",
                image_fit=ImageFit.CONTAIN,
                padding=20,
                height=450,
                width=350
            )])
            
            ],alignment=MainAxisAlignment.SPACE_EVENLY)
        homee=Column([header,Intro],alignment=MainAxisAlignment.SPACE_BETWEEN)
        
        
        
        
        return Container(
                content=homee,
                image_src="weee.jpeg",
                height=720,
                bgcolor="",
                padding=padding.only(left=150,right=150,top=50,bottom=100),
                border_radius=30,
                image_opacity=0.7,
                image_fit=ImageFit.COVER
                )