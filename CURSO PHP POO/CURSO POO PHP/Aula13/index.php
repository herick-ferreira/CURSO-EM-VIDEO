<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <title>Aula 13</title>
    </head>
    <body>
        <?php
        require_once 'Mamifero.php';
        require_once 'Cachorro.php';
        require_once 'Lobo.php';
        
        $c = new Cachorro();
        //emitirSom();
        
        $c->reagirFrase("Ola");
        $c->reagirFrase("Vai Apanhar");
        $c->reagirHora(11, 45);
        $c->reagirHora(21, 00);
        $c->reagirDono(true);
        $c->reagirDono(false);
        $c->reagirIdadePeso(2, 12.5);
        $c->reagirIdadePeso(17, 4.5);
        ?>
    </body>
</html>
