<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8"/>
  <title>Aula04 - POO </title>
</head>
<body>
<div>
    <pre>
    <?php
        require_once('Caneta.php');
        $c1=new Caneta("Bic","Azul", 0.5);
        $c2=new Caneta("KKK","Verde",1.0);
         /*$c1-> setModelo("BIC");
           $c1->modelo = "BIC";
           $c1-> setPonta(0.5);
           $c1->ponta = 0.5;*/
     /*print "Eu tenho uma caneta {$c1->getModelo()} de ponta {$c1->getPonta()}";*/
   
        print_r($c1);
        print_r($c2);
    ?>
    </pre>
</div>
</body>
</html>
 