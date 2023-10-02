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
       $i = isset($_GET["num"])?$_GET["num"]:1;

	   echo "Mostrando a Tabuada do $i<br/>";
	   $c=1;    
	   do {
	       $r = $i * $c;
	       echo "$i X $c = $r <br/>"; 
	       $c++;
	   } while ($c<=10);
    ?>
	<br/>
	<a href="javascript:history.go(-1)" class="botao">Voltar</a>
</div>
</body>
</html>
 