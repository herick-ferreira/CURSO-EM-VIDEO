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
        $a = isset($_GET["ano"])?$_GET["ano"]:1900;
        $i = date("Y") - $a;
        echo "Você nasceu em $a e terá $i anos";
        if ($i >=18){
            $v = "já pode votar";
            $d = "já pode dirigir";
        }
        else {
            $v = "Não pode Votar";
            $d = "Não pode dirigir";
        }
        echo "<br/>Com essa idade você $v e também $d";
    ?>
</div>
</body>
</html>
 