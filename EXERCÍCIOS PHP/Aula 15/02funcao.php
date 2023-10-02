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
    include "funcoes.php";
    /*include exige mas tenta ainda executar o que consegue mesmo não existindo o arquivo.
    require exige a criação de outro php ou html*/
    /*require_once ou include_once simplifica o processo se for chamar apenas um arquivo para o programa inteiro nao precisa copiar varias vezes*/
    echo "<h1>Testando novas funções</h1>";
    ola();
    mostraValor(4);
    echo "<h2>Finalizando o programa...</h2>";
    ?>
</div>
</body>
</html>
 