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
        $frase = "Eu vou estudar PHP";
        $cont = str_word_count($frase,0);
        echo "$cont<br/>";
        $cont2 = str_word_count($frase,1);
        print_r($cont2);
        $cont3 = str_word_count($frase,2);
        print_r($cont3);
        
    ?>
</div>
</body>
</html>
 