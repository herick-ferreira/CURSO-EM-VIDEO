<!DOCTYPE html>
<!--
To change this license header, choose License Headers in Project Properties.
To change this template file, choose Tools | Templates
and open the template in the editor.
-->
<html>
    <head>
        <meta charset="UTF-8">
        <title>Aula 11</title>
    </head>
    <body>
        <pre>
        <?php
        require_once 'Pessoa.php';
        require_once 'Visitante.php';
        require_once 'Aluno.php';
        require_once 'Bolsista.php';
        require_once 'Professor.php';
        require_once 'Tecnico.php';
        //Classe abstrata não pode ser instânciada
        //$p = new Pessoa();
        /*$v1 = new Visitante();
        $v1->setNome("Juvenal");
        $v1->setIdade(33);
        $v1->setSexo("M");
        
        print_r($v1);*/
        
        $a1 = new Aluno();
        $a1->setNome("Pedro");
        $a1->setMatricula(111111);
        $a1->setIdade(16);
        $a1->setSexo("M");
        $a1->setCurso("Informática");
        $a1->pagarMensalidade();
        
        print_r($a1);
        
        $b1 = new Bolsista();
        $b1->setMatricula(11112);
        $b1->setNome("Jubileu");
        $b1->setBolsa(12.5);
        $b1->setCurso("Administração");
        $b1->setIdade(17);
        $b1->pagarMensalidade();
        print_r($b1);
        
        $p1 = new Professor();
        $p1->setNome("Fausto");
        $p1->setSalario(2222);
        $p1->receberAumento();
        $p1->setEspecialidade("TI");
        print_r($p1);
        
        $t1 = new Tecnico();
        $t1->setCurso("Bases Numéricas");
        $t1->setNome("João");
        $t1->setRegistroProfissional(2452111);
        $t1->praticar();
        print_r($t1);
        
        ?>
        </pre>
    </body>
</html>
