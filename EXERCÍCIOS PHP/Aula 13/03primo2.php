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
       $n = isset($_GET["num"])?$_GET["num"]:0;
       echo "Analisando o número $n... <br/><br/> Valores Múltiplos: ";
        for ($c= 1; $c<= $n;$c++){
            if ($n % $c==0){
                echo " $c  ";
                $t+=1;
            }
            else{
                echo " ";
            }
        }
        echo "<br/><br/>Total de múltiplos: $t <br/><br/>";
        if ($t==2){
            echo "Resultado: $n <span class='foco'>É Primo !</span>";
        }
        else {
            echo "Resultado: $n <span class='foco'>Não é primo !</span>";
        }
    ?>
	<br/><br/><a href="javascript:history.go(-1)" class="botao">Voltar</a>
</div>
</body>
</html>
 