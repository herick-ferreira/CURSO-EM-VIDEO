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
    $es = isset($_GET["est"])?$_GET["est"]:"";
    
  switch ($es)   {
            case 1:
                $r = "Norte";
                break;
            case 2:
                $r = "Nordeste";
                break;
            case 3:
               $r = "Centro-Oeste";
                break;
            case 4:
                $r = "Sudeste";
                break;
            case 5:
                $r = "Sul";
                break;
            default:
                echo "Não sei";
                break;
        }
        
        echo "Você mora na região <span class = 'foco'>$r</span>";
   ?>
      <br/>
      <br/>
      <a href="javascript:history.go(-1)" class="botao">VOLTAR</a>
</div>
</body>
</html>
 