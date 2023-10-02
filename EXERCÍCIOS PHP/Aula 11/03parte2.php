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
        $i = isset($_GET["ini"])?$_GET["ini"]:0;
        $f = isset($_GET["fim"])?$_GET["fim"]:0;
        $in = isset($_GET["inc"])?$_GET["inc"]:0;
        if ($i<$f){
        $c = $i;
            while ($c<=$f){
                echo "$c ";
                $c+=$in;
            }
        }
        else {
        $c = $i;
            while ($c>=$f){
                 echo "$c ";
                 $c-= $in ;           
          }
        }
    ?>
</div>
</body>
</html>
 