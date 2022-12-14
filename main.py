from manim import *
import PIL.Image

class Narration(Text):
    def __init__(self, *args, **kwargs) -> Text:
        super().__init__(*args, **kwargs)
        self.z_index = 999 # prioritize thyself

class Geography(Scene):
    def construct(self):
        title = Text("Растер дүрслэл вэктор дүрслэлээр ямар ялгаатай бэ?", font_size=36.0)

        self.play(Write(title))
        self.wait(1)
    
        self.play(
                *[FadeOut(mob)for mob in self.mobjects]
        )

        if True: # so vscode can fold for tidying up
            grid_title = Narration("Растер зураг")
            grid_title.z_index = 999
            grid_title.to_corner(UP+LEFT)
            self.play(Write(grid_title))
            
            image = ImageMobject("raster.jpg").scale(0.7)

            self.play(FadeIn(image), image.animate.shift(LEFT*4))
        
            grid = NumberPlane(axis_config={"color": GRAY, "stroke_width": 0.8}, x_length=4.5/0.75, y_length=4.5/0.75, x_range=[-25, 25], y_range=[-25, 25], background_line_style={"stroke_color": GRAY, "stroke_width": 1}).shift(RIGHT*4)

            arrow = Arrow()
            text = Text("томруулж", font_size=20).next_to(arrow, UP)

            self.play(Write(VGroup(arrow, text)))

            arr = np.array(PIL.Image.open("pooled.jpg"))

            def _compute(pix, i, j):
                sq = Square(color="#%02x%02x%02x" % tuple(pix), fill_opacity=1, side_length=(18*0.7/200))
                coords = grid.coords_to_point(i-60, j-60)
                return sq.move_to(coords)
            
            rasterized = VGroup(*[VGroup(*[_compute(pix, i, j) for i, pix in enumerate(row)]) for j, row in enumerate(arr)]).scale(0.7).move_to(ORIGIN)
            self.play(FadeIn(rasterized), rasterized.animate.shift(RIGHT*4))

            explanation = Text("Растер дүрслэл нь пикселийн 2 хэмжээст массив юм. Растэр давхаргатай\nгазрын зургийг томруулж үзэхэд жижиг нарийн ширийн зүйлс алдагдаж эхэлнэ", font_size=21)
            box = RoundedRectangle(0.3, width=explanation.width+2, height=explanation.height+0.5, color=GREEN, fill_color=BLACK, fill_opacity=1)
            explanation.z_index=999
            explanation.move_to(box.get_center())
            todor = VGroup(explanation, box).to_corner(DOWN)
            self.play(FadeIn(todor))

            self.wait(5)
            self.play(
                *[FadeOut(mob)for mob in self.mobjects]
            )

        if True:
            grid_title = Narration("Вектор зураг")
            grid_title.z_index = 999
            grid_title.to_corner(UP+LEFT)
            self.play(Write(grid_title))
            
            image = ImageMobject("vector.jpg").scale(0.7)

            self.play(FadeIn(image), image.animate.shift(LEFT*4))

            arrow = Arrow()
            text = Text("stripping", font_size=20).next_to(arrow, UP)

            grid = NumberPlane(x_range=[0, 20], y_range=[0, 20], x_length=5, y_length=5)

            self.play(Write(VGroup(arrow, text)))
            self.play(Write(grid), grid.animate.shift(RIGHT*4))
            self.wait(1)
            self.play(Transform(grid, grid.plot_line_graph(x_values=[0,4,10,20], y_values=[0,10,0,5])))
            self.wait(5)

            apology = Text("I was unable to get this to work, sorry!", font_size=18, color=GRAY).next_to(grid, UP).shift(UP)
            self.play(FadeIn(apology))

            explanation = Text("Вектор график нь математикийн тэгшитгэл, геометрийн дүрс дээр тулгуурладаг\nбөгөөд энэ нь нарийн ширийн зүйлийг алдагдуулахгүйгээр тасралтгүй томруулж чаддаг.", font_size=21)
            box = RoundedRectangle(0.3, width=explanation.width+2, height=explanation.height+0.5, color=GREEN, fill_color=BLACK, fill_opacity=1)


            explanation.z_index=999
            explanation.move_to(box.get_center())
            todor = VGroup(explanation, box).to_corner(DOWN)
            self.play(FadeIn(todor))

            self.wait(5)
            self.play(
                *[FadeOut(mob)for mob in self.mobjects]
            )

        if True:
            img = ImageMobject("conclusion.png").to_corner(LEFT+UP).shift(RIGHT*0.5+DOWN*0.5)
            self.play(FadeIn(img))
            suicide = Text("Газрын зураг ихэвчлэн хот, байшин, гудамжийг вэктор дүрслэлээр харуулдаг\nМөн газрын ашиглалт, хотгор, гүдгэрийг растэр дүрслэлийг ашигладаг", font_size=21)
            box = RoundedRectangle(0.3, width=explanation.width+2, height=explanation.height+0.5, color=GREEN, fill_color=BLACK, fill_opacity=1)
            explanation.z_index=999
            explanation.move_to(box.get_center())
            todor = VGroup(suicide, box).to_corner(DOWN)
            self.play(FadeIn(todor))
            self.wait(10)
            self.play(
                *[FadeOut(mob)for mob in self.mobjects]
            )
            self.wait(2)