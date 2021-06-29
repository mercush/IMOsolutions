from manim import *

def emphasize(self,point):
    self.play(ApplyMethod(point.scale,3/2))
    self.play(ApplyMethod(point.scale),2/3)

class Introduction(Scene):
  def construct(self):
    imologo= ImageMobject("IMOLogo.jpg")
    imologo.scale(0.5)
    self.play(GrowFromCenter(imologo))
    self.play(FadeOut(imologo))
class ProblemStatement(Scene):
  def construct(self):
    text=Tex(
            r"El Triangulo $BCF$ es rectangulo en $B$.", r"Sea $A$ el punto de la recta\
            $CF$ tal que $FA=FB$ y $F$ esta entre $A$ y $C$.", r"Se elige el punto $D$ de\
            modo que $DA=DC$ y $AC$ es bisectriz del angulo $\angle EAC$.", r"Se elige\
            el punto $E$ de modo que $EA=ED$ y $AD$ es bisectriz del angulo $\angle EAC$.",
            r"Sea $M$ el punto medio de $CF$.", r"Sea $X$ el punto tal que $AMXE$ es un\
            paralelogramo (con $AM || EX$ y $AE || MX$).", r"Demostrar que las rectas\
            $BD, FX$, y $ME$ son concurrentes."
        ).scale(0.4)
    self.play(Write(text))
    self.play(ApplyMethod(text.shift,2.5*UP))
    highlighted = [0,0,0,0,0,0]
    for i in range(6):
      highlighted[i] = text[i].copy().set_color(RED)

    # self.wait(5)
    
    A = np.array([-2.25,-3.3,0])
    B = np.array([0.19,-3.3,0])
    C = np.array([2.82,0.37,0])
    D = np.array([-1.03,0.37,0])
    E = np.array([-2.98,-1.03,0])
    F = np.array([-1.03,-2.43,0])
    M = np.array([0.895,-1.03,0])
    X = np.array([0.17,1.23,0])

    BCF = Polygon(B,C,F,color='#FFFFFF')
    right_angle_B = Polygon(B,B+np.array([0.132,0.1835,0]),B+np.array([0.132,0.1835,0])+np.array([-0.159,0.113,0]),B+np.array([-0.159,0.113,0]),color='#FFFFFF')
    AF = Line(A,F)
    AB = Line(A,B)
    BF = Line(B,F)
    BA = Line(B,A)
    angleFAB = Angle(AF,AB,other_angle=True)
    angleFBA = Angle(BF,BA)
    ADC = Polygon(A,D,C,color='#FFFFFF')
    CF = Line(C,F)
    CD = Line(C,D)
    angleFCD = Angle(CF,CD,other_angle=True)
    AD = Line(A,D)
    angleFAD = Angle(AF,AD)
    AED = Polygon(A,E,D,color='#FFFFFF')
    AE = Line(A,E)
    angleDAE = Angle(AD,AE)
    DE = Line(D,E)
    DA = Line(D,A)
    angleEDA = Angle(DE,DA)
    Mdot = Dot(M)
    Mcongruence1 = Line((M+C)/2+np.array([0.056,-0.077,0]),(M+C)/2-np.array([0.056,-0.077,0]))
    Mcongruence2 = Line((M+F)/2+np.array([0.056,-0.077,0]),(M+F)/2-np.array([0.056,-0.077,0]))
    Xdot = Dot(X)
    AMXE = Polygon(A,M,X,E)

    self.play(ReplacementTransform(text.copy()[0],highlighted[0]))
    self.play(Create(BCF))
    self.play(FadeIn(Tex("B").scale(0.7).next_to(B),Tex("C").scale(0.7).next_to(C),Tex("F").scale(0.7).next_to(F),right_angle_B))
    self.play(ReplacementTransform(highlighted[0],highlighted[1]))
    self.play(Create(AF))
    self.play(FadeIn(Tex("A").scale(0.7).next_to(A,LEFT)))
    self.play(FadeIn(Line(A,B),angleFAB,angleFBA))
    self.play(ReplacementTransform(highlighted[1],highlighted[2]))
    self.play(Create(ADC))
    self.play(FadeIn(angleFCD,angleFAD))
    self.play(FadeIn(Tex("D").scale(0.7).next_to(D,UP)))
    self.play(ReplacementTransform(highlighted[2],highlighted[3]))
    self.play(Create(AED))
    self.play(FadeIn(angleDAE,angleEDA))
    self.play(FadeIn(Tex("E").scale(0.7).next_to(E,LEFT)))
    self.play(ReplacementTransform(highlighted[3],highlighted[4]))
    self.play(FadeIn(Mdot,Tex("M").scale(0.7).next_to(M),Mcongruence1,Mcongruence2))
    self.play(ReplacementTransform(highlighted[4],highlighted[5]))
    self.play(FadeIn(Xdot,Tex("X").scale(0.7).next_to(X,UP)))
    self.play(Create(AMXE))
    self.play(ApplyMethod(AMXE.set_color,'#FFFFFF'))
    self.play(FadeOut(text,highlighted[5]))
    self.wait(5)

