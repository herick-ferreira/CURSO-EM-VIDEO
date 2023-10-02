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
       $n1 = isset($_GET["nota1"])?$_GET["nota1"]:0;
       $n2 = isset($_GET["nota2"])?$_GET["nota2"]:0;
       $m = ($n1+$n2)/2;
       echo "A média entre $n1 e $n2 é igual a ".number_format($m,1);
       if ($m<5){
           $situacao = "REPROVADO";
       }
       elseif (($m>=5) && ($m<7)){
           $situacao = "RECUPERAÇÃO";
       }
       else{
           $situacao = "APROVADO";
       }
       echo "<br/>Situação do aluno: $situacao<br/>";
    ?>
    <a href="exercício03.html" class="botao">VOLTAR</a>
</div>
</body>
</html>
 