<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8"/>
  <title>Aula05 - POO </title>
</head>
<body>
<div>
    <pre>
    <?php
        require_once("contaBanco.php");
        $p1 = new ContaBanco();// Jubileu
        $p2 = new ContaBanco();// Creuza
        
        $p1->setDono("Jubileu");
        $p1->abrirConta("cc");

        $p2->setDono("Creuza");
        $p2->abrirConta("cp");
        
        $p1->depositar(300);
        $p2->depositar(500);
        
        $p2->sacar(1000);
        
        $p1->pagarMensal();
        $p2->pagarMensal();
        
        $p2->sacar(1000);
        
        $p1->sacar(330);
        $p2->sacar(630);
        
        $p1->fecharConta();
        $p2->fecharConta();
        
        print_r($p1);
        print_r($p2);
        
    ?>
    </pre>
</div>
</body>
</html>
 