class ZoomIntoShape(MovingCameraScene):
  def construct(self):
    A = np.array([-2.25,-3.3,0])
    B = np.array([0.19,-3.3,0])
    C = np.array([2.82,0.37,0])
    D = np.array([-1.03,0.37,0])
    E = np.array([-2.98,-1.03,0])
    F = np.array([-1.03,-2.43,0])
    M = np.array([0.895,-1.03,0])
    X = np.array([0.17,1.23,0])

    BCF = Polygon(B,C,F,color='#FFFFFF')
    right_angle_B = Polygon(B,B+np.array([0.132,0.1835,0]),B+np.array([0.132,0.1835,0])+np.array([-0.159,0.113,0]),B+np.array([-0.159,0.113,0]),color='#FFFFFF')
    AF = Line(A,F)
    AB = Line(A,B)
    BF = Line(B,F)
    BA = Line(B,A)
    angleFAB = Angle(AF,AB,other_angle=True)
    angleFBA = Angle(BF,BA)
    ADC = Polygon(A,D,C,color='#FFFFFF')
    CF = Line(C,F)
    CD = Line(C,D)
    angleFCD = Angle(CF,CD,other_angle=True)
    AD = Line(A,D)
    angleFAD = Angle(AF,AD)
    AED = Polygon(A,E,D,color='#FFFFFF')
    AE = Line(A,E)
    angleDAE = Angle(AD,AE)
    DE = Line(D,E)
    DA = Line(D,A)
    angleEDA = Angle(DE,DA)
    Mdot = Dot(M)
    Mcongruence1 = Line((M+C)/2+np.array([0.056,-0.077,0]),(M+C)/2-np.array([0.056,-0.077,0]))
    Mcongruence2 = Line((M+F)/2+np.array([0.056,-0.077,0]),(M+F)/2-np.array([0.056,-0.077,0]))
    Xdot = Dot(X)
    AMXE = Polygon(A,M,X,E,color='#FFFFFF')

    self.add(BCF)
    self.add(Tex("B").scale(0.7).next_to(B),Tex("C").scale(0.7).next_to(C),Tex("F").scale(0.7).next_to(F),right_angle_B)
    self.add(AF)
    self.add(Tex("A").scale(0.7).next_to(A,LEFT))
    self.add(Line(A,B),angleFAB,angleFBA)
    self.add(ADC)
    self.add(angleFCD,angleFAD)
    self.add(Tex("D").scale(0.7).next_to(D,UP))
    self.add(AED)
    self.add(angleDAE,angleEDA)
    self.add(Tex("E").scale(0.7).next_to(E,LEFT))
    self.add(Mdot,Tex("M").scale(0.7).next_to(M),Mcongruence1,Mcongruence2)
    self.add(Xdot,Tex("X").scale(0.7).next_to(X,UP))
    self.add(AMXE)
    self.play(self.camera.frame.animate.scale(1).move_to(AMXE))
    similarity1 = MathTex(r"\frac{AB}{AC}=\frac{AF}{AD}").shift(3.5*LEFT).shift(UP)
    similarity2 = MathTex(r"\frac{AD}{AC}=\frac{AF}{AB}").shift(3.5*LEFT).shift(UP)
    self.play(Write(similarity1))
    self.play(ReplacementTransform(similarity1,similarity2))
    similarity3 = MathTex(r"\triangle ABC \sim \triangle AFD").shift(3.5*LEFT).shift(UP)
    self.play(ReplacementTransform(similarity2,similarity3))
    self.play(FadeOut(similarity3))
    DF = Line(D,F)
    AFD = Polygon(A,D,F)
    ABC = Polygon(A,B,C)
    print(ABC.color)
    self.play(Create(ABC))
    self.play(Create(AFD))
    self.play(ApplyMethod(AFD.set_color,'#FFFFFF'),ApplyMethod(ABC.set_color,'#FFFFFF'),FadeIn(DF))
    self.remove(ABC)
    equation1 = MathTex(r"\angle AFD=\angle ABC").shift(3.5*LEFT).shift(UP)
    equation2 = MathTex(r"\angle AFD=90^\circ+\angle ABF").shift(3.5*LEFT).shift(UP)
    equation3 = MathTex(r"\angle AFD=180^\circ-\frac{1}{2}\angle AFB").shift(3.5*LEFT).shift(UP)
    equation4 = MathTex(r"\angle AFD=180^\circ-\frac{1}{2}\angle AED").shift(3.5*LEFT).shift(UP)
    self.play(GrowFromPoint(mobject=equation1,point=F))
    self.play(ReplacementTransform(equation1,equation2))
    self.play(ReplacementTransform(equation2,equation3))
    self.play(ReplacementTransform(equation3,equation4))




    Ecircle = Circle(radius=2.43).move_to(E)
    self.play(ApplyMethod(equation4.shift,UP))
    self.play(FadeIn(Ecircle))
    P = np.array([-5.175,0,0])
    textP = Tex("P").scale(0.7).next_to(P, LEFT)
    APDF = Polygon(A,P,D,F)
    PA = Line(P,A)
    PD = Line(P,D)
    self.play(FadeIn(PA,PD,textP))
    Pangle_text = MathTex(r"\frac{1}{2}\angle AED").next_to(P).shift(0.3*DOWN).scale(0.5)
    self.play(FadeIn(Pangle_text))




    m=0.125/4
    p=0.025
    Econgruence1 = Line(((0.5+p)*E+(0.5-p)*F)+m*np.array([1.4,1.95,0]),((0.5+p)*E+(0.5-p)*F)-m*np.array([1.4,1.95,0]))
    Econgruence2 = Line(((0.5+p)*E+(0.5-p)*A)+m*np.array([2.27,0.73,0]),((0.5+p)*E+(0.5-p)*A)-m*np.array([2.27,0.73,0]))
    Econgruence3 = Line(((0.5+p)*E+(0.5-p)*D)+np.array([0.056,-0.077,0]),((0.5+p)*E+(0.5-p)*D)-np.array([0.056,-0.077,0]))
    Econgruence4 = Line(((0.5+p)*X+(0.5-p)*M)+m*np.array([2.27,0.73,0]),((0.5+p)*X+(0.5-p)*M)-m*np.array([2.27,0.73,0]))
    Econgruence5 = Line(((0.5-p)*E+(0.5+p)*F)+m*np.array([1.4,1.95,0]),((0.5-p)*E+(0.5+p)*F)-m*np.array([1.4,1.95,0]))
    Econgruence6 = Line(((0.5-p)*E+(0.5+p)*A)+m*np.array([2.27,0.73,0]),((0.5-p)*E+(0.5+p)*A)-m*np.array([2.27,0.73,0]))
    Econgruence7 = Line(((0.5-p)*E+(0.5+p)*D)+np.array([0.056,-0.077,0]),((0.5-p)*E+(0.5+p)*D)-np.array([0.056,-0.077,0]))
    Econgruence8 = Line(((0.5-p)*X+(0.5+p)*M)+m*np.array([2.27,0.73,0]),((0.5-p)*X+(0.5+p)*M)-m*np.array([2.27,0.73,0]))
    text_group = VGroup(Pangle_text,equation4)
    text_merged = MathTex(r"\angle AFD+\frac{1}{2}\angle AED=180^\circ").shift(3.5*LEFT).shift(2*UP)
    self.play(ReplacementTransform(text_group,text_merged))
    self.play(Create(APDF))
    self.play(FadeIn(DashedVMobject(Line(E,F)),Econgruence1,Econgruence2,Econgruence3,Econgruence4,Econgruence5,Econgruence6,Econgruence7,Econgruence8))
    self.play(FadeOut(APDF))
    self.remove(APDF)
    collinearity_equation = MathTex(r"\angle EFA=\angle CFB").shift(3.5*LEFT).shift(2*UP)
    self.play(ReplacementTransform(text_merged, collinearity_equation))
    collinearity_text = Tex(r"E, F, y B son colineales!").shift(3.5*LEFT).shift(2*UP)
    self.play(ReplacementTransform(collinearity_equation, collinearity_text))
    self.play(self.camera.frame.animate.shift(LEFT))




    EGMO= ImageMobject("EGMO.png")
    EGMO.scale(2)

    self.play(FadeIn(EGMO.shift(7*LEFT)))
    self.play(FadeOut(EGMO))
    EDXcollinearity1 = MathTex(r"\angle MAD = \angle EDA").shift(3.5*LEFT).shift(2*UP)
    EDXcollinearity2 = MathTex(r"ED || AM").shift(3.5*LEFT).shift(2*UP)
    EDXcollinearity3 = Tex(r"E, D, y X son colineales!").shift(3.5*LEFT).shift(2*UP)
    self.play(ReplacementTransform(collinearity_text,EDXcollinearity1))
    self.play(ReplacementTransform(EDXcollinearity1,EDXcollinearity2))
    self.play(ReplacementTransform(EDXcollinearity2,EDXcollinearity3))

    EB = Line(E,B)

    angleEDA = Angle(Line(D,E),Line(D,A))
    ED = Line(E,D)
    AM = Line(A,M)
    
    EX = Line(E,X,color='#58c4dd')

    Edot = Dot(E,color="#58c4dd")
    Ddot = Dot(D,color="#58c4dd")
    self.play(FadeIn(EX,Edot,Ddot))
    self.play(FadeOut(Edot,Ddot,Xdot, EX))





    n = 0.025
    congruence2 = 1/4*(F+C-B)+3/4*B
    self.play(FadeIn(Line(M,B)),FadeIn(Line(congruence2-n*np.array([-4.54,1.41,0]),congruence2+n*np.array([-4.54,1.41,0]))))

    self.wait(2)

