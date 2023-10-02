<!DOCTYPE html>
<html>
<head>
  <link rel="stylesheet" href="_css/estilo.css"/>
  <meta charset="UTF-8"/>
  <title>Curso de PHP - CursoemVideo.com</title>
</head>
<body>
<div>
    <?php
        function soma ($a,$b){
            $s = $a+$b;
            echo "<p>A soma vale $s </p>";
        }
        soma(5,7);
        soma(10,51);
        soma(54,77);
        soma(55,89);
        $x = 9;
        $y = 15;
        soma($x,$y);
    ?>
</div>
</body>
</html>
 