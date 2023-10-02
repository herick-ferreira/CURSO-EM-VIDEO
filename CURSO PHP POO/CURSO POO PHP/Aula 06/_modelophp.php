<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8"/>
  <title>Aula06 - POO </title>
</head>
<body>
<div>
    <h1>PROJETO CONTROLE REMOTO</h1>
    <pre>
    <?php
        require_once("ControleRemoto.php");
        $c = new ControleRemoto();
        $c->ligar();
        $c->abrirMenu();
        //$c->play();
        $c->maisVolume();
        //$c->menosVolume();
        //$c->pause();
        //$c->fecharMenu();
        //$c->ligarMudo();
        //$c->desligar();
        //$c->fecharMenu();


    ?>
    </pre>
</div>
</body>
</html>
 