class ResumeShape(MovingCameraScene):
  def construct(self):
    A = np.array([-2.25,-3.3,0])
    B = np.array([0.19,-3.3,0])
    C = np.array([2.82,0.37,0])
    D = np.array([-1.03,0.37,0])
    E = np.array([-2.98,-1.03,0])
    F = np.array([-1.03,-2.43,0])
    M = np.array([0.895,-1.03,0])
    X = np.array([0.17,1.23,0])

    BCF = Polygon(B,C,F,color='#FFFFFF')
    right_angle_B = Polygon(B,B+np.array([0.132,0.1835,0]),B+np.array([0.132,0.1835,0])+np.array([-0.159,0.113,0]),B+np.array([-0.159,0.113,0]),color='#FFFFFF')
    AF = Line(A,F)
    AB = Line(A,B)
    BF = Line(B,F)
    BA = Line(B,A)
    angleFAB = Angle(AF,AB,other_angle=True)
    angleFBA = Angle(BF,BA)
    ADC = Polygon(A,D,C,color='#FFFFFF')
    CF = Line(C,F)
    CD = Line(C,D)
    angleFCD = Angle(CF,CD,other_angle=True)
    AD = Line(A,D)
    angleFAD = Angle(AF,AD)
    AED = Polygon(A,E,D,color='#FFFFFF')
    AE = Line(A,E)
    angleDAE = Angle(AD,AE)
    DE = Line(D,E)
    DA = Line(D,A)
    angleEDA = Angle(DE,DA)
    Mdot = Dot(M)
    Mcongruence1 = Line((M+C)/2+np.array([0.056,-0.077,0]),(M+C)/2-np.array([0.056,-0.077,0]))
    Mcongruence2 = Line((M+F)/2+np.array([0.056,-0.077,0]),(M+F)/2-np.array([0.056,-0.077,0]))
    Xdot = Dot(X)
    AMXE = Polygon(A,M,X,E,color='#FFFFFF')

    self.play(self.camera.frame.animate.scale(1).move_to(AMXE))
    self.add(BCF)
    self.add(Tex("B").scale(0.7).next_to(B),Tex("C").scale(0.7).next_to(C),Tex("F").scale(0.7).next_to(F),right_angle_B)
    self.add(AF)
    self.add(Tex("A").scale(0.7).next_to(A,LEFT))
    self.add(Line(A,B),angleFAB,angleFBA)
    self.add(ADC)
    self.add(angleFCD,angleFAD)
    self.add(Tex("D").scale(0.7).next_to(D,UP))
    self.add(AED)
    self.add(angleDAE,angleEDA)
    self.add(Tex("E").scale(0.7).next_to(E,LEFT))
    self.add(Mdot,Tex("M").scale(0.7).next_to(M),Mcongruence1,Mcongruence2)
    self.add(Xdot,Tex("X").scale(0.7).next_to(X,UP))
    self.add(AMXE)

    m=0.125/4
    p=0.025
    Econgruence1 = Line(((0.5+p)*E+(0.5-p)*F)+m*np.array([1.4,1.95,0]),((0.5+p)*E+(0.5-p)*F)-m*np.array([1.4,1.95,0]))
    Econgruence2 = Line(((0.5-p)*E+(0.5+p)*F)+m*np.array([1.4,1.95,0]),((0.5-p)*E+(0.5+p)*F)-m*np.array([1.4,1.95,0]))
    E1 = VGroup(Econgruence1,Econgruence2)
    Econgruence3 = Line(((0.5+p)*E+(0.5-p)*D)+np.array([0.056,-0.077,0]),((0.5+p)*E+(0.5-p)*D)-np.array([0.056,-0.077,0]))
    Econgruence4 = Line(((0.5-p)*E+(0.5+p)*D)+np.array([0.056,-0.077,0]),((0.5-p)*E+(0.5+p)*D)-np.array([0.056,-0.077,0]))
    E2 = VGroup(Econgruence3,Econgruence4)
    Econgruence5 = Line(((0.5-p)*E+(0.5+p)*A)+m*np.array([2.27,0.73,0]),((0.5-p)*E+(0.5+p)*A)-m*np.array([2.27,0.73,0]))
    Econgruence6 = Line(((0.5+p)*E+(0.5-p)*A)+m*np.array([2.27,0.73,0]),((0.5+p)*E+(0.5-p)*A)-m*np.array([2.27,0.73,0]))
    E3 = VGroup(Econgruence5,Econgruence6)
    Econgruence7 = Line(((0.5+p)*X+(0.5-p)*M)+m*np.array([2.27,0.73,0]),((0.5+p)*X+(0.5-p)*M)-m*np.array([2.27,0.73,0]))
    Econgruence8 = Line(((0.5-p)*X+(0.5+p)*M)+m*np.array([2.27,0.73,0]),((0.5-p)*X+(0.5+p)*M)-m*np.array([2.27,0.73,0]))
    E4 = VGroup(Econgruence7,Econgruence8)

    self.add(DashedVMobject(Line(E,F)),E1,E2,E3,E4)
    self.add(Line(M,B))
    print(M-B)
    n=0.04
    self.add(Line((M+B)/2,(M+B)/2+n*np.array([2.27,-0.705,0])))
    self.add(Line((M+B)/2,(M+B)/2+n*np.array([-2.27,0.705,0])))

    text = MathTex(r"BM=AE=XM").shift(2*UP+3*LEFT)
    text2 = MathTex(r"\triangle EMX \cong \triangle EMB").shift(2*UP+3*LEFT)
    congruence1 = Line((M+B)/2,(M+B)/2+n*np.array([2.27,-0.705,0]))
    self.play(
        ReplacementTransform(E1,Line(((0.5)*E+(0.5)*F)+m*np.array([1.4,1.95,0]),((0.5)*E+(0.5)*F)-m*np.array([1.4,1.95,0]))),
        ReplacementTransform(E2,Line(((0.5)*E+(0.5)*D)+np.array([0.056,-0.077,0]),((0.5)*E+(0.5)*D)-np.array([0.056,-0.077,0]))),
        ReplacementTransform(E3,Line(((0.5)*E+(0.5)*A)+m*np.array([2.27,0.73,0]),((0.5)*E+(0.5)*A)-m*np.array([2.27,0.73,0]))),
        ReplacementTransform(E4,Line(((0.5)*X+(0.5)*M)+m*np.array([2.27,0.73,0]),((0.5)*X+(0.5)*M)-m*np.array([2.27,0.73,0]))),
        FadeIn(Line(((0.5)*X+(0.5)*M)+m*np.array([2.27,0.73,0]),((0.5)*X+(0.5)*M)-m*np.array([2.27,0.73,0])))
        )
    self.play(Write(text))
    self.play(ReplacementTransform(text,text2))
    Line(B,E)
    Line(A,M)
    Line(E,X)
    Line((X+M)/2,(X+M)/2)
    Polygon(E,M,B)
    Polygon(E,M,X)

    
    
    EM = DashedVMobject(Line(E,M))
    FX = DashedVMobject(Line(F,X))
    DB = DashedVMobject(Line(D,B))
    EMB = Polygon(E,M,B)
    EXM = Polygon(E,X,M)
    self.play(Create(EMB))
    self.play(Create(EXM))
    self.play(Create(FX))
    self.play(Create(DB))
    text = Tex(r"$BD$ y $XF$ son simetricos a respeto a $EM$!").shift(2*UP+3*LEFT).scale(0.65)
    self.play(ReplacementTransform(text2,text))
    self.wait(2)