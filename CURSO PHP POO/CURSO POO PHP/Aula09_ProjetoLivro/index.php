<!DOCTYPE html>
<!--
To change this license header, choose License Headers in Project Properties.
To change this template file, choose Tools | Templates
and open the template in the editor.
-->
<html>
    <head>
        <meta charset="UTF-8">
        <title>Aula 09</title>
    </head>
    <body>
        <pre>
        <?php
        require_once 'Pessoa.php';
        require_once 'Livro.php';
        
        
        $p[0] = new Pessoa("Pedro", 22, "M");
        $p[1] = new Pessoa("Maria", 25, "F");
        
        $l[0] = new Livro("Aprendendo Java", "José da Silva", 300, $p[0]);
        $l[1] = new Livro("POO para Iniciantes", "Pedro Paulo", 500,$p[0]);
        $l[2] = new Livro("Java Avançado", "Marai Candido", 800, $p[1]);
        
        //print_r($l[0]);
        $l[0]->abrir();
        $l[0]->folhear(100);
        //$l[0].avancarPag();
        
        $l[0]->detalhes();
        $l[1]->detalhes();
        $l[2]->detalhes();
        ?>
        </pre>
    </body>
</html